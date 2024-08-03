# Property of NoviX Development
# https://nsic.dev/
# Coded by yung-megafone
# Write some code to do some things that'll accomplish some task

# GTA V MDT script for roleplaying
# Graphic and disturbing content, this is your warning
# Run a GTAV license plate (Or any NNLLLNNN formatted input) and itll come back with information
# Proceed as you wish, officer.

import random
import os
import tkinter as tk
from tkinter import simpledialog, messagebox

# Generate random registration data
def generate_random_name():
    first_names = ['John', 'Jane', 'Michael', 'Emily', 'David', 'Sarah', 'James', 'Emma', 'William', 'Olivia']
    last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor']
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_random_gender():
    return random.choice(['Male', 'Female', 'Non-Binary'])

def generate_random_race():
    return random.choice(['White', 'Black', 'Asian', 'Hispanic', 'Other'])

def generate_random_vehicle_color():
    colors = ['Red', 'Blue', 'Black', 'White', 'Silver', 'Gray']
    return random.choice(colors)

def generate_random_vehicle_type():
    vehicle_types = ['Sedan', 'SUV', 'Truck', 'Motorcycle', 'Van']
    return random.choice(vehicle_types)

def generate_random_prior_incidents():
    return random.choice(['None', 'Minor accident', 'Major accident', 'Traffic violation'])

def generate_random_risk_level():
    return random.choice(['high', 'medium', 'low'])

def generate_random_kill_marker(gender, race):
    if gender == 'Non-Binary' or race != 'White':
        return 'Kill'
    else:
        return random.choice(['Confirmed Kill', 'Hit - Accident', 'Hit - High Profile', 'Kill', 'No Kill'])

def is_valid_plate_format(input_plate):
    if len(input_plate) == 8:
        if input_plate[:2].isdigit() and input_plate[2:5].isalpha() and input_plate[5:].isdigit():
            return True
    return False

# Load plate data from text file
def load_plate_data(file_name):
    plate_data = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    plate_number, name, gender, race, vehicle_color, vehicle_type, prior_incidents, risk_level, kill_marker = line.split(',')
                    plate_data[plate_number] = {
                        'name': name,
                        'gender': gender,
                        'race': race,
                        'vehicle_color': vehicle_color,
                        'vehicle_type': vehicle_type,
                        'prior_incidents': prior_incidents,
                        'risk_level': risk_level,
                        'kill_marker': kill_marker
                    }
    except FileNotFoundError:
        pass  # No existing file, return empty dictionary
    return plate_data

# save plate data to text file 
def save_plate_data(file_name, plate_data):
    with open(file_name, 'w') as file:
        for plate_number, data in plate_data.items():
            name = data.get('name', 'Not specified')
            gender = data.get('gender', 'Not specified')
            race = data.get('race', 'Not specified')
            vehicle_color = data.get('vehicle_color', 'Not specified')
            vehicle_type = data.get('vehicle_type', 'Not specified')
            prior_incidents = data.get('prior_incidents', 'None')
            risk_level = data.get('risk_level', 'Unknown')
            kill_marker = data.get('kill_marker', 'Unknown')
            file.write(f"{plate_number},{name},{gender},{race},{vehicle_color},{vehicle_type},{prior_incidents},{risk_level},{kill_marker}\n")

# Display plate information in a popup dialog
def display_plate_info(plate_data, input_plate):
    if input_plate in plate_data:
        plate_info = plate_data[input_plate]
    else:
        plate_info = {
            'name': generate_random_name(),
            'gender': generate_random_gender(),
            'race': generate_random_race(),
            'vehicle_color': generate_random_vehicle_color(),
            'vehicle_type': generate_random_vehicle_type(),
            'prior_incidents': generate_random_prior_incidents(),
            'risk_level': generate_random_risk_level(),
            'kill_marker': generate_random_kill_marker('', '')
        }

    root = tk.Tk()
    root.title(f"Plate Information: {input_plate}")
    root.configure(bg='#1f2833')  # Dark mint style background color

    tk.Label(root, text=f"Plate Number: {input_plate}", bg='#1f2833', fg='#66fcf1', font=('Arial', 14)).pack(pady=10)

    tk.Label(root, text=f"Name: {plate_info['name']}", bg='#1f2833', fg='#66fcf1', font=('Arial', 12)).pack(pady=5)
    create_edit_button(root, plate_data, input_plate, plate_info, 'name')

    tk.Label(root, text=f"Gender: {plate_info['gender']}", bg='#1f2833', fg='#66fcf1', font=('Arial', 12)).pack(pady=5)
    create_edit_button(root, plate_data, input_plate, plate_info, 'gender')

    tk.Label(root, text=f"Race: {plate_info['race']}", bg='#1f2833', fg='#66fcf1', font=('Arial', 12)).pack(pady=5)
    create_edit_button(root, plate_data, input_plate, plate_info, 'race')

    tk.Label(root, text=f"Vehicle Color: {plate_info['vehicle_color']}", bg='#1f2833', fg='#66fcf1', font=('Arial', 12)).pack(pady=5)
    create_edit_button(root, plate_data, input_plate, plate_info, 'vehicle_color')

    tk.Label(root, text=f"Vehicle Type: {plate_info['vehicle_type']}", bg='#1f2833', fg='#66fcf1', font=('Arial', 12)).pack(pady=5)
    create_edit_button(root, plate_data, input_plate, plate_info, 'vehicle_type')

    tk.Label(root, text=f"Prior Incidents: {plate_info['prior_incidents']}", bg='#1f2833', fg='#66fcf1', font=('Arial', 12)).pack(pady=5)
    create_edit_button(root, plate_data, input_plate, plate_info, 'prior_incidents')

    tk.Label(root, text=f"Risk Level: {plate_info['risk_level']}", bg='#1f2833', fg='#66fcf1', font=('Arial', 12)).pack(pady=5)
    tk.Label(root, text=f"Kill Marker: {plate_info['kill_marker']}", bg='#1f2833', fg='#66fcf1', font=('Arial', 12)).pack(pady=5)

    tk.Button(root, text="Close", command=root.destroy, bg='#45a29e', fg='#1f2833', font=('Arial', 12)).pack(pady=10)

    root.mainloop()

# create edit button for each field
def create_edit_button(root, plate_data, input_plate, plate_info, field_name):
    def edit_field():
        new_value = simpledialog.askstring(f"Edit {field_name}", f"Enter new {field_name}:",
                                           initialvalue=plate_info[field_name])
        if new_value is not None:
            plate_info[field_name] = new_value
            plate_data[input_plate] = plate_info  # Update plate_data
            save_plate_data("plates.txt", plate_data)
            messagebox.showinfo("Information Updated", f"{field_name.capitalize()} updated successfully.")
            root.destroy()  # Close current window after update
            display_plate_info(plate_data, input_plate)  # Re-display updated information

    tk.Button(root, text="Edit", command=edit_field, bg='#45a29e', fg='#1f2833', font=('Arial', 10)).pack(pady=2)

# main function to interact with user
def main():
    file_name = "plates.txt"
    plate_data = load_plate_data(file_name)

    root = tk.Tk()
    root.title("Plate Lookup")
    root.configure(bg='#1f2833')  # Dark mint style background color

    tk.Label(root, text="Enter Plate Number (NNLLLNNN format):", bg='#1f2833', fg='#66fcf1', font=('Arial', 14)).pack(pady=10)

    plate_entry = tk.Entry(root, bg='#C5C6C7', fg='#1f2833', font=('Arial', 14))
    plate_entry.pack(padx=20, ipadx=50, ipady=5)
    plate_entry.focus_set()  # Set focus to plate entry field

    def handle_enter(event):
        search_plate()

    root.bind('<Return>', handle_enter)  # Bind Enter key to search function

    def search_plate():
        input_plate = plate_entry.get().strip().upper()
        if input_plate == 'E' or input_plate == 'EXIT':
            root.destroy()
            return

        if not is_valid_plate_format(input_plate):
            messagebox.showwarning("Invalid Plate Format", "Plate number should be in NNLLLNNN format.")
            return

        display_plate_info(plate_data, input_plate)

    search_button = tk.Button(root, text="Search Plate", command=search_plate, bg='#45a29e', fg='#1f2833', font=('Arial', 12))
    search_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
