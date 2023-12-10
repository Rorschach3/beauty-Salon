from flask_wtf import FlaskForm
from wtforms import DateField, SelectField, StringField
from wtforms.validators import DataRequired


class AppointmentForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    appointment_type = SelectField('Appointment Type',
                                   choices=[('1', 'Hair Style'),
                                            ('2', 'Hair Cut'),
                                            ('3', 'Color Change')],
                                   validators=[DataRequired()])
    stylist = SelectField('Stylist',
                          choices=[('1', 'Ana'), ('2', 'Marie'),
                                   ('3', 'Suzie')],
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