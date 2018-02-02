from flask import *
from Database import *

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"

engine = create_engine('sqlite:///database.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()

# Set "homepage" to index.html
@app.route('/')
def home():
    return render_template('Home.html')

# Save e-mail to database and send to success page
@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        submitted_email = request.form['email']
        # Check that email does not already exist (not a great query, but works)
        if not session.query(Emails).filter_by(email= submitted_email).count():
            reg = Emails(email=submitted_email, name=request.form['fullName'])
            session.add(reg)
            session.commit()
            return render_template('Home.html')
    return render_template('Home.html')

@app.route('/merch')
def merch():
    return render_template('Merch.html')

if __name__ == '__main__':
    app.run(debug=True)