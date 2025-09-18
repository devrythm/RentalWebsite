from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# Load API Key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful AI property sales assistant."},
            {"role": "user", "content": user_msg}
        ]
    )

    reply = response.choices[0].message.content.strip()
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
