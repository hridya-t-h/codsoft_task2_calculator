from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']
        
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                result = 'Error! Division by zero.'
            else:
                result = num1 / num2
        elif operation == 'power':
            result = num1 ** num2
        elif operation == 'mod':
            result = num1 % num2
        else:
            result = 'Invalid operation.'
    except ValueError:
        result = 'Invalid input. Please enter numbers only.'

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
