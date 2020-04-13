from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://avwqhsxrcmjzjq:f9685dd171367f481b02315a321835fa2057a1db9b7db58f3cf4bc8592665987@ec2-3-91-112-166.compute-1.amazonaws.com:5432/dd1eri7mlervvs'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(200))
    age = db.Column(db.Integer)
    role = db.Column(db.String(200))
    whichtea = db.Column(db.String(200))
    userrecommend = db.Column(db.String(200))
    comment = db.Column(db.Text())

    def __init__(self, name, email, age, role, whichtea, userrecommend, comment):
        self.name = name
        self.email = email
        self.age = age
        self.role = role
        self.whichtea = whichtea
        self.userrecommend = userrecommend
        self.comment = comment
        

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        role = request.form['role']
        whichtea = request.form['whichtea']
        userrecommend = request.form['userrecommend']
        comment = request.form['comment']

        if db.session.query(survey).filter(survey.name == name).count() == 0:
            data = survey(name, email, age, role, whichtea, userrecommend, comment)
            db.session.add(data)
            db.session.commit()
            return render_template('success.html')
        else:    
            return render_template('index.html', message = 'You have already submitted feedback to this survey.')



if __name__ == "__main__":
    app.run(debug=True)
