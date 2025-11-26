from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World :)'

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"

@app.route('/f')
@app.route('/f/<celsius>')
def convert_celsius_to_fahrenheit(celsius=0.0):
    """Convert celsius to fahrenheit"""
    celsius = float(celsius)
    fahrenheit = celsius * 9.0 / 5 + 32
    return f"Result: {fahrenheit:.2f} F"


if __name__ == '__main__':
    app.run()