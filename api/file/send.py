import resend

resend.api_key = "re_9PkoGJau_PSgVmtuWtU2cM6pVK2oSv8ct"

def send(data):
    try:
        email = resend.Emails.send({
            "from": "KhetMitra26@gmail.com",
            "to": data["to"],
            "subject": "KhetMitra",
            "html": data["text"]
        })
        return {"status": "mail sent"}
    except Exception as e:
        print(e)
        return {"status": "mail not sent"}
