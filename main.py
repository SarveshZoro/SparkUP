from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

client = OpenAI(
    api_key=os.getenv("TOGETHER_API_KEY"),
    base_url="https://api.together.xyz/v1"
)

# System prompt
chat_history = [
    {"role": "system", "content": "You are a friendly motivational support assistant. You always respond with positivity, encouragement, and supportive advice, like a friend."}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    chat_history.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="mistralai/Mixtral-8x7B-Instruct-v0.1",
            messages=chat_history
        )
        assistant_reply = response.choices[0].message.content
        chat_history.append({"role": "assistant", "content": assistant_reply})
        return jsonify({"reply": assistant_reply})
    except Exception as e:
        return jsonify({"reply": f"❌ Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
