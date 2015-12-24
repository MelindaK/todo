import json

from flask import request, session
from flask_restful import Resource
from sqlalchemy import and_

from app import db, Todo, TodoListPermission
from app.lib import authentication, response_util, status


class TodoMultiResource(Resource):
    """Class for creating and accessing todos.
    """
    @authentication.requiresAuth
    def get(self):
        """Method gets a list of all the todos and returns them in an OK
        response. The API can be filtered by todoListId to return a list of
        todos in the specified todoList.
        """
        userId = session.get('userId')
        todoListId = request.args.get('todoListId')

        if todoListId is None:
            permissions = TodoListPermission.query.filter_by(userId=userId)
            todoListIds = [permission.todoListId for permission in permissions]
            if not todoListIds:
                return response_util.buildOkResponse([])

            myTodos = Todo.query.filter(Todo.todoListId.in_(todoListIds))

            return response_util.buildOkResponse([todo.toDict() for todo in myTodos])
        else:
            todoListId = int(todoListId)  # bad request if not int
            permissions = TodoListPermission.query.filter(
                            and_(TodoListPermission.todoListId == todoListId,
                                TodoListPermission.userId == userId)).all()

            if not permissions:
                raise status.Forbidden()

            todos = Todo.query.filter_by(todoListId=todoListId)

            return response_util.buildOkResponse([todo.toDict() for todo in todos])

    @authentication.requiresAuth
    def post(self):
        """Method adds a new todo and returns the todo in an OK response..
        """
        data = json.loads(request.data)
        userId = session.get('userId')
        todoListId = data.get('todoListId')

        if not(data.get('subject') and todoListId):
            raise status.BadRequest()

        permission = TodoListPermission.query.filter(
                        and_(TodoListPermission.todoListId == todoListId,
                             TodoListPermission.userId == userId)).first()

        if permission is None:
            raise status.Forbidden()

        todo = Todo(data.get('subject'),
                    todoListId,
                    userId,
                    data.get('dueDate'),
                    data.get('description'),
                    data.get('priority'),
                    data.get('completed'),
                    data.get('assigneeId'))
        db.session.add(todo)
        db.session.commit()

        return response_util.buildOkResponse(todo.toDict())


class TodoResource(Resource):
    """Class for updating, deleting, getting a single todo.
    """
    @authentication.requiresAuth
    def put(self, todoId):
        """Method updates a todo instance and returns it todo in an OK response.

        Args:
            todoId - Interger, primary key identifying the todo.
        """
        data = json.loads(request.data)
        userId = session.get('userId')
        todo = Todo.query.get(todoId)

        if todo is None:
            raise status.NotFound()

        permission = TodoListPermission.query.filter(
                        and_(TodoListPermission.todoListId == todo.todoListId,
                             TodoListPermission.userId == userId)).first()

        if permission is None:
            raise status.Forbidden()

        todo.subject = data.get('subject') or todo.subject
        todo.dueDate = data.get('dueDate') or todo.dueDate
        todo.description = data.get('description') or todo.description
        todo.priority = data.get('priority') or todo.priority
        todo.assigneeId = data.get('assigneeId') or todo.assigneeId

        todo.completed = data.get('completed') \
            if data.get('completed') != todo.completed \
            else todo.completed

        db.session.commit()

        return response_util.buildOkResponse(todo.toDict())

    @authentication.requiresAuth
    def get(self, todoId):
        """Method gets and returns a single todo in an OK response.

        Args:
            todoId - Interger, primary key identifying the todo.
        """
        userId = session.get('userId')
        todo = Todo.query.get(todoId)

        if todo is None:
            raise status.NotFound()

        permission = TodoListPermission.query.filter(
                        and_(TodoListPermission.todoListId == todo.todoListId,
                             TodoListPermission.userId == userId)).first()

        if permission is None:
            raise status.Forbidden()

        return response_util.buildOkResponse(todo.toDict())

    @authentication.requiresAuth
    def delete(self, todoId):
        """Method deletes a todo and returns result none.

        Args:
            todoId - Interger, primary key identifying the todo.
        """
        userId = session.get('userId')
        todo = Todo.query.get(todoId)

        if todo is None:
            raise status.NotFound()

        permission = TodoListPermission.query.filter(
                        and_(TodoListPermission.todoListId == todo.todoListId,
                             TodoListPermission.userId == userId)).first()

        if permission is None:
            raise status.Forbidden()

        db.session.delete(todo)
        db.session.commit()

        return response_util.buildOkResponse(None)
