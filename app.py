# Flask Calculator Application



from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to Flask Calculator</h1><p>Use /add, /subtract, /multiply, or /divide in the URL.</p>"

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    result = a + b
    return render_template('result.html', operation="Addition", a=a, b=b, result=result)

@app.route('/subtract/<int:a>/<int:b>')
def subtract(a, b):
    result = a - b
    return render_template('result.html', operation="Subtraction", a=a, b=b, result=result)

@app.route('/multiply/<int:a>/<int:b>')
def multiply(a, b):
    result = a * b
    return render_template('result.html', operation="Multiplication", a=a, b=b, result=result)

@app.route('/divide/<int:a>/<int:b>')
def divide(a, b):
    if b == 0:
        return render_template('result.html', operation="Division", a=a, b=b, result="Error: Cannot divide by zero")
    result = a / b
    return render_template('result.html', operation="Division", a=a, b=b, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
