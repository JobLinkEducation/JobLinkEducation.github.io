hospitals = ["Apollo Hospital", "Fortis Hospital", "Max Hospital"]
doctors = {
    "Apollo Hospital": ["Dr. Smith", "Dr. Jones", "Dr. Brown"],
    "Fortis Hospital": ["Dr. Green", "Dr. Blue", "Dr. Red"],
    "Max Hospital": ["Dr. White", "Dr. Black", "Dr. Yellow"],
}
appointment_times = {
    "Apollo Hospital": {
        "Dr. Smith": ["10:00 AM", "11:00 AM", "12:00 PM"],
        "Dr. Jones": ["2:00 PM", "3:00 PM", "4:00 PM"],
        "Dr. Brown": ["5:00 PM", "6:00 PM", "7:00 PM"],
    },
    "Fortis Hospital": {
        "Dr. Green": ["10:00 AM", "11:00 AM", "12:00 PM"],
        "Dr. Blue": ["2:00 PM", "3:00 PM", "4:00 PM"],
        "Dr. Red": ["5:00 PM", "6:00 PM", "7:00 PM"],
    },
    "Max Hospital": {
        "Dr. White": ["10:00 AM", "11:00 AM", "12:00 PM"],
        "Dr. Black": ["2:00 PM", "3:00 PM", "4:00 PM"],
        "Dr. Yellow": ["5:00 PM", "6:00 PM", "7:00 PM"],
    },
}


# Get the hospital name
print("Here are the available hospitals:")
for hospital in hospitals:
    print(f"* {hospital}")

hospital_name = input("Enter the hospital name: ")

# Check if the hospital name is valid
if hospital_name not in hospitals:
    print("Invalid hospital name.")
    exit()

# Get the doctor name
print("Here are the available doctors at {}:".format(hospital_name))
for doctor in doctors[hospital_name]:
    print(f"* {doctor}")

doctor_name = input("Enter the doctor name: ")

# Check if the doctor name is valid
if doctor_name not in doctors[hospital_name]:
    print("Invalid doctor name.")
    exit()

# Get the appointment time
print("Here are the available appointment times for {} {}:".format(doctor_name, hospital_name))
for appointment_time in appointment_times[hospital_name][doctor_name]:
    print(f"* {appointment_time}")

appointment_time = input("Enter the appointment time: ")

# Check if the appointment time is valid
if appointment_time not in appointment_times[hospital_name][doctor_name]:
    print("Invalid appointment time.")
    exit()

# Update the appointment
appointment_times[hospital_name][doctor_name].remove(appointment_time)

print("Appointment booked successfully!")
