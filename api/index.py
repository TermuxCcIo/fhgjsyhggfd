import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def sms_api():

    user_id = request.args.get("id")

    if not user_id:
        return jsonify({
            "status": False,
            "message": "Missing id parameter"
        }), 400

    try:
        url = f"https://api.subhxcosmo.in/api?key=suryanshrootx&type=sms&term={user_id}"
        response = requests.get(url)

        text_data = response.text

        # Replace telegram text
        text_data = text_data.replace("://t.me/SUBHXCOSMO", "Sahil.")

        try:
            data = response.json()
        except:
            return jsonify({
                "status": False,
                "message": "Invalid upstream response"
            }), 500

        # Force owner field
        data["owner"] = "Sahil."

        return jsonify(data)

    except Exception as e:
        return jsonify({
            "status": False,
            "message": "API fetch failed"
        }), 500
