import json

from flask import request, session
from flask_restful import Resource
from sqlalchemy import and_

from app import db, TodoList, TodoListPermission
from app.lib import authentication, response_util, status


class TodoListMultiResource(Resource):
    """Class for creating and accessing lists.
    """
    @authentication.requiresAuth
    def get(self):
        """Method gets a list of logged in user's todoLists and returns them in
        an Ok response.
        """
        userId = session.get('userId')
        permissions = TodoListPermission.query.filter_by(userId=userId)
        todoListIds = [permission.todoListId for permission in permissions]

        if not todoListIds:
            return response_util.buildOkResponse([])

        todoLists = TodoList.query.filter(TodoList.id.in_(todoListIds))

        return response_util.buildOkResponse([todoList.toDict()
                                              for todoList in todoLists])

    @authentication.requiresAuth
    def post(self):
        """Method creates a todoList and returns it in an Ok response.
        """
        data = json.loads(request.data)

        if not(data.get('name')):
            raise status.BadRequest()

        todoList = TodoList(data.get('name'), session.get('userId'))
        db.session.add(todoList)
        db.session.commit()

        permission = TodoListPermission(session.get('userId'), todoList.id)
        db.session.add(permission)
        db.session.commit()

        return response_util.buildOkResponse(todoList.toDict())


class TodoListResource(Resource):
    """Class to get, update, or delete a single todoList.
    """
    @authentication.requiresAuth
    def put(self, todoListId):
        """Method that updates and returns a todoList in an Ok response.

        Args:
            listId - An integer, primary key that identifies the todo list.
        """
        userId = session.get('userId')
        todoList = TodoList.query.get(todoListId)
        data = json.loads(request.data)

        if todoList is None:
            raise status.NotFound()

        permission = TodoListPermission.query.filter(
                        and_(TodoListPermission.todoListId == todoList.id,
                             TodoListPermission.userId == userId)).first()

        if permission is None:
            raise status.Unauthorized()

        todoList.name = data.get('name') or todoList.name
        db.session.commit()

        return response_util.buildOkResponse(todoList.toDict())

    @authentication.requiresAuth
    def get(self, todoListId):
        """Method that gets and returns a todoList in an Ok response.

        Args:
            todoListId - An integer, primary key that identifies the todo list.
        """
        userId = session.get('userId')
        todoList = TodoList.query.get(todoListId)

        if todoList is None:
            raise status.NotFound()

        permission = TodoListPermission.query.filter(
                        and_(TodoListPermission.todoListId == todoList.id,
                             TodoListPermission.userId == userId)).first()

        if permission is None:
            raise status.Unauthorized()

        return response_util.buildOkResponse(todoList.toDict())

    @authentication.requiresAuth
    def delete(self, todoListId):
        """Method that deletes a todoList and returns result None.

        Args:
            todoListId - An integer, primary key that identifies the todo list.
        """
        userId = session.get('userId')
        todoList = TodoList.query.get(todoListId)

        if todoList is None:
            raise status.NotFound()

        permission = TodoListPermission.query.filter(
                        and_(TodoListPermission.todoListId == todoList.id,
                             TodoListPermission.userId == userId)).first()

        if permission is None:
            raise status.Unauthorized()

        db.session.delete(todoList)
        db.session.commit()

        return response_util.buildOkResponse(None)
