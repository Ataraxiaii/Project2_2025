# 🌱 Plant Moisture Monitor with Email Notification

This is a Python project designed for Raspberry Pi.  
It monitors soil moisture using a GPIO-connected sensor and sends **daily email reports** at scheduled times.

---

## 🧠 Project Overview

- **Project Type**: Agile IoT Sensor System
- **Platform**: Raspberry Pi
- **Sensor**: Digital Soil Moisture Sensor
- **Output**: Email alerts via SMTP
- **Development**: Managed via Scrum + Sprint + Burndown chart

---

## 📦 Features

- 🌿 Real-time moisture detection via GPIO (pin 17)
- 📧 Sends 4 automated email reports per day at:
  - **07:00**
  - **10:00**
  - **13:00**
  - **16:00**
- 🛠️ Built with `gpiozero`, `schedule`, `smtplib`
- 💬 Console logs each water status change and email result

---

## 📁 Project Structure

```bash
📁 Project2_2025/
├── SoilSensor.py          # perform initial sensor test
├── send_email.py          # email sending test
├── SoilSensorEmail.py     # integrate sensor and email scripts
├── Physical Setup.jpg     # physical setup figure
└── README.md 
```

---

## 🛠 Hardware Requirements

- Raspberry Pi with Raspbian OS
- Digital moisture sensor (DOUT signal)
- GPIO pin connection: **Pin 17**
- Internet connection (for sending emails)

### 💡 Sensor Pinout

| Pin | Description  | Connects To       |
|-----|--------------|-------------------|
| VCC | Power        | Pi 5V             |
| GND | Ground       | Pi GND            |
| D0  | Digital Out  | Pi GPIO 17        |


### 🖼️ Wiring Diagram / Real Setup

<img src="https://github.com/Ataraxiaii/Project2_2025/blob/main/Physical%20Setup.jpg" alt="Hardware Setup" width="500"/>

> Above: Physical wiring of moisture sensor to Raspberry Pi GPIO 17

---

## 📧 Email Setup

Before running the script, edit the following fields in `SoilSensorEmail.py`:

```python
FROM_EMAIL = "youremail@qq.com"
FROM_PASSWORD = "your_app_password"  # APP password
TO_EMAIL = "receiver@qq.com"
```

---

## 🐍 How to Run the Script

### 🔧 1. Install Dependency

```bash
sudo apt update
pip install schedule gpiozero
```

### 📚 3. Clone the Repository
```bash
git clone https://github.com/Ataraxiaii/Project2_2025.git
```

### ▶️ 2. Run the Program
```bash
python SoilSensorEmail.py
```

---

## 💬 Contact

- 📧 Email: xuanru.guo.echo@gmail.com
- 📚 Course: Project Semester 3
- 🧑‍🎓 Author: Xuanru Guo
