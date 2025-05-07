<!-- Project Title -->

<p align="center">
  <img src="https://i.ibb.co/96nrpZ4/screencapture-127-0-0-1-5000-2025-03-12-05-00-36.png" alt="Beauty Salon Homepage" width="600"/>
</p>

# Beauty Salon

A mock beauty-salon website built with **Python**, **Flask**, **WTForms**, **SQLAlchemy**, and **HTML/CSS**. This project showcases a four-page site—Home, About, Services, Appointments—using Flask’s Jinja2 templating and Bootstrap for styling.

---

## Table of Contents

1. [Features](#features)
2. [Tech Stack](#tech-stack)
3. [Screenshots](#screenshots)
4. [Getting Started](#getting-started)
5. [Site Structure](#site-structure)
6. [Future Improvements](#future-improvements)
7. [Credits](#credits)

---

## Features

* **Responsive Layout** with Bootstrap/Bootswatch
* **Navbar + Footer** via a shared `base.html` template
* **Carousel Banner** placeholder for hero images
* **Business Info**: hours, location, social links
* **WTForms-powered Appointment Form**
* **SQLAlchemy** models for persisting bookings
* **Flash Messages** for user feedback

---

## Tech Stack

| Component    | Library / Framework    |
| ------------ | ---------------------- |
| Backend      | Flask                  |
| Forms        | Flask-WTForms          |
| ORM          | SQLAlchemy             |
| Templates    | Jinja2 (Flask)         |
| Frontend CSS | Bootstrap / Bootswatch |
| Language     | Python 3.x             |
| Database     | SQLite (default)       |

---

## Screenshots

### Home

Welcome banner, quote, “Book Appointment” button

<p align="center">
  <img src="https://i.ibb.co/96nrpZ4/screencapture-127-0-0-1-5000-2025-03-12-05-00-36.png" alt="Home Page" width="600"/>
</p>

### About

Salon description + image collage

<p align="center">
  <img src="https://i.ibb.co/9mQ1nXkX/screencapture-127-0-0-1-5000-about-2025-03-12-04-35-03.png" alt="About Page" width="600"/>
</p>

### Services

Grid of hair, nails, haircuts, beauty products

<p align="center">
  <img src="https://i.ibb.co/HpdfmWmv/screencapture-127-0-0-1-5000-services-2025-03-12-04-35-30.png" alt="Services Page" width="600"/>
</p>

### Appointments

Booking form with stylist, services, date/time

<p align="center">
  <img src="https://i.ibb.co/F4xnSjqq/screencapture-127-0-0-1-5000-appointments-2025-03-12-04-35-52.png" alt="Appointments Page" width="600"/>
</p>

### Success

Confirmation table + flash message

<p align="center">
  <img src="https://i.ibb.co/99Tbjs4/Screenshot-2023-12-30-053313.png" alt="Success Page" width="600"/>
</p>

---

## Getting Started

1. **Clone repository**

   ```bash
   git clone https://github.com/Rorschach3/beauty-Salon.git
   cd beauty-Salon
   ```

2. **Create and activate virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**

   ```bash
   python main.py
   ```

5. **Visit in browser**
   Open [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Site Structure

```
beauty-Salon/
├─ templates/
│  ├─ base.html          # common navbar, footer
│  ├─ home.html
│  ├─ about.html
│  ├─ services.html
│  ├─ appointments.html
│  └─ success.html
├─ static/
│  ├─ css/               # custom styles
│  └─ images/            # banners, icons
├─ main.py               # Flask app & route definitions
├─ models.py             # SQLAlchemy models
├─ forms.py              # WTForms definitions
└─ requirements.txt
```

---

## Future Improvements

* Activate and fix the **carousel**
* Enhance **mobile responsiveness**
* Add **user authentication** for stylists
* Implement **appointment reminders** via email/SMS

---

## Credits

* Site design inspired by [medialinkers Saloon Demo](https://www.medialinkers.net/demo/envato/saloon/publish/index.html)
* Developed by **Daniel Hernandez** ([daniel\_fhernandez@yahoo.com](mailto:daniel_fhernandez@yahoo.com))
