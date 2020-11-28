from flask import Blueprint, request

from src.services.twilio_service import TwilioService

twilio = Blueprint('twilio', __name__)


@twilio.route('/twilio', methods=['GET'])
def twilio_message():
    """
    Send message endpoint
    ---
    tags:
      - twilio
    parameters:
        - in: query
          name: message
          type: string
          description: A message to send via text message.
    responses:
      200:
        description: Message sent successfully
    """
    message = request.args.get('message', 'Hello, world!')

    twilio_service = TwilioService()
    twilio_service.send_message(message)

    return 'Message sent successfully!'
