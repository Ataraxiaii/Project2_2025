# Program: Plant Moisture Sensor with Email Notification
# Author: Xuanru Guo
# Student Number: W20109677
# Date: 23/4/2025
# Description: send daily email reports using GPIO moisture sensor input
# Course & Year: Project Semester 3

import smtplib
from email.message import EmailMessage
from gpiozero import Button
from datetime import datetime
import schedule
import time

# ===== Email Configuration =====
FROM_EMAIL = "1241428411@qq.com"
FROM_PASSWORD = "qpxzanjnrhwejejh"  # QQ Mail app password
TO_EMAIL = "2722458837@qq.com"
SMTP_SERVER = "smtp.qq.com"
SMTP_PORT = 587

# ===== Moisture Sensor Configuration =====
MOISTURE_PIN = 17
sensor = Button(MOISTURE_PIN, pull_up=True, bounce_time=0.2)

# ===== Water Status (updated in real-time) =====
# True = Dry (no water detected): watering needed
# False = Wet (water detected): no watering needed
water_needed = not sensor.is_pressed  # Initial status on startup

# Callback when water is detected (button pressed)
def on_water_detected():
    global water_needed
    water_needed = False
    # print("Water detected: Plant does NOT need watering.")

# Callback when no water is detected (button released)
def on_no_water():
    global water_needed
    water_needed = True
    # print("No water detected: Plant NEEDS watering.")

# Attach sensor callbacks
sensor.when_pressed = on_water_detected
sensor.when_released = on_no_water

# ===== Email Sending Function =====
def send_email():
    now = datetime.now()
    status = "Plant NEEDS watering" if water_needed else "Plant does NOT need watering"
    timestamp = now.strftime('%Y-%m-%d %H:%M:%S')

    body = f"""Plant Status Report
    
	Timestamp: {timestamp}
	Current Condition: {status}
	"""

    msg = EmailMessage()
    msg.set_content(body)
    msg['From'] = FROM_EMAIL
    msg['To'] = TO_EMAIL
    msg['Subject'] = f"[Plant Daily] {status} - {now.strftime('%H:%M')}"

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    try:
        server.starttls()
        server.login(FROM_EMAIL, FROM_PASSWORD)
        server.send_message(msg)
        print(f"[{timestamp}] Email sent successfully: {status}")
    except Exception as e:
        print(f"[{timestamp}] Error during email send: {e}")
    finally:
        server.quit()


# ===== Schedule Email Times =====
send_times = ["07:00", "10:00", "13:00", "16:00"]
for t in send_times:
    schedule.every().day.at(t).do(send_email)
    print(f"Scheduled email at {t} every day.")

# ===== Main Loop =====
print("Plant Moisture Monitoring System is running...")

try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("Program manually terminated.")
