from database.database import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String, nullable=False)
    done = db.Column(db.Boolean, nullable=False)


    def deserialize(self):
        return {
            "id": self.id,
            "label": self.label,
            "done": self.done
        }