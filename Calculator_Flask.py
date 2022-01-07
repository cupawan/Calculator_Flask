from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])

def home_page():
    return render_template('index.html')


@app.route("/math",methods = ["GET","POST"])

def math_ops():
    if (request.method == 'POST'):
        operation = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if operation == 'add':
            r = num1+num2
            result = "The sum of {} and {} is {}.".format(num1,num2,r)
        if operation == 'subtract':
            r = num1-num2
            result = "The diffrence of {} and {} is {}.".format(num1,num2,r)
        if operation == 'multiply':
            r = num1*num2
            result = "The product of {} and {} is {}.".format(num1,num2,r)
        if operation == 'divide':
            r = num1/num2
            result = "The quotient when {} is divided by {} is {}.".format(num1,num2,r)
        return render_template('results.html',result = result)

if __name__ == "__main__":
    app.run()