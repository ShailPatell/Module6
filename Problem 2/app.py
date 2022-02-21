from flask import Flask, render_template, request


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate')
def calculator(number=None):
    if len(request.args)==0:
        return render_template('calculate.html')
    number = request.args.get('number')
    try:
        if int(number)%2==0:
            type='even'
        elif int(number)%2!=0:
            type='odd'
    except:
        type='not an integer!'
    return render_template('calculate.html', number=number, type=type)
