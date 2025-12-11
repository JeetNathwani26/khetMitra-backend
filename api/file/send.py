import requests

url = "https://api.emailjs.com/api/v1.0/email/send"

payload = {
    "service_id": "service_vizjesg",
    "template_id": "template_vidl8lb",
    "user_id": "HgPoef-8Ux5AFV4u5_4lu",
    "template_params": {
        "name": "Jeet",
        "message_html": """
            <div style="padding:20px; background:#f7f7f7;">
                <h2 style="color:#ff6600;">Hello Jeet!</h2>
                <p>This is an <b>HTML formatted</b> message sent from Python.</p>
                <p style="margin-top:10px;">✔ Supports bold<br>✔ Supports color<br>✔ Supports inline CSS</p>
            </div>
        """
    }
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.status_code)
print(response.text)
