from flask import Flask, render_template, request


app = Flask(__name__)

students=[]
organizations=[]
@app.get('/')
def index():
    return render_template('index.html')
 
@app.get('/register')
def register():
    student = request.args.get("student")
    students.append(student)
    organization = request.args.get("organizations")
    organizations.append(organization)

    return render_template('register.html', students =students, organizations = organizations)