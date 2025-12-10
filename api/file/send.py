import resend

resend.api_key = "re_9PkoGJau_PSgVmtuWtU2cM6pVK2oSv8ct"

def send(data):
    try:
        email = resend.Emails.send({
            "from": "KhetMitra <onboarding@resend.dev>",
            "to": [data["to"]],                     # MUST be list
            "subject": "KhetMitra",
            "html": data["text"]
        })
        return {"status": "mail sent", "id": email["id"]}

    except Exception as e:
        print("Email Error:", e)
        return {"status": "mail not sent"}
