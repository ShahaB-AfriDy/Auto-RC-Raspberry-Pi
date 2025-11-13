---

# 🚗 Auto-RC-Raspberry-Pi

**Auto-RC-Raspberry-Pi** is an intelligent self-driving RC car project powered by **Raspberry Pi** and **machine learning**.
The goal of this project is to create an autonomous RC car that can **collect driving data, train a deep learning model, and navigate independently** without human control.

---

## 🧠 Project Overview

This project integrates **computer vision**, **deep learning**, and **hardware control** to achieve autonomous navigation for a small-scale RC car.
It demonstrates the end-to-end pipeline — from **data collection** and **visualization**, to **model training**, and finally **testing** on the real car.

---

## 🗂️ Directory Structure

```
Auto-RC-Raspberry-Pi/
│
├── Data Collection/          # Scripts to capture images & steering data from the RC car
│   ├── collect_data.py
│   └── utils.py
│
├── Data Visualisation/       # Tools for exploring and visualizing collected driving data
│   ├── visualize_data.py
│   └── plot_steering.py
│
├── Model Training/           # Deep learning scripts for training autonomous driving models
│   ├── train_model.py
│   ├── model_architecture.py
│   └── dataset_loader.py
│
├── Test AutoCar/             # Scripts to deploy and test the trained model on Raspberry Pi
│   ├── test_autocar.py
│   └── motor_controller.py
│
└── README.md
```

---

## ⚙️ Features

* 📷 **Real-time Data Collection** via Pi Camera
* 🧩 **Deep Learning Model** for steering prediction
* 📊 **Data Visualization** for preprocessing and analysis
* 🚗 **Autonomous Driving** tested on Raspberry Pi with RC car hardware
* 🔧 **Modular Structure** for easy experimentation and upgrades

---

## 🧩 Technologies Used

| Category      | Tools & Libraries                             |
| ------------- | --------------------------------------------- |
| Hardware      | Raspberry Pi, Pi Camera, RC Car, Motor Driver |
| Language      | Python 3                                      |
| ML Frameworks | TensorFlow / Keras                            |
| Data Handling | NumPy, OpenCV, Pandas                         |
| Visualization | Matplotlib, Seaborn                           |

---

## 🧪 How It Works

1. **Data Collection**

   * Drive the RC car manually to record images and steering angles.
   * Store the data in CSV format for training.

2. **Data Visualization**

   * Explore and analyze collected data to ensure balance and diversity.

3. **Model Training**

   * Use CNN-based deep learning model to predict steering angles from camera images.

4. **Deployment & Testing**

   * Upload the trained model to Raspberry Pi.
   * Run the **Test AutoCar** script to let the RC car drive autonomously.

---

## 🚀 Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ShahaB-AfriDy/Auto-RC-Raspberry-Pi.git
cd Auto-RC-Raspberry-Pi
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Connect Hardware

* Raspberry Pi (with GPIO pins)
* Pi Camera module
* Motor driver (L298N or similar)
* RC car chassis

### 4. Run Modules

```bash
# Step 1: Collect driving data
python Data\ Collection/collect_data.py

# Step 2: Train the model
python Model\ Training/train_model.py

# Step 3: Test on car
python Test\ AutoCar/test_autocar.py
```

---

## 📈 Future Enhancements

* Add lane detection using OpenCV
* Implement obstacle detection with ultrasonic sensors
* Upgrade to reinforcement learning
* Introduce mobile/web dashboard for remote monitoring

---

## 🤝 Contribution

Contributions, pull requests, and suggestions are welcome!
If you find a bug or want to improve the system, feel free to open an issue.

---

## 🧑‍💻 Author

** Shahab Afridi**
🔗 GitHub: [ShahaB-AfriDy](https://github.com/ShahaB-AfriDy)

---

## 📜 License

This project is open-source and available under the **MIT License**.

---
