from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()

class DB(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(20))
    comment = db.Column(db.String(100))

@app.route('/')
@app.route('/index.html')
def index():
    comments = DB.query.all()
    return render_template('index.html', heading='Importance of Programming',comments=comments)

@app.route('/javascript.html')
def javascript():
   return render_template('languages/javascript.html', heading='JAVASCRIPT')

@app.route('/python.html')
def python():
   return render_template('languages/python.html', heading='PYTHON')

@app.route('/html.html')
def html():
   return render_template('languages/html.html', heading='HTML')

@app.route('/css.html')
def css():
   return render_template('languages/css.html', heading='CSS')

@app.route('/sql.html')
def sql():
   return render_template('languages/sql.html', heading='SQL')

@app.route("/comment",methods=["GET","POST"])
def comment():
    comment = request.form.get('_comment')
    name = request.form.get('_name')
    comment = DB(name=name,comment=comment)
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
