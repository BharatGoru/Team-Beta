from flask import Flask, render_template, request, redirect, url_for, session


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'            #created a database which stores and registers our id and password 
db = SQLAlchemy(app)
app.secret_key = 'your_secret_key'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():                           # registeration logic
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            error = 'Username already exists. Please choose a different username.'
            return render_template('register.html', error=error)

        # Insert the new user into the database
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():                                        # registeration logic
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Retrieve the user from the database
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            # Successful login
            # Store the username in the session
            session['username'] = username

            return redirect(url_for('dashboard'))

        error = 'Invalid username or password.'
        return render_template('login.html', error=error)

    return render_template('login.html')



@app.route('/dashboard')    # created the logic for our dashboard
def dashboard():
    # Retrieve the username from the session
    username = session.get('username')

    return render_template('dashboard.html', username=username)

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    
    return interpretation

def create_bar_chart_data(scores):
    data = [{'label': 'Score', 'value': score} for score in scores]    #  Display evaluation in bar-chart format
    return data

def create_pie_chart_data(scores):
    data = [{'label': f'Score {i+1}', 'value': score} for i, score in enumerate(scores)]     #  Display evaluation in pie-chart format
    return data

@app.route('/result')
    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True)
