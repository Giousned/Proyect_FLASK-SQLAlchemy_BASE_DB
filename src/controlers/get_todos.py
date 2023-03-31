from database.database import db
from models.Todo import Todo

def get_todos():
    todos = db.session.execute(db.select(Todo)).scalars().all()
    
    response_body = []
    
    for todo in todos:
        response_body.append(todo.deserialize())

    return response_body