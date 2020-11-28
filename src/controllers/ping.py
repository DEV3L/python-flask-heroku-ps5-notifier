from flask import Blueprint

ping = Blueprint('ping', __name__)


@ping.route('/', methods=['GET'])
@ping.route('/ping', methods=['GET'])
def hello_world():
    """
    Monitor endpoint
    ---
    tags:
      - ping
    responses:
      200:
        description: Hello, world!
    """
    return 'Hello, world!'


@ping.route('/raise', methods=['GET'])
def raise_exception():
    raise RuntimeError('500 status code')
