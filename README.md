# Beauty Salon

## A mock beauty salon website using Python, Flask, WTForms, SQLAlchemy, and basic HTML/CSS. The theme and layout of this website are inspired by another beauty salon site, which is credited at the bottom of this README. Python was used for the entire website, utilizing the Flask framework for website setup and navigation. The website has four pages: a homepage, an about page, a services page, and an appointments page. A `base.html` file serves as the template for all pages, using template inheritance with Flask's Jinja2 template engine. The template includes a navbar, carousel banner, business hours, salon location, contact info, and icons linking to the salon's social media accounts. The appointments page features a form created using WTForms, allowing users to book appointments. The data is saved to the database using SQLAlchemy. Upon form submission, a new page renders the appointment details. Future improvements include fixing the carousel and making the site mobile-friendly

---

## Run Locally

Clone the project:

```sh
git clone https://github.com/Rorschach3/beauty-Salon.git
```

Navigate to the project directory:

```sh
cd beauty-Salon
```

Create a virtual environment:

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install required packages:

```sh
pip install -r requirements.txt
```

Start the server:

```sh
python main.py
```

---

## Pages

### Base Template

The website uses Bootswatch for styling, providing a sleek theme and a responsive navbar. The navbar features the business logo, "Home," "About," "Appointments," and a dropdown "Services" menu with options for "Hair," "Nails," "Hair Cut," and "Beauty Products." A carousel (currently non-functional) is planned for future implementation. The footer includes contact details, business hours, and quick links to social media platforms (Facebook, Instagram, Twitter).

---

### Home Page

The homepage features a welcome message with a brief business description and a button to book an appointment, directing users to the appointments page. Below this button, a blockquote displays a quote from a valued customer. Additional quotes may be added in the future.

![Webpage Example](https://i.ibb.co/96nrpZ4/screencapture-127-0-0-1-5000-2025-03-12-05-00-36.png)

---

### About Page

The about page contains positive statements about the beauty salon and a collage of images related to beauty and hair.

![About Page](https://i.ibb.co/9mQ1nXkX/screencapture-127-0-0-1-5000-about-2025-03-12-04-35-03.png)

---

### Services Page

The services page features a dropdown menu in the navbar with options for "Hair," "Nails," "Hair Cut," and "Beauty Products." The main content displays three columns, each containing an image representing a service and a corresponding description.

![Services Page](https://i.ibb.co/HpdfmWmv/screencapture-127-0-0-1-5000-services-2025-03-12-04-35-30.png)

---

### Appointments Page

The appointments page features a form for booking appointments. Users can choose from different hairstylists and optional services. They also select a date and time for their appointment. A submit button sends the information to the database, and upon submission, the user is redirected to the success page.

![Appointment Page](https://i.ibb.co/F4xnSjqq/screencapture-127-0-0-1-5000-appointments-2025-03-12-04-35-52.png)

---

### Success Page

The success page displays appointment details in a table, along with a flash message stating "Appointment booked successfully." It also includes a button to return to the homepage.

![Success Page](https://i.ibb.co/99Tbjs4/Screenshot-2023-12-30-053313.png)

---

## Feedback

This website was inspired by the following site: [medialinkers.net/demo/envato/saloon/publish/index](https://www.medialinkers.net/demo/envato/saloon/publish/index.html)

For feedback, please reach out: [daniel_fhernandez@yahoo.com](mailto:daniel_fhernandez@yahoo.com)
