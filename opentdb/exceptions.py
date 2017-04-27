class OpenTDBException(IOError):
    """Generic error for when no other exception matches."""

    def __init__(self, *args, **kwargs):
        super(OpenTDBException, self).__init__(*args, **kwargs)

class ConnectionError(OpenTDBException):
    """An error occurred while connecting to the OpenTDB API."""

class APIError(OpenTDBException):
    """The response from the API is not what we were expecting."""

class HTTPError(OpenTDBException):
    """The HTTP request returned an unsuccessful status code."""
