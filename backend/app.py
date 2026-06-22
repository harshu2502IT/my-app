from flask import Flask, request, jsonify, render_template
from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

# ✅ Serve single combined page (Home + Login)
@app.route('/')
def home():
    return render_template('index.html')

# ✅ Login API
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    result = (
        supabase
        .table("OrderList")
        .select("*")
        .eq("email", email)
        .eq("password", password)
        .execute()
    )

    if len(result.data) > 0:
        return jsonify({
            "success": True,
            "message": "Login Successful"
        })

    return jsonify({
        "success": False,
        "message": "Invalid Email or Password"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)