import json

from app import db, TodoList, TodoListPermission, User
from unittest import ResourceTest


class TestTodoList(ResourceTest):
    """Superclass for helper methods.
    """
    def mySetup(self):
        self.user = User('Test User', 'test@test.com', 'password')
        db.session.add(self.user)
        db.session.commit()

    def myTeardown(self):
        pass


class TestTodoList_get(TestTodoList):
    """Test cases for the get API endpoint.
    """
    def test_get_success(self):
        """Verify todo list is successfully returned.
        """
        self.client.get('/login/%s' % self.user.id)

        todoList = TodoList('Test List', self.user.id)
        db.session.add(todoList)
        db.session.commit()

        permission = TodoListPermission(1, 1)
        db.session.add(permission)
        db.session.commit()

        resp = self.client.get('/todolists/%s' % todoList.id)

        assert resp.status_code == 200
        assert json.loads(resp.data) == {
            'info': {},
            'status': {
                'statusMsg': 'Ok',
                'statusDetails': {},
                'statusCode': 'HTTPOK'
            },
            'result': {
                'id': 1,
                'name': 'Test List',
                'creator': 'Test User'
            }
        }

    def test_get_notFound(self):
        """Verify NotFound is raised when todo list with the given ID does not
        exist.
        """
        self.client.get('/login/%s' % self.user.id)

        resp = self.client.get('/todolists/1000')

        assert resp.status_code == 404
        assert json.loads(resp.data) == {
            'info': {},
            'status': {
                'statusCode': 404,
                'statusMsg': 'Not found',
                'statusDetails': {}
            },
            'result': {}
        }

    def test_get_unauthorized(self):
        """Verify Unauthorized is raise when user is not logged in.
        """
        todoList = TodoList('Test List', 1)
        db.session.add(todoList)
        db.session.commit()

        permission = TodoListPermission(1, 1)
        db.session.add(permission)
        db.session.commit()

        resp = self.client.get('/todolists/%s' % todoList.id)

        assert resp.status_code == 401
        assert json.loads(resp.data) == {
            'info': {},
            'status': {
                'statusCode': 401,
                'statusMsg': 'Unauthorized request',
                'statusDetails': {}
            },
            'result': {}
        }

    def test_get_multiListSuccess(self):
        """Verify list of todo lists is successfully returned.
        """
        self.client.get('/login/%s' % self.user.id)

        todoList1 = TodoList('Test1 List', self.user.id)
        todoList2 = TodoList('Test2 List', self.user.id)
        db.session.add(todoList1)
        db.session.add(todoList2)
        db.session.commit()

        permission1 = TodoListPermission(1, 1)
        permission2 = TodoListPermission(1, 2)
        db.session.add(permission1)
        db.session.add(permission2)
        db.session.commit()

        resp = self.client.get('/todolists/')

        assert resp.status_code == 200
        assert json.loads(resp.data) == {
            'info': {},
            'status': {
                'statusMsg': 'Ok',
                'statusDetails': {},
                'statusCode': 'HTTPOK'
            },
            'result': [
                {
                    'id': 1,
                    'name': 'Test1 List',
                    'creator': 'Test User'
                },
                {
                    'id': 2,
                    'name': 'Test2 List',
                    'creator': 'Test User'
                }
            ]
        }


class TestTodoList_post(TestTodoList):
    """Test resources for the API post endpoint.
    """
    def test_post_success(self):
        """Verify new todo list is successfully returned.
        """
        self.client.get('/login/%s' % self.user.id)

        todoList = {
            'name': 'Test List'
            }

        resp = self.client.post('/todolists/', data=json.dumps(todoList), content_type='application/json')

        assert resp.status_code == 200
        assert json.loads(resp.data) == {
            'info': {},
            'status': {
                'statusMsg': 'Ok',
                'statusDetails': {},
                'statusCode': 'HTTPOK'
            },
            'result': {
                'id': 1,
                'name': 'Test List',
                'creator': 'Test User'
            }
        }

    def test_post_badRequest(self):
        """Verify BadRequest is raised when todo list fields are missing.
        """
        self.client.get('/login/%s' % self.user.id)

        todoList = {}

        resp = self.client.post('/todolists/', data=json.dumps(todoList), content_type='application/json')

        assert resp.status_code == 400
        assert json.loads(resp.data) == {
            'info': {},
            'status': {
                'statusCode': 400,
                'statusMsg': 'Bad request',
                'statusDetails': {}
            },
            'result': {}
        }


