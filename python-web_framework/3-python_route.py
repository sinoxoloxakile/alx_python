from flask import Flask, request
app = Flask(__name__)
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Displays “Hello HBNB!” """
    return "Hello HBNB!"
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Displays “HBNB” """
    return "HBNB"
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ Displays “C ”, followed by the value of the text variable (replace underscore _ symbols with a space ) """
    text = text.replace("_", " ")
    return f"C {text}"
@app.route('/python/<text>', strict_slashes=False, defaults={'text': 'is cool'})
def python_text(text):
    """ Displays “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space ) """
    text = text.replace("_", " ")
    return f"Python {text}"
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)