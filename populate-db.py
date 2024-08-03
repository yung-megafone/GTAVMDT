## For testing purposes, main script now generates registration info on the fly
## Not even close to lspdfr tho :(
# Property of NoviX Development
# https://nsic.dev/
# Coded by yung-megafone
# Write some code to do some things that'll accomplish some task
import random
import string

def generate_license_plate():
    """
    Generates a random license plate in the format:
    NNLLLNNN (where N is a digit and L is a capital letter)
    """
    numbers = ''.join(random.choices(string.digits, k=2))
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    return f"{numbers}{letters}{numbers}"

def generate_random_name():
    first_names = ['John', 'Jane', 'Michael', 'Emily', 'David', 'Sarah', 'James', 'Emma', 'William', 'Olivia']
    last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor']
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_random_gender():
    return random.choice(['Male', 'Female', 'Non-Binary'])

def generate_random_race():
    return random.choice(['White', 'Black', 'Asian', 'Hispanic', 'Other'])

def generate_random_vehicle_description():
    vehicle_types = ['Sedan', 'SUV', 'Truck', 'Motorcycle', 'Van']
    colors = ['Red', 'Blue', 'Black', 'White', 'Silver', 'Gray']
    return f"{random.choice(colors)} {random.choice(vehicle_types)}"

def generate_random_prior_incidents():
    return random.choice(['None', 'Minor accident', 'Major accident', 'Traffic violation'])

def generate_random_risk_level():
    return random.choice(['high', 'medium', 'low'])

def main():
    file_name = "output.txt"

    # Ask user for number of entries to generate
    while True:
        try:
            num_entries = int(input("Enter the number of entries to generate: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    with open(file_name, 'w') as f:
        for _ in range(num_entries):
            plate_number = generate_license_plate()
            name = generate_random_name()
            gender = generate_random_gender()
            race = generate_random_race()
            vehicle_desc = generate_random_vehicle_description()
            prior_incidents = generate_random_prior_incidents()
            risk_level = generate_random_risk_level()

            f.write(f"{plate_number},{name},{gender},{race},{vehicle_desc},{prior_incidents},{risk_level}\n")

    print(f"{num_entries} entries generated and saved to {file_name}.")

if __name__ == "__main__":
    main()
