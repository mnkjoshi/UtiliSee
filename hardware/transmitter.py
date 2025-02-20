import serial
import time
import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase
cred = credentials.Certificate("firebase_config.json")  # Path to your service account key
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-database-name.firebaseio.com/'  # Replace with your database URL
})

# Open serial connection
ser = serial.Serial('COM3', 9600)  # Change 'COM3' to your Arduino port (Linux/Mac: '/dev/ttyUSB0')
time.sleep(2)  # Give time for the serial connection to establish

# Reference to Firebase database
ref = db.reference("arduino_data")  # Root node in Firebase

print("Reading data from Arduino and sending to Firebase...")

while True:
    try:
        line = ser.readline().decode('utf-8').strip()  # Read and decode serial data
        if line:
            print("Received:", line)

            # Parse the data (expects format: "Power: XX.XX mW | Energy: XX.XX mWh")
            parts = line.split("|")
            power = float(parts[0].split(":")[1].strip().split(" ")[0])  # Extract power in mW
            energy = float(parts[1].split(":")[1].strip().split(" ")[0])  # Extract energy in mWh

            # Create a timestamped entry in Firebase
            data_entry = {
                "power_mW": power,
                "energy_mWh": energy,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            ref.push(data_entry)

            print("Data sent to Firebase:", data_entry)

    except Exception as e:
        print("Error:", e)

    time.sleep(1)  # Avoid spamming Firebase
