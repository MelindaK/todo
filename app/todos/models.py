from app import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String)
    todoListId = db.Column(db.Integer, db.ForeignKey('todo_list.id'))
    dueDate = db.Column(db.DateTime)
    description = db.Column(db.Text)
    #creatorId = db.Column(db.Integer, db.ForeignKey('user.id'))
    priority = db.Column(db.Integer)
    completed = db.Column(db.Boolean)
    assigneeId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    #creator = db.relationship('User')
    assignee = db.relationship('User', backref=db.backref('assignedTodos'))
    todoList = db.relationship('TodoList', backref=db.backref('todos'))

    def __init__(self, subject, todoListId, dueDate, description,
                 priority=3, completed=False, assigneeId=None):
        self.subject = subject
        self.todoListId = todoListId
        self.dueDate = dueDate
        self.description = description
        #self.creatorId = creatorId
        self.priority = priority
        self.completed = completed
        self.assigneeId = assigneeId
