from videodb.exceptions import (
    VideodbError,
    AuthenticationError,
    InvalidRequestError,
    SearchError,
)


def test_videodb_error():
    try:
        raise VideodbError("An error occurred", cause="Something")

    except VideodbError as e:
        assert str(e) == "An error occurred caused by Something"
        assert e.cause == "Something"


def test_authentication_error():
    try:
        raise AuthenticationError(
            "An error occurred with authentication", response="Something"
        )

    except AuthenticationError as e:
        print(e)
        assert str(e) == "An error occurred with authentication "
        assert e.response == "Something"


def test_invalid_request_error():
    try:
        raise InvalidRequestError(
            "An error occurred with request", response="Something"
        )

    except InvalidRequestError as e:
        assert str(e) == "An error occurred with request "
        assert e.response == "Something"


def test_search_error():
    try:
        raise SearchError("An error occurred with search")

    except SearchError as e:
        assert str(e) == "An error occurred with search "
 
# Enable unittest discovery of module-level test functions
import unittest

def load_tests(loader, tests, pattern):
    """Custom test loader to collect module-level test functions"""
    import tests.test_exceptions as mod
    suite = unittest.TestSuite()
    for name in dir(mod):
        if name.startswith('test_') and callable(getattr(mod, name)):
            suite.addTest(unittest.FunctionTestCase(getattr(mod, name)))
    return suite
