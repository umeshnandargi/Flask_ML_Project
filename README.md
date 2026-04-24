# Student Depression Classifier

A Flask web application that uses a deep learning model to identify patterns associated with depression in students, based on lifestyle and academic inputs.

> **Disclaimer:** This tool is intended for **educational and awareness purposes only**. It is **not a medical diagnosis** and does not replace professional psychological or medical advice. If you are experiencing mental health difficulties, please reach out to a qualified professional.

---

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the App](#running-the-app)
- [Running with Docker](#running-with-docker)
- [Input Fields](#input-fields)
- [Tech Stack](#tech-stack)
- [Contributing](#contributing)

---

## Overview

This project is a full-stack web application built with **Flask** that takes student lifestyle data as input and runs it through a trained deep learning model to estimate the likelihood of depression-related patterns. The goal is to raise awareness and encourage early help-seeking behaviour among students.

---

## Prerequisites

- Python 3.8+
- pip
- (Optional) Docker

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/umeshnandargi/Flask_ML_Project.git
cd Flask_ML_Project
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## Running the App

```bash
python main.py
```

Then open your browser and navigate to:

```
http://localhost:<port from config>
```

---

## Running with Docker

1. **Build the image**

```bash
docker build -t student-depression-classifier .
```

2. **Run the container**

```bash
docker run -p HOST_PORT(from config):CONTAINER_PORT(from Dockerfile) student-depression-classifier
```

Then visit `http://localhost:<port from config>` in your browser.

---

## Input Fields

The classifier collects the following student data:

| Field | Description |
|---|---|
| Age | Student age (18–24) |
| Gender | Male / Female |
| Department | Science, Engineering, Medical, Arts, or Business |
| CGPA | Grade point average (0.0 – 4.0) |
| Sleep Duration | Average hours of sleep per night |
| Study Hours | Average hours spent studying per day |
| Social Media Hours | Average hours spent on social media per day |
| Physical Activity | Average minutes of physical activity per week |
| Stress Level | Self-reported stress level (scale 0–10) |

---

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS (Jinja2 templates)
- **ML/DL:** Deep learning model using pytorch (see `ml_models/`)
- **Containerisation:** Docker

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

*Built for educational purposes. Mental health matters — if you or someone you know is struggling, please seek professional support.*