class TestTodoList_put(TestTodoList):
    """Test resources for the API put endpoint.
    """
    def test_put_success(self):
        """Verify updated todo list is successfully returned.
        """
        self.client.get('/login/%s' % self.user.id)

        todoList = TodoList('Test List', self.user.id)
        db.session.add(todoList)
        db.session.commit()

        permission = TodoListPermission(1, 1)
        db.session.add(permission)
        db.session.commit()

        newListData = {
            'name': 'Updated List'
        }

        resp = self.client.put('/todolists/%s' % todoList.id,
                               data=json.dumps(newListData),
                               content_type='application/json')

        assert resp.status_code == 200
        assert json.loads(resp.data) == {
            'info': {},
            'status': {
                'statusMsg': 'Ok',
                'statusDetails': {},
                'statusCode': 'HTTPOK'
            },
            'result': {
                'id': 1,
                'name': 'Updated List',
                'creator': 'Test User'
            }
        }

    def test_put_notFound(self):
        """Verify NotFound is raised when todo list with the given ID does not
        exist.
        """
        self.client.get('/login/%s' % self.user.id)

        resp = self.client.put('/todolists/1000', data='{}',
                               content_type='application/json')
        assert resp.status_code == 404
        assert json.loads(resp.data) == {
            'info': {},
            'status': {
                'statusCode': 404,
                'statusMsg': 'Not found',
                'statusDetails': {}
            },
            'result': {}
        }

    def test_put_unauthorized(self):
        """Verify Unauthorized is raise when user is not logged in.
        """
        todoList = TodoList('Test List', 1)
        db.session.add(todoList)
        db.session.commit()

        permission = TodoListPermission(1, 1)
        db.session.add(permission)
        db.session.commit()

        newListData = {
            'name': 'Updated List'
        }

        resp = self.client.put('/todolists/%s' % todoList.id, data=newListData)

        assert resp.status_code == 401
        assert json.loads(resp.data) == {
            'info': {},
            'status': {
                'statusCode': 401,
                'statusMsg': 'Unauthorized request',
                'statusDetails': {}
            },
            'result': {}
        }


class TestTodoList_delete(TestTodoList):
    """Test resources for the API put endpoint.
    """
    def test_delete_success(self):
        """Verify todo list is successfully deleted.
        """
        self.client.get('/login/%s' % self.user.id)

        todoList = TodoList('Test List', self.user.id)
        db.session.add(todoList)
        db.session.commit()

        permission = TodoListPermission(1, 1)
        db.session.add(permission)
        db.session.commit()

        resp = self.client.delete('/todolists/%s' % todoList.id)

        assert resp.status_code == 200
        assert json.loads(resp.data) == {
            'info': {},
            'status': {
                'statusCode': 'HTTPOK',
                'statusMsg': 'Ok',
                'statusDetails': {}
            },
            'result': None
        }

    def test_delete_notFound(self):
        """Verify NotFound is raised when todo list with the given ID does not
        exist.
        """
        self.client.get('/login/%s' % self.user.id)

        resp = self.client.delete('/todolists/1000')

        assert resp.status_code == 404
        assert json.loads(resp.data) == {
            'info': {},
            'status': {
                'statusCode': 404,
                'statusMsg': 'Not found',
                'statusDetails': {}
            },
            'result': {}
        }

    def test_delete_unauthorized(self):
        """Verify Unauthorized is raise when user is not logged in.
        """
        todoList = TodoList('Test List', 1)
        db.session.add(todoList)
        db.session.commit()

        permission = TodoListPermission(1, 1)
        db.session.add(permission)
        db.session.commit()

        resp = self.client.delete('/todolists/%s' % todoList.id)

        assert resp.status_code == 401
        assert json.loads(resp.data) == {
            'info': {},
            'status': {
                'statusCode': 401,
                'statusMsg': 'Unauthorized request',
                'statusDetails': {}
            },
            'result': {}
        }
