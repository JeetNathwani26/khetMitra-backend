from google_auth_oauthlib.flow import InstalledAppFlow # type: ignore

SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

flow = InstalledAppFlow.from_client_secrets_file(
    "credentials.json", SCOPES
)

creds = flow.run_local_server(port=5000)

print("REFRESH TOKEN:", creds.refresh_token)
