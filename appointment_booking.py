import random

hospitals = ["Hospital A", "Hospital B", "Hospital C"]
doctors = ["Doctor 1", "Doctor 2", "Doctor 3"]
appointment_times = ["10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM", "3:00 PM", "4:00 PM", "5:00 PM"]

def book_appointment(hospital, doctor, appointment_time):
  # Check if the appointment time is available.
  if appointment_time not in appointment_times:
    return False

  # Book the appointment.
  appointment_times.remove(appointment_time)

  # Return success.
  return True

if __name__ == "__main__":
  # Get the selected hospital and doctor.
  hospital = input("Enter the selected hospital: ")
  doctor = input("Enter the selected doctor: ")

  # Get the selected appointment time.
  appointment_time = input("Enter the selected appointment time: ")

  # Book the appointment.
  result = book_appointment(hospital, doctor, appointment_time)

  # Print the result.
  if result:
    print("Appointment booked successfully!")
  else:
    print("Failed to book appointment.")
