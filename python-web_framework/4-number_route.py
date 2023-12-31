from flask import Flask, request, abort
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
@app.route('/number/<n>', strict_slashes=False)
def number(n):
    """ Displays “n is a number” only if n is an integer """
    try:
        n = int(n)
        return f"{n} is a number"
    except ValueError:
        abort(404)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)