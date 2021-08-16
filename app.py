from flask import Flask, render_template
import logging
from myapp.api import api




    
# Flask App
def create_app():
    app = Flask(__name__)
    app.debug = True
    app.register_blueprint(api)

    logging.basicConfig(filename='app.log',
                    level=logging.DEBUG)


    @app.route("/")
    def Website():
        return render_template("address.html")
    

    return app