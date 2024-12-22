import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import classification_report, mean_squared_error
from persona import names

# Step 1: Load the data from the CSV
def load_data(csv_path):
    df = pd.read_csv(csv_path)

    # Step 2: Handle missing values
    # Separate numeric and categorical columns
    numeric_cols = df.select_dtypes(include=['number']).columns
    categorical_cols = df.select_dtypes(exclude=['number']).columns

    # Fill missing numeric data with the mean
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    # Fill missing categorical data with the most frequent value (mode)
    for col in categorical_cols:
        df[col] = df[col].fillna(df[col].mode()[0])  # Filling with mode of the column

    return df

# Step 3: Preprocess the data (excluding Education and Occupation)
def preprocess_data(df):
    # Encode only numeric columns, not Education or Occupation
    label_encoder = LabelEncoder()
    categorical_cols = df.select_dtypes(exclude=['number']).columns.difference(['Education', 'Occupation'])

    for col in categorical_cols:
        df[col] = label_encoder.fit_transform(df[col])

    # Separate features (X) and target variables (y)
    X = df[['Product Type']]  # Using 'Product Type' as input
    y = df.drop(columns=['Product Type', 'Education', 'Occupation'])  # Exclude 'Education' and 'Occupation' from y

    return X, y, label_encoder, df['Education'], df['Occupation']  # Return original 'Education' and 'Occupation'

# Step 4: Train the model (one per column in y)
def train_model(X_train, y_train):
    models = {}
    
    for col in y_train.columns:
        if y_train[col].dtype == 'object':  # If the column is categorical
            model = RandomForestClassifier(n_estimators=100, random_state=42)
        else:  # If the column is continuous
            model = RandomForestRegressor(n_estimators=100, random_state=42)
        
        model.fit(X_train, y_train[col])
        models[col] = model
    
    return models

# Step 5: Evaluate the model
def evaluate_model(models, X_test, y_test):
    for col, model in models.items():
        y_pred = model.predict(X_test)
        if isinstance(model, RandomForestClassifier):
            print(f"Classification Report for {col}:")
            print(classification_report(y_test[col], y_pred))
        else:
            print(f"Mean Squared Error for {col}:")
            print(mean_squared_error(y_test[col], y_pred))

# Step 6: Get input from user and predict the values
def predict_from_input(models, product_type, label_encoder, original_education, original_occupation):
    # Encode the product type using the same label_encoder used during training
    encoded_product_type = label_encoder.transform([product_type])

    input_data = pd.DataFrame({'Product Type': encoded_product_type})

    # Predict for all other columns (excluding Education and Occupation)
    predictions = {}
    for col, model in models.items():
        prediction = model.predict(input_data)
        
        # Convert prediction to integer (round if necessary)
        predictions[col] = int(round(prediction[0]))  # Convert to integer

    # Convert Education and Occupation back to the original string values from the original dataset
    education_prediction = original_education.mode()[0]  # Most frequent value of Education
    occupation_prediction = original_occupation.mode()[0]  # Most frequent value of Occupation
    
    # Add Education and Occupation to the predictions
    predictions['Education'] = education_prediction
    predictions['Occupation'] = occupation_prediction
    
    return predictions

# Main function to run the steps
def main():
    # Load the data
    df = load_data('kblg.csv')
    
    # Preprocess the data
    X, y, label_encoder, original_education, original_occupation = preprocess_data(df)

    # Step 5: Split the data into training and testing sets (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Step 6: Train the models
    models = train_model(X_train, y_train)

    # Step 7: Evaluate the models
    evaluate_model(models, X_test, y_test)

    # Step 8: Get user input for Product Type and make predictions
    product_type = input("Enter the Product Type: ")
    predictions = predict_from_input(models, product_type, label_encoder, original_education, original_occupation)
    
    # Display predictions
    print("\nPredicted Persona based on the given Product Type:")
    name=names('All')
    print(f"Persona Name: {name}")
    print('*'*33)
    for col, pred in predictions.items():
        print(f"{col}: {pred}")

if __name__ == '__main__':
    main()

