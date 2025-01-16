from flask import Blueprint, jsonify, request
from .models import Task
from . import db

bp = Blueprint('routes', __name__)

@bp.route('/')
def home():
    return "Hello, World!"

@bp.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed
    } for task in tasks])

'''
Example usage:
    curl -X POST http://127.0.0.1:5000/tasks \
     -H "Content-Type: application/json" \
     -d '{"title": "New Task", "description": "This is a test task."}'
'''
@bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.json

    if not isinstance(data, list):  
        return jsonify({"error": "Expected a list of tasks"}), 400

    tasks_created = []
    for task_data in data:
        title = task_data.get('title')
        description = task_data.get('description', '')

        if not title:
            return jsonify({"error": "Each task must have a title"}), 400

        new_task = Task(title=title, description=description)
        db.session.add(new_task)
        tasks_created.append(new_task)

    db.session.commit()

    return jsonify({
        "message": f"{len(tasks_created)} tasks created",
        "tasks": [{"id": task.id, "title": task.title} for task in tasks_created]
    }), 201