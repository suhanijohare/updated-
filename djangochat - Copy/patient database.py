import sqlite3

# Connect to the SQLite database (it will create a database if it doesn't exist)
conn = sqlite3.connect('hospital_emergency.db')
cursor = conn.cursor()

# Create a table for storing patient details
cursor.execute('''CREATE TABLE IF NOT EXISTS patients (
                    patient_id TEXT PRIMARY KEY,
                    name TEXT,
                    age INTEGER,
                    disease TEXT,
                    blood_pressure TEXT,
                    oxygen_level INTEGER,
                    gender TEXT,
                    temperature REAL,
                    other_details TEXT
                )''')

# Function to add patient details
def add_patient():
    patient_id = input("Enter patient ID: ")
    
    # Check if the patient ID already exists
    cursor.execute('SELECT * FROM patients WHERE patient_id = ?', (patient_id,))
    if cursor.fetchone():
        print("Error: Patient ID already exists. Please try again with a unique ID.")
        return
    
    name = input("Enter patient's name: ")
    age = int(input("Enter patient's age: "))
    disease = input("Enter patient's disease: ")
    blood_pressure = input("Enter patient's blood pressure (e.g., 120/80): ")
    oxygen_level = int(input("Enter patient's oxygen level: "))
    gender = input("Enter patient's gender (M/F/O): ")
    temperature = float(input("Enter patient's temperature (in Celsius): "))
    other_details = input("Enter other patient details (optional): ")

    cursor.execute('''INSERT INTO patients (patient_id, name, age, disease, blood_pressure, oxygen_level, gender, temperature, other_details)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                   (patient_id, name, age, disease, blood_pressure, oxygen_level, gender, temperature, other_details))
    conn.commit()
    print("Patient details added successfully.")

# Function to retrieve patient details by different criteria
def retrieve_patient():
    print("\nRetrieve patient details by:")
    print("1. Patient ID")
    print("2. Disease")
    print("3. Age Range")
    print("4. All Patients")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        patient_id = input("Enter the patient ID: ")
        cursor.execute('SELECT * FROM patients WHERE patient_id = ?', (patient_id,))
    elif choice == '2':
        disease = input("Enter the disease: ")
        cursor.execute('SELECT * FROM patients WHERE disease LIKE ?', ('%' + disease + '%',))
    elif choice == '3':
        min_age = int(input("Enter the minimum age: "))
        max_age = int(input("Enter the maximum age: "))
        cursor.execute('SELECT * FROM patients WHERE age BETWEEN ? AND ?', (min_age, max_age))
    elif choice == '4':
        cursor.execute('SELECT * FROM patients')
    else:
        print("Invalid choice. Please try again.")
        return
    
    # Fetch and display all patients from the query
    patients = cursor.fetchall()
    
    if patients:
        print("\n--- Patient Details ---")
        for patient in patients:
            print(f"\nPatient ID: {patient[0]}")
            print(f"Name: {patient[1]}")
            print(f"Age: {patient[2]}")
            print(f"Disease: {patient[3]}")
            print(f"Blood Pressure: {patient[4]}")
            print(f"Oxygen Level: {patient[5]}")
            print(f"Gender: {patient[6]}")
            print(f"Temperature: {patient[7]}")
            print(f"Other Details: {patient[8]}")
    else:
        print("No patient found for the selected criteria.")

# Main program loop
def main():
    while True:
        print("\n1. Add patient details")
        print("\n2. Retrieve patient details")
        print("\n3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            add_patient()
        elif choice == '2':
            retrieve_patient()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

    conn.close()

# Run the program
if __name__ == "__main__":
    main()
