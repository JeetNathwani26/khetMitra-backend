import resend
from flask import jsonify

# Your new API key
resend.api_key = "re_PvGKNSkr_2VvL3vsQnEGu7ajZQ61zQPJr"

def send(data):
    receiver_email = data["to"]
    message_html = data["text"]    # full HTML content

    try:
        email = resend.Emails.send({
            "from": "onboarding@resend.dev",  # sandbox sender
            "to": [receiver_email],                        # MUST be list
            "subject": "KhetMitra",
            "html": message_html
        })

        print("Resend Response:", email)    # Should contain an email ID
        return {"status": "mail sent"}

    except Exception as e:
        print("Email Error:", e)
        return {"status": "mail not sent"}
