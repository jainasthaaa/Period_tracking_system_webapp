from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import pyodbc

db = SQLAlchemy()
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mssql+pyodbc://DESKTOP-FPQKSBS/user_data?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


# User Data Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    period_start = db.Column(db.Date, nullable=False)
    period_end = db.Column(db.Date, nullable=False)
    cycle_length = db.Column(db.Integer, nullable=False)
    last_period_date = db.Column(db.Date, nullable=False)

    def __init__(self, name, email, period_start, period_end, cycle_length, last_period_date):
        self.name = name
        self.email = email
        self.period_start = period_start
        self.period_end = period_end
        self.cycle_length = cycle_length
        self.last_period_date = last_period_date

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'period_start': str(self.period_start),
            'period_end': str(self.period_end),
            'cycle_length': self.cycle_length,
            'last_period_date': str(self.last_period_date)
        }

with app.app_context():
    db.create_all()

# Routes
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/update_account', methods=['POST'])
def update_account():
    name = request.form['name']
    email = request.form['email']
    period_start = request.form['period_start']
    period_end = request.form['period_end']
    cycle_length = request.form['cycle_length']
    last_period_date = request.form['last_period_date']

    user = User.query.filter_by(email=email).first()
    if user:
        user.name = name
        user.period_start = period_start
        user.period_end = period_end
        user.cycle_length = cycle_length
        user.last_period_date = last_period_date
    else:
        new_user = User(name, email, period_start, period_end, cycle_length, last_period_date)
        db.session.add(new_user)

    db.session.commit()
    return redirect(url_for('account'))

if __name__ == '__main__':
    app.run(debug=True)
