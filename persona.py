import random
import pandas as data

#Main testing the local library
def main():
    name = names('Male')
    print(f"Generated name is: {name}")

#Picking a random name by gender from the profiles CSV
def names(sexe):
    df = data.read_csv('profiles.csv', delimiter=';')
    
    if sexe == "Male":
        return random.choice(df['Male'].dropna().tolist())
    elif sexe == "Female":
        return random.choice(df['Female'].dropna().tolist())
    else:
        all_names = df['Male'].dropna().tolist() + df['Female'].dropna().tolist()
        return random.choice(all_names)
        

if __name__ == "__main__":
    main()