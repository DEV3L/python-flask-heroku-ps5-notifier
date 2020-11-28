from flask import Blueprint, jsonify
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint

swagger_url = '/swagger'
swagger_spec_url = '/swagger_spec'

swagger_spec = Blueprint('swagger_spec', __name__)

swagger_ui_blueprint = get_swaggerui_blueprint(
    swagger_url,
    swagger_spec_url,
    config={
        'app_name': 'PS5 Notifier'
    }
)


@swagger_spec.route(swagger_spec_url)
def spec():
    from app import app
    swag = swagger(app)
    swag['info']['version'] = '1.0'
    swag['info']['title'] = 'PS5 Notifier'
    swag['securityDefinitions'] = {'BasicAuth': {'type': 'basic'}}
    return jsonify(swag)
