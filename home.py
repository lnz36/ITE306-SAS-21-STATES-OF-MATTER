Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from flask import Flask 
... 
... app = flask(__name__)
... 
... @app.route(""/)
... def home();
...     return "HELLO <h1>HELLO<h1>"
... 
... if __name__ == "__main__":
