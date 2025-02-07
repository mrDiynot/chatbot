from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from datetime import datetime

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key='AIzaSyAZ9YWk1vOykCkHVTu07bZgDUJlo6NyhQo')

model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/chat_response', methods=['POST'])
def chat_response():
    message = request.json['message']
    response = model.generate_content(message)
    return jsonify({
        'response': response.text,
        'timestamp': datetime.now().strftime("%H:%M")
    })

if __name__ == '__main__':
    app.run(debug=True)