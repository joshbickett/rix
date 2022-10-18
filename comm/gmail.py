# from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from email.mime.text import MIMEText
from email_reply_parser import EmailReplyParser
import base64
from comm.mail import Mail

def create_reply(mail, reply):
    """Create a message for an email.

      Args:
        sender: Email address of the sender.
        to: Email address of the receiver.
        subject: The subject of the email message.
        message_text: The text of the email message.

      Returns:
        An object containing a base64url encoded email object.
      """

    message = MIMEText(reply)
    message['To'] = mail.sender
    message['Subject'] = mail.subject
    if mail.cc:
        message['Cc'] = mail.cc
        print("-- - - cc - - -")
        print(mail.cc)
        print("-- - - cc - - -")
    else:
        print("Noone CCed")
    message['From'] = 'Your assistant <assistant@tryrix.com>'
    message['References'] = mail.references
    message['In-Reply-To'] = mail.in_reply_to
    encoded_message = base64.urlsafe_b64encode(message.as_bytes())
    decoded_message = encoded_message.decode()
    return {'raw': decoded_message, 'threadId':mail.thread_id}

def add_thread(mail, reply):
    return reply + "\n\nOn " + mail.date + " " + mail.sender + " wrote:\n\n" + mail.threads[-1]

def get(service):
    threads = service.users().threads().list(userId="me", labelIds="INBOX").execute().get('threads', [])

    if len(threads)>0:
        print("You have mail")
        thr = threads[0]

        thread = service.users().threads().get(userId="me", id=thr['id']).execute()


        thread_id = thread['id']

        conversation = ''
        subject = ''
        sender = ''
        cc = ''
        references = ''
        in_reply_to =''
        date = ''
        messages = []
        threads =[]

        last_message = thread['messages'][-1]

        for header in last_message['payload']['headers']:
            if header['name'] == 'References':
                references = header['value']
        for header in last_message['payload']['headers']:
            if header['name'] == 'Date':
                date = header['value']
            if header['name'] == 'Message-ID':
                in_reply_to = header['value']
                if not references:
                    references = header['value']
                else:
                    references = references + " " + header['value']
            # sometimes the header comes across as so
            if header['name'] == 'Message-Id':
                in_reply_to = header['value']
                if not references:
                    references = header['value']
                else:
                    references = references + " " + header['value']
            if header['name'] == 'From':
                sender = header['value']
                # print(header['value'])
            if header['name'] == 'Cc':
                cc = header['value']
                # print(header['value'])
            if header['name'] == 'CC':
                cc = header['value']
                # print(header['value'])
            if header['name'] == 'Subject':
                subject = header['value']
                # print(header['value'])
        for message in thread['messages']:
            for header in message['payload']['headers']:
                if header['name'] == 'From':
                    sender_arr = header['value'].split('<')
                    sender_name = sender_arr[0]
                    sender_says = ">" + sender_name + "says:\n"
                    conversation += sender_says

            if message['payload']['mimeType']=='multipart/alternative':
                for part in message['payload']['parts']:
                    if part['mimeType']=='text/plain':
                        msg = base64.urlsafe_b64decode(part['body']['data']).decode("utf-8")
                        threads.append(msg)
                        parsed_message = EmailReplyParser.parse_reply(msg)
                        messages.append(parsed_message)
                        conversation += parsed_message +"\n"
            elif message['payload']['mimeType']=='text/plain':
                msg = base64.urlsafe_b64decode(message['payload']['body']['data']).decode("utf-8")
                threads.append(msg)
                parsed_message = EmailReplyParser.parse_reply(msg)
                messages.append(parsed_message)
                conversation += parsed_message + "\n"
            elif message['payload']['mimeType'] == 'multipart/mixed':
                for part in message['payload']['parts']:
                    if part['mimeType']=='multipart/alternative':
                        for p in part['parts']:
                            if p['mimeType'] == 'text/calendar':
                                # This archives any calendar messages
                                print("Received calendar email - ARCHIVED")
                                archive(service, thread_id)
                                return
            else:
                print('Unknown payload type')
        mail = Mail(thread_id, date, references, in_reply_to, sender, cc, subject, messages, threads, conversation)
        return mail
    # else:
    #     print("Mailbox empty")

def archive(service,thread_id):
    service.users().threads().modify(userId='me',id=thread_id,body={'removeLabelIds': ['INBOX']}).execute()

def send(service, message):
    """Send an email message.

    Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    message: Message to be sent.

    Returns:
    Sent Message.
    """
    message = (service.users().messages().send(userId='me', body=message)
               .execute())


def get_service():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    SCOPES = ['https://mail.google.com/']
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('tokens/agent/mail/token.json'):
        creds = Credentials.from_authorized_user_file('tokens/agent/mail/token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'tokens/agent/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('tokens/agent/mail/token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    return service

def get_test_service():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    SCOPES = ['https://mail.google.com/']
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('tokens/agent/test/mail/token.json'):
        creds = Credentials.from_authorized_user_file('tokens/agent/test/mail/token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'tokens/agent/test/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('tokens/agent/test/mail/token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    return service









