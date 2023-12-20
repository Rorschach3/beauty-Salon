from flask import Flask, redirect, render_template, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import DateField, SelectField, StringField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config["SECRET_KEY"] = 'secret_key' 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    appointment_type = db.Column(db.String(20), nullable=False)
    stylist = db.Column(db.String(20), nullable=False)
    date = db.Column(db.Date)
    time = db.Column(db.String(10), nullable=False)


class AppointmentForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    appointment_type = SelectField('Appointment Type',
                                   choices=[('Hair Style', 'Hair Style'),
                                            ('Hair Cut', 'Hair Cut'),
                                            ('Color Change', 'Color Change')],
                                   validators=[DataRequired()])
    stylist = SelectField('Stylist',
                          choices=[('Ana', 'Ana'), ('Marie', 'Marie'),
                                   ('Suzie', 'Suzie')],
                          validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    time = SelectField('Time',
                       choices=[('10:00 AM', '10:00 AM'), ('10:30 AM', '10:30 AM'),
                                ('11:00 AM', '11:00 AM'), ('11:30 AM', '11:30 AM'),
                                ('12:00 PM', '12:00 PM'), ('12:30 PM', '12:30 PM'),
                                ('1:00 PM', '1:00 PM'), ('1:30 PM', '1:30 PM'),
                                ('2:00 PM', '2:00 PM'), ('2:30 PM', '2:30 PM'),
                                ('3:00 PM', '3:00 PM'), ('3:30 PM', '3:30 PM'),
                                ('4:00 PM', '4:00 PM'), ('4:30 PM', '4:30 PM'),
                                ('5:00 PM', '5:00 PM'), ('5:30 PM', '5:30 PM'),
                                ('6:00 PM', '6:00 PM'), ('6:30 PM', '6:30 PM'),
                                ('7:00 PM', '7:00 PM')],
                       validators=[DataRequired()])


def create_tables():
    with app.app_context():
        db.create_all()


        # Query and print the data from the test table
        # result = Appointment.query.all()
        # for record in result:
        #     print(
        #         f"ID: {record.id}",
        #         f"First Name: {record.first_name}",
        #         f"Last Name: {record.last_name}",
        #         f"Email: {record.email}",
        #         f"Phone: {record.phone}",
        #         f"Appointment Type: {record.appointment_type}",
        #         f"Stylist: {record.stylist}",
        #         f"Date: {record.date}",
        #         f"Time: {record.time}"
        #     )


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/appointments', methods=['GET', 'POST'])
def render_appointment_form():
    form = AppointmentForm()
    if form.validate_on_submit():

        appointment = Appointment(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            phone=form.phone.data,
            appointment_type=form.appointment_type.data,
            stylist=form.stylist.data,
            date=form.date.data,
            time=form.time.data
        )
        db.session.add(appointment)
        db.session.commit()

        flash('Appointment booked successfully!', 'success')
        return redirect(url_for('success', appointment_id=appointment.id))

    return render_template('appointments.html', form=form)


@app.route('/success/<int:appointment_id>')
def success(appointment_id):
    appointment = Appointment.query.get(appointment_id)
    if not appointment:
        return redirect(url_for('render_appointment_form'))

    return render_template('success.html', appointment=appointment)


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    create_tables()
    app.run(host='0.0.0.0', port=5000, debug=True)