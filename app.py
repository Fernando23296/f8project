import random
from flask import Flask, request
from pymessenger.bot import Bot

app = Flask(__name__)
ACCESS_TOKEN = 'EAAFFZC3XDrDQBAAKoYdzNn7ZAbddS7T4ZCeRrNlNLP7vFmRniHkU7ikYy01sqRAMRQZABpRm7piQUNs24ifMXbjug1XZB9BYn8ZBpW0T80bsY8BoSVyNzRbbeiZBwZBCVg6Xyt7DkHtjpkEaZCUQLnZAu6ci3BLBM5kklUPwT3UsbuMAZDZD'
VERIFY_TOKEN = 'f8hackathon2019'
bot = Bot(ACCESS_TOKEN)


@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook.""" 
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    
    else:
    
       output = request.get_json()
       for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('message'):
                recipient_id = message['sender']['id']
                if message['message'].get('text'):
                    response_sent_text = get_message()
                    send_message(recipient_id, response_sent_text)
                if message['message'].get('attachments'):
                    response_sent_nontext = get_message()
                    send_message(recipient_id, response_sent_nontext)
    return "Message Processed"


def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'



def get_message():
    sample_responses = ["You are stunning!", "We're proud of you.", "Keep on being you!", "We're greatful to know you :)"]
    return random.choice(sample_responses)



def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return "success"

if __name__ == "__main__":
    app.run(debug=True)