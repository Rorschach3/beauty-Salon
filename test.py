from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
print(app.config['SQLALCHEMY_DATABASE_URI'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class TestTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    appointment_type = db.Column(db.String(20))
    stylist = db.Column(db.String(20))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    time = db.Column(db.String(10), nullable=False)


def create_tables():
    with app.app_context():
        db.create_all()


def test_database_operations():
    with app.app_context():
        # Create tables if they don't exist
        create_tables()

        # Add a record to the test table
        test_record = TestTable(
            first_name='Gabe',
            last_name='Lahkman',
            email='gabe@example.com',
            phone='714-574-2269',
            appointment_type='Haircut',
            stylist='John Doe',
            date=datetime.now().date(),
            time='10:00 AM'
        )
        db.session.add(test_record)
        try:
            db.session.commit()
        except Exception as e:
            print(f"Error committing to the database: {e}")

        # Query and print the data from the test table
        result = TestTable.query.all()
        for record in result:
            print(
                f"ID: {record.id}",
                f"First Name: {record.first_name}",
                f"Last Name: {record.last_name}",
                f"Email: {record.email}",
                f"Phone: {record.phone}",
                f"Appointment Type: {record.appointment_type}",
                f"Stylist: {record.stylist}",
                f"Date: {record.date}",
                f"Time: {record.time}"
            )

        print(result)

if __name__ == '__main__':
    create_tables()
    test_database_operations()
    app.run(host='0.0.0.0', port=5000)