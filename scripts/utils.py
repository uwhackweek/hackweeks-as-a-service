def read_google_sheets(credentials_file=None, sheet_id=None, sheet_range=None):
    """

    code to read data directly from google sheets

    using instructions from https://medium.com/analytics-vidhya/how-to-read-and-write-data-to-google-spreadsheet-using-python-ebf54d51a72c

    Parameters
    ----------

        credentials_file : string
            The filename of the credentials file acquired from the Google API
        sheet_id : string
            The object identifier of the spreadsheet you want to read, taken from the link generated when sharing a file
        range : string
            The spreadsheet range

    Returns 
    -------

        df: data frame

    """

    import pandas as pd
    from googleapiclient.discovery import build
    from google_auth_oauthlib.flow import InstalledAppFlow,Flow
    from google.auth.transport.requests import Request
    import os
    import pickle

    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    # here enter the id of your google sheet
    SAMPLE_SPREADSHEET_ID_input = sheet_id
    SAMPLE_RANGE_NAME = sheet_range

    def main():
        global values_input, service
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    credentials_file, SCOPES) # here enter the name of your downloaded JSON file
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result_input = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID_input,
                                    range=SAMPLE_RANGE_NAME).execute()
        values_input = result_input.get('values', [])

        if not values_input and not values_expansion:
            print('No data found.')

    main()

    df=pd.DataFrame(values_input[1:], columns=values_input[0])
    return df