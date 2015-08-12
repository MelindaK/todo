
class TodoException(Exception):
    """Base exception that all errors should inherit from.
    """
    statusCode = 500

    def __init__(self, message, details=None, result=None, info=None):
        super(TodoException, self).__init__()
        self.statusMsg = message
        self.statusDetails = details or {}
        self.result = result or {}
        self.info = info or {}

    def toDict(self):
        return {
            'result': self.result,
            'info': self.info,
            'status': {
                'statusCode': self.statusCode,
                'statusMsg': self.statusMsg,
                'statusDetails': self.statusDetails,
            },
        }


class Unauthorized(TodoException):
    """Exception where unauthorized request is made.
    """
    statusCode = 401

    def __init__(self, message="Unauthorized request.", details=None,
                 result=None, info=None):
        super(Unauthorized, self).__init__(message, details=None, result=None, info=None)
