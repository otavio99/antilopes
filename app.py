# Third party libraries
from flask import Flask

# Internal import
from main import main

app = Flask(__name__)


app.register_blueprint(main.blueprint)

if __name__ == "__main__":
    app.run(debug=True, ssl_context="adhoc")
