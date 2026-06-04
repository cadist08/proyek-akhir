from flask import Flask, render_template, request, jsonify
from engine import GovernmentChatbot

app = Flask(__name__)

bot = GovernmentChatbot()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()
    message = data["message"]

    reply = bot.process(message)

    return jsonify({
        "reply": reply
    })

if __name__ == "__main__":
    app.run(debug=True)