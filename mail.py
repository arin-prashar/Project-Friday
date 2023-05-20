from __future__ import print_function
import base64
from email.message import EmailMessage
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly','https://www.googleapis.com/auth/gmail.send','https://www.googleapis.com/auth/gmail.compose','https://www.googleapis.com/auth/gmail.modify','https://www.googleapis.com/auth/gmail.labels']

frm='prashararin@gmail.com'
def gmail_create_draft(to,sub,msg):
    # use the token.json file to access the gmail api
    creds = None
    if os.path.exists('extra/token.json'):
        creds = Credentials.from_authorized_user_file('extra/token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            
            flow = InstalledAppFlow.from_client_secrets_file(
                'extra/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('extra/token.json', 'w') as token:
            token.write(creds.to_json())
    try:
        # create gmail api client
        service = build('gmail', 'v1', credentials=creds)

        message = EmailMessage()

        message.set_content(msg)

        message['To'] = to
        message['From'] = frm
        message['Subject'] = sub

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        create_message = {
            'message': {
                'raw': encoded_message
            }
        }
        # pylint: disable=E1101
        draft = service.users().drafts().create(userId="me",
                                                body=create_message).execute()

        print(F'Draft id: {draft["id"]}\nDraft message: {draft["message"]}')

    except HttpError as error:
        print(F'An error occurred: {error}')
        draft = None

    return draft