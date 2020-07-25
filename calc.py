from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def welcome():
    return render_template('form.html')


@app.route('/calc', methods=['GET','POST'])
def calc():
    if request.method == 'POST':
        value1 = request.form.get("value1", type=int)
        value2 = request.form.get("value2", type=int)
        operation = request.form.get("operation")
    else:
        value1 = request.args.get("value1", type=int)
        value2 = request.args.get("value2", type=int)
        operation = request.args.get("operation")
    
    if(operation == '+'):
        result = value1 + value2
    elif(operation == '-'):
        result = value1 - value2
    elif(operation == '*'):
        result = value1 * value2
    elif(operation == '/'):
        result = value1 / value2
    else:
        result = 'INVALID CHOICE'
    entry = result
    return render_template('form.html', entry=entry)

if __name__ == '__main__':
    app.run(debug=True)

