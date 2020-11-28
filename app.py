import os

from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_script import Manager

load_dotenv()

from src.controllers.ping import ping
from src.controllers.twilio import twilio
from src.controllers.swagger import swagger_ui_blueprint, swagger_spec, swagger_url
from src.services.logging_service import LoggingService

logger = LoggingService('app')
logger.info('Python Flask Heroku PS5 Notifier Flask app starting up')

LOCAL_ENVIRONMENT = "local"
environment = os.getenv('ENVIRONMENT', LOCAL_ENVIRONMENT)

app = Flask(__name__)
app.register_blueprint(ping)
app.register_blueprint(twilio)

app.register_blueprint(swagger_spec)
app.register_blueprint(swagger_ui_blueprint, url_prefix=swagger_url)

flask_host = os.getenv('HOST', '0.0.0.0')
flask_port = os.getenv('PORT', 5000)
flask_debug = os.getenv('DEBUG', False)


@app.errorhandler(AssertionError)
def invalid_request(e):
    return jsonify({'message': str(e)}), 406


@app.errorhandler(500)
def handle_error(e):
    logger.exception(e)
    return jsonify({'message': str(e)}), 500


manager = Manager(app)

if __name__ == '__main__':
    manager.run()
