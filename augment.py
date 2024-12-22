import pandas as pd
import random

# Expanded list of education levels
education_levels = [
    "No Formal Education", "High School", "Associate's Degree", "Bachelor's Degree", "Master's Degree", 
    "PhD", "MBA", "Certification", "Self-Taught", "Associate Degree", "Professional Training", 
    "Doctoral Degree", "Vocational Training", "Trade School", "Postdoctoral Studies", "Graduate Diploma"
]

# Expanded list of occupations
occupations = [
    "Unemployed", "Software Engineer", "Data Scientist", "Freelance Designer", "University Professor",
    "UX/UI Designer", "Customer Support", "Retail Worker", "Construction Worker", "Tech CEO",
    "Dentist", "Physician", "Gardener", "Sales Agent", "Marketer", "Public Speaker", "Business Analyst", 
    "Product Manager", "Project Manager", "Nurse", "Teacher", "Lawyer", "Architect", "Engineer", "Scientist", 
    "Pharmacist", "Writer", "Editor", "Social Media Manager", "Artist", "Chef", "Waiter", "Realtor", 
    "Mechanic", "Electrician", "Photographer", "Accountant", "IT Consultant", "HR Manager", "Financial Analyst", 
    "Event Planner", "Tourism Manager", "Construction Manager", "Copywriter", "Web Developer", "Graphic Designer", 
    "Civil Engineer", "Investment Banker", "Social Worker", "Public Relations Specialist"
]

# Expanded list of product types
product_types = [
    "Mobile App", "Web Application", "E-commerce", "Enterprise Software", "Design Software", 
    "Educational Platform", "SaaS Platform", "Gaming Platform", "Cloud Storage", "IoT Platform", 
    "Artificial Intelligence Tool", "Cybersecurity Tool", "Health & Fitness App", "Streaming Service", 
    "E-learning Tool", "Productivity Tool", "Business Intelligence Software", "Finance & Accounting Software", 
    "CRM Tool", "HR Management Software", "Project Management Tool", "Communication Tool", "Travel App", 
    "Food Delivery App", "Video Editing Software", "Music Production Software", "Collaboration Tool", 
    "Data Analytics Tool", "Real Estate Software", "Marketing Automation Tool", "Photo Editing Software", 
    "Remote Work Tool", "Virtual Reality Tool", "Augmented Reality App", "Blockchain Platform", 
    "Learning Management System", "Personal Finance Tool", "Customer Feedback Tool", "Survey Platform"
]

# Define logic to map education levels to certain occupations
education_to_occupation_map = {
    "No Formal Education": ["Retail Worker", "Construction Worker", "Waiter", "Gardener", "Sales Agent"],
    "High School": ["Retail Worker", "Sales Agent", "Construction Worker", "Gardener", "Mechanic", "Electrician"],
    "Associate's Degree": ["Customer Support", "UX/UI Designer", "Web Developer", "Photographer", "Nurse"],
    "Bachelor's Degree": ["Software Engineer", "Data Scientist", "Product Manager", "Teacher", "Architect", "Designer"],
    "Master's Degree": ["University Professor", "Engineer", "Scientist", "Lawyer", "Pharmacist"],
    "PhD": ["University Professor", "Scientist", "Engineer", "Researcher"]
}

# Define logic to map occupations to product types
occupation_to_product_map = {
    "Software Engineer": ["Enterprise Software", "SaaS Platform", "Cloud Storage", "Artificial Intelligence Tool"],
    "Data Scientist": ["Business Intelligence Software", "Data Analytics Tool", "Artificial Intelligence Tool"],
    "Freelance Designer": ["Design Software", "Photo Editing Software", "Video Editing Software"],
    "University Professor": ["Educational Platform", "E-learning Tool", "CRM Tool"],
    "UX/UI Designer": ["Design Software", "Web Application", "Mobile App"],
    "Retail Worker": ["Mobile App", "E-commerce", "Food Delivery App"],
    "Construction Worker": ["Project Management Tool", "Communication Tool"],
    "Tech CEO": ["Enterprise Software", "CRM Tool", "Business Intelligence Software", "Project Management Tool"]
}

# Function to generate a random row based on education, occupation, and product type logic
def generate_row():
    # Randomly select education level
    education = random.choice(education_levels)
    
    # Ensure occupation list exists for the chosen education level
    if education in education_to_occupation_map:
        occupation = random.choice(education_to_occupation_map[education])
    else:
        # If the education level doesn't have a corresponding list, fallback to a default list
        occupation = random.choice(occupations)
    
    # Map occupation to potential product types
    product_type = random.choice(occupation_to_product_map.get(occupation, product_types))
    
    # Generate random values for proficiency, frustration, etc., with basic logic based on occupation
    proficiency = random.randint(0, 10)
    frustration = random.randint(0, 10)
    curiosity = random.randint(0, 10)
    
    # Adjust tech savviness, flexibility, and intuition based on occupation and education
    if occupation in ["Software Engineer", "Data Scientist", "Web Developer"]:
        tech_savviness = random.randint(7, 10)
    else:
        tech_savviness = random.randint(0, 6)
    
    if occupation in ["Tech CEO", "Product Manager", "Engineer"]:
        tech_flexibility = random.randint(7, 10)
    else:
        tech_flexibility = random.randint(0, 6)
    
    if occupation in ["Freelance Designer", "Artist", "Teacher"]:
        level_of_intuition = random.randint(7, 10)
    else:
        level_of_intuition = random.randint(0, 6)
    
    pain_points = random.randint(0, 10)
    functional_need = random.randint(0, 10)
    emotional_need = random.randint(0, 10)
    
    # Return the generated row as a dictionary
    return {
        "Education": education,
        "Occupation": occupation,
        "Proficiency": proficiency,
        "Level of Frustration": frustration,
        "Curiosity": curiosity,
        "Tech Savviness": tech_savviness,
        "Tech Flexibility": tech_flexibility,
        "Level of Intuition": level_of_intuition,
        "Pain Points": pain_points,
        "Functional Need": functional_need,
        "Emotional Need": emotional_need,
        "Product Type": product_type
    }

# Function to generate a dataset with multiple rows
def generate_data(num_rows=900):
    data = [generate_row() for _ in range(num_rows)]
    return pd.DataFrame(data)

# Generate 1300 rows of synthetic data
df = generate_data(900)

# Save the data to a CSV file
df.to_csv('kblg.csv', index=False)

# Print the first 5 rows of the dataset
print(df.head())
