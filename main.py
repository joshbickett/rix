from flask import Flask
from comm.gmail import get_test_service, get_service, get
from comm.calendarrequest import CalendarRequest
import nlp.gpt
import time

app = Flask(__name__)

@app.route("/")
def home():
    # PRODUCTION
    mail_service = get_service()
    # TESTING
    # mail_service = get_test_service()
    print(f'mail_service: {mail_service}')
    while True:
        time.sleep(3)
        mail = get(mail_service)
        if mail:
            print("______________________________ email ___________________________________")
            message = mail.messages[-1]
            message = nlp.gpt.filter_signature(message)
            print(f'message: {message}')

if __name__ == '__main__':
    app.run(debug=True)
