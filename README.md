---
runme:
  id: 01HGF2PWJB0EQGKH1JHVNS9EG6
  version: v2.0
---

# Beauty Salon

A brief description of what this project does and who it's for

## Run Locally

Clone the project

```bash {"id":"01HGF2PWJAAY0Z5PCWWDE3PWTS"}
  git clone https://github.com/Rorschach3/beauty-Salon.git

```

Go to the project directory

```bash {"id":"01HGF2PWJAAY0Z5PCWWE1AYTN4"}
  cd beauty-Salon

```

```bash {"id":"01HGF2PWJAAY0Z5PCWWGQ7Z62F"}
  pip install -r requirements.txt

```

Start the server

```bash {"id":"01HGF2PWJAAY0Z5PCWWJ50TH2H"}
 python main.py

```

## Pages

> Website Base Template

    - Bootwatch was used to create the navbar and overall theme of the website. Bootswatch is a  and  The business logo is the first element in the navbar followed by "Home" which takes you to the landing page. Followed by "About", "Appointments", "Services" and Services is a dropdown for more options. Those options are "Hair", "Nails", "Hair Cut", and "Beauty Products". Followed by a non-working search bar with submit button.
    
    - A courosel has been added to the base template, although it currently does not switch images, it will be a feature in the future. 
    
    - The footer is part of the base template with three main componenets. Contact information with the address, business email, and business phone number. The second component is the Hours of Operation which is just a Monday through Sunday with the hours of operation. The third component is a quick links to the same pages in the navbar, social media section with icons for Facebook, Instagram, and Twitter.

> Homepage

    - Homepage is just a welcome page with a brief description of the business and a button to book an appointment and that takes you to the appointments page. After the button is a blockquote with a quote from a valued customer. More quotes can be added but for now there is just one.

> About Page

    - About page has some positive statements about the beauty salon and a collage of images related to beauty and hair.

> Services Page

    - Services page has a dropdown menu in the navbar with options for "Hair", "Nails", "Hair Cut", and "Beauty Products". For the web content it displays three columns with each column having an image of the services offered and a description of each service.

> Appointments Page

    - Appointments page has a form for setting up an appointment. You can choose between the different hair stylists and also the optional services that are offered. You Also choose the date and time of the appointment. There is a submit button that will send the information to the database. Once you submit the data it will take you to the success page. This was created using Flask wtforms for the forms and flask-SQLAlchemy for the database.

> Success Page

    - Success page renders the appointment data on a table has a flash message saying "Appointment booked successfully" and text "Your appointment has been scheduled" and a button to go back to the homepage.

## Feedback

This website was created based on this website: (medialinkers.net/demo/envato/saloon/publish/index)[https://www.medialinkers.net/demo/envato/saloon/publish/index.html]

If you have any feedback, please reach out: daniel_fhernandez@yahoo.com
