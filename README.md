# Beauty Salon

#### A mock beauty salon website using Python, Flask, WTForms, SQLAlchemy, and basic HTML/CSS. The theme and layout of this website is taken from another beauty salon site which is credited at the bottom of this README. Python was used for the entire website, using the Flask framework for website setup and navigation. The website has 4 pages: a homepage, an about page, a services page, and an appointments page. I have a base.html file that is used as the template for all pages, done using template inheritance with Flask's Jinja2 template engine. The template includes a navbar, carousel banner, business hours, salon location, contact info, and icons linking to the salon's different social media accounts. The appointments page has a form created using WTForms, this form creates appointments. To get the data to save to the database SQLAlchemy is used. Once the form is submitted a new page is created and the appointment info is rendered onto the new page. There are still changes to be made, including fixing the carousel and making the site mobile device-friendly.
---

## Run Locally

Clone the project

```bash {"id":"01HGF2PWJAAY0Z5PCWWDE3PWTS"}
  `git clone https://github.com/Rorschach3/beauty-Salon.git`
```

Go to the project directory

```bash {"id":"01HGF2PWJAAY0Z5PCWWE1AYTN4"}
  `cd beauty-Salon`
```

Install required packages and libraries

```bash {"id":"01HGF2PWJAAY0Z5PCWWGQ7Z62F"}
  `pip install -r requirements.txt`
```

Start the server

```bash {"id":"01HGF2PWJAAY0Z5PCWWJ50TH2H"}
 `python main.py`
```

## Pages


### Base Template 

#### Bootwatch shapes the theme and navbar of this website, creating a sleek design. The navbar features the business logo, "Home," "About," "Appointments," and a dropdown "Services" menu including "Hair," "Nails," "Hair Cut," and "Beauty Products." A carousel, though currently non-functional, will be a future feature. The footer includes contact details, hours of operation, and quick links to social media (Facebook, Instagram, Twitter).
--- 

### Home Page

#### Homepage is just a welcome page with a brief description of the business and a button to book an appointment and that takes you to the appointments page. After the button is a blockquote with a quote from a valued customer. More quotes can be added but for now there is just one.
![Webpage Example](https://i.ibb.co/Tkbfhj9/Scissors-Beauty-Salon.png)
---

### About Page

#### About page has some positive statements about the beauty salon and a collage of images related to beauty and hair.
![About Page](https://i.ibb.co/B6mt4rW/About-wep-page.png)
---

### Services Page

#### Services page has a dropdown menu in the navbar with options for "Hair", "Nails", "Hair Cut", and "Beauty Products". For the web content it displays three columns with each column having an image of the services offered and a description of each service.
![Services Page](https://i.ibb.co/6tvM4MR/Screenshot-2023-12-30-051819.png)
---

### Appointments Page

#### Appointments page has a form for setting up an appointment. You can choose between the different hair stylists and also the optional services that are offered. You Also choose the date and time of the appointment. There is a submit button that will send the information to the database. Once you submit the data it will take you to the success page.
![https://giphy.com/gifs/KjOR2r2hRe4SSdDpSD](https://media.giphy.com/media/KjOR2r2hRe4SSdDpSD/giphy.gif)
---

### Success Page

#### Success page renders the appointment data on a table, has a flash message saying "Appointment booked successfully", and a button to go back to the homepage.
![Success Page](https://i.ibb.co/99Tbjs4/Screenshot-2023-12-30-053313.png)
---

## Feedback

This website was created based on this website: (medialinkers.net/demo/envato/saloon/publish/index)[https://www.medialinkers.net/demo/envato/saloon/publish/index.html]

If you have any feedback, please reach out: daniel_fhernandez@yahoo.com

