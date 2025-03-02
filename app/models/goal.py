from app import db


class Goal(db.Model):
    goal_id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    tasks = db.relationship('Task', back_populates='goal', lazy=True)

    def goal_to_dict(self):
        return {
            "id": self.goal_id,
            "title": self.title,
            }
