from flask import Blueprint, jsonify, request
from database.database import db
from controlers.get_todos import get_todos
from controlers.create_todo import create_todo


api = Blueprint("api", __name__)

@api.route('/todos', methods=['GET', 'POST'])
def todos():
    if request.method == 'GET':
        return jsonify(get_todos())
    if request.method == 'POST':
        return jsonify(create_todo())