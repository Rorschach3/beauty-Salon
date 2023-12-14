from flask import Flask, redirect, render_template, url_for, request, flash
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from appointments import AppointmentForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/appointments.db'
db = SQLAlchemy(app)


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    appointment_type = db.Column(db.String(20), nullable=False)
    stylist = db.Column(db.String(20), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.String(10), nullable=False)


def create_tables():
    with app.app_context():
        db.create_all()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/appointments', methods=['GET', 'POST'])
def render_appointment_form():
    form = AppointmentForm()

    if request.method == 'POST' and form.validate_on_submit():
        date_str = form.date.data
        formatted_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        
        appointment = Appointment(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            phone=form.phone.data,
            appointment_type=form.appointment_type.data,
            stylist=form.stylist.data,
            date=formatted_date,
            time=form.time.data)

        db.session.add(appointment)
        db.session.commit()

        flash('Appointment booked successfully!', 'success')
        return redirect(url_for('success', appointment_id=appointment.id))
    else:
        flash('Appointment not booked. Please try again.', 'danger')

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
