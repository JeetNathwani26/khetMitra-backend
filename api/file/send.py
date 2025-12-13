import os
import base64
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

def send(data):
    receiver_email = data["to"]
    message_html = data["text"]

    # Check env variables
    if not os.getenv("REFRESH_TOKEN"):
        raise Exception("REFRESH_TOKEN not found in .env")

    creds = Credentials(
        token=None,
        refresh_token=os.getenv("REFRESH_TOKEN"),
        token_uri="https://oauth2.googleapis.com/token",
        client_id=os.getenv("GOOGLE_CLIENT_ID"),
        client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    )

    service = build("gmail", "v1", credentials=creds)

    message = MIMEText(message_html, "html")
    message["To"] = receiver_email
    message["From"] = os.getenv("EMAIL_FROM")
    message["Subject"] = "KhetMitra"

    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    try:
        service.users().messages().send(
            userId="me",
            body={"raw": raw_message}
        ).execute()
        print("✅ Message sent successfully")
        return {"status": "mail sent"}
    except Exception as e:
        print("❌ Error sending email:", e)
        return {"status": "mail not sent", "error": str(e)}

