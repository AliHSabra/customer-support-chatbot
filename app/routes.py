from flask import Blueprint, request, jsonify, render_template
from .chatbot import get_response

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return "Welcome to the Customer Support Chatbot!"

@main.route("/api/chatbot", methods=["POST"])
def chatbot_response():
    data = request.get_json()
    query = data.get("query")
    response = get_response(query)
    return jsonify({"response": response})
