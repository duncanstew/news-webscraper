import pickle
import os
from pprint import pprint as pp
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from datetime import date
from scrape import parseFile


'''
Variables to adjust for personal calendar:
    - GMT_OFF : TZ is based on UTC and must offset this value for calendar to insert at proper time. 
    Ex: Chicago is 5 hours behind UTC so my offset is -05:00
    - startTime : Identify when you want your event to START in calendar. I read news mornings from 8:30-9:00 so ST: 08:30:00
    - endTime : Identify when you want your event to END in calendar. I don't always read for 30 minutes but I allocate that 
    time in my schedule anyways. Ex: 9:00:00
    - COLOR : 
'''
CLIENT_SECRET_FILE = 'client_secret.json'
API_SERVICE_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']
GMT_OFF = '-05:00'
START_TIME = '08:30:00'
END_TIME = '09:00:00'
COLOR = 5

# create an authorized token file, depends on how you use the application
def main():
    cred = None
    if os.path.exists('token.pickle'):
        with open('token.pickle','rb') as token:
            cred = pickle.load(token)

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())

        else:
            ''' Server strategy insturcts the user to open the authorization URL in their browser and will attempt to 
                automatically open the URL for them. It will start a local web server to listen for the authorization
                response. Once authorization is complete the authorization server will redirect the uers's browser to the local web server.
                The web server will get the authorization code from the response and shutdown. The code is then exchanged for a token.

            '''
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            cred = flow.run_local_server()

        with open('token.pickle','wb') as token:
            pickle.dump(cred, token)

    '''
    Create service event and capture any errors. In aws, crontab has option of 'mailTo' which captures any error passed from this file. 
    Will email and notify that the upload did not work, and event not created.
    '''
    try:
        service = build(API_SERVICE_NAME, API_VERSION, credentials=cred)
        today = date.today()
        day = today.strftime("%Y/%m/%d").replace('/','-')
        text = parseFile('output.json')
        fulltext = ' \n'.join(text)
        event = {
            'summary': 'Breakfast + News',
            'description': fulltext,
            'start': {
                'dateTime': '%sT%s%s' % (day,START_TIME,GMT_OFF),
                'timeZone': 'America/Chicago',
                },
            'end': {
                'dateTime': '%sT%s%s' % (day,END_TIME,GMT_OFF),
                'timeZone': 'America/Chicago',
                },
            'colorId': COLOR,
        }

        print('Service created successfully')
        event = service.events().insert(calendarId='primary',body=event).execute()
        print(event)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()