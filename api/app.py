from flask import Flask, request,jsonify
from flask_cors import CORS  # type: ignore
from api.file.send import send
from api.file.adminclass import Admin
from api.file.user import user
import os

admin=Admin("user")
user1=user("user")
proposal=user("proposal")
report=user("report")

app = Flask(__name__)
CORS(app, supports_credentials=True, origins=["http://localhost:5173"])  # allow requests from React (localhost:5173)


UPLOAD_FOLDER = '../khetmitra-manager/public/document'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/verify", methods=["POST"])
def verify_token():
    token=request.json
    t=token.get("token")
    data=user.google(t)
    
    return jsonify({"user":data})

@app.route("/set_data",methods=["POST"])
def data():
    data = request.json
    name = data.get("name")
    return jsonify({"message": "Session stored"}), 200

@app.route("/me", methods=["GET"])
def me():
    if not user:
        
        return jsonify({"error": "Not authenticated"}), 401
    print("Session user:", user)
    return jsonify({"user": user})
    
@app.route("/gets_data", methods=["POST"])
def gets_data():
    data = admin.get_data()  # list of all users
    login_data = request.json
    admin_input = login_data.get("admin")
    password_input = login_data.get("password")
    captcha_token = login_data.get("captcha")
    if not captcha_token or not admin.verify_user(captcha_token):
        return jsonify({"error": "Captcha verification failed"}), 400

    # Filter user matching email/password
    matched = [
        u for u in data
        if u.get("email", "").lower() == admin_input.lower() and u.get("password") == password_input
    ]

    return jsonify(matched)

@app.route("/sendmail", methods=["POST"])
def send_mail():
    data = request.json
    return jsonify(send(data))

@app.route("/add",methods=["POST"])
def add_data():
    data = request.json
    user_id = admin.add_data(data)
    return jsonify({"id": user_id})

@app.route("/get_data", methods=["GET"])
def get_data():
    data = admin.get_data()
    return jsonify(data)
    
@app.route("/block",methods=["POST"])
def block():
    user_eamil=request.json.get("email")
    user_role=request.json.get("role")
    status=request.json.get("status")
    if status == "Reject":
        result = admin.delete_user(user_eamil, user_role)
    else:
        result = admin.status(user_eamil, status, user_role)
    return jsonify(result)

@app.route("/password",methods=["POST"])
def password():
    user_mail=request.json.get("email")
    password=request.json.get("password")
    result=user1.password(user_mail,password)
    return jsonify()

@app.route("/add_prosal",methods=["POST"])
def proposal_add():
    data=request.json
    recive_mail=data.get('emails')
    send_mail=data.get('sendemail')
    count=proposal.gets_data(send_mail,recive_mail)
    
    if count:
        return jsonify({"message": "you already proposal sent"})

    result=proposal.add_data(data)
    return jsonify(result)

@app.route("/get_proposal",methods=["GET"])
def get_proposal():
    result=proposal.get_data()
    return jsonify(result)

@app.route("/update_proposal_status", methods=["POST"])
def update_proposal_status():
    data = request.json
    proposal_id = data.get("proposal_id")
    status = data.get("status")
    if not proposal_id or not status:
        return jsonify({"error": "Missing proposal_id or status"}), 400
    success = proposal.update_proposal_status(proposal_id, status)
    if success:
        return jsonify({"message": "Status updated successfully"})
    else:
        return jsonify({"error": "Failed to update status"}), 400
    
    data = request.json  # Expect JSON input
    
    # Example: {"N":50, "P":40, "K":60, "ph":6.5}
    features = [[
        data["N"],
        data["P"],
        data["K"],
        data["ph"]
    ]]
    
    prediction = model.predict(features)
    return jsonify({"Recommended Crop": prediction[0]})

@app.route("/add_user_data", methods=["POST"])
def get_user_data():
    data = request.form
    documents = request.files.getlist('documents')
    datas = [file.filename.split('.')[0] for file in documents]
    # Save each uploaded file
    for file in documents:
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

    data_dict = data.to_dict()
    data_dict['documents'] = datas
    result = user1.add_data(data_dict)
    return jsonify(result)

@app.route("/add_report", methods=["POST"])
def add_report():
    data = request.json   
    result = report.add_data(data)
    return jsonify(result)

@app.route("/get_reports", methods=["GET"])
def get_reports():
    result = report.get_report()
    return jsonify(result)

@app.route("/close_report", methods=["POST"])
def close_report():
    data = request.json
    report_id = data.get("id")
    result = report.update(report_id, "Closed")
    return jsonify({"modified": result.modified_count})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
