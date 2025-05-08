import pytest
import unittest.mock as mock
from src.controllers.usercontroller import UserController

@pytest.fixture
def user_data():
    return [
      {
        "firstName": "Jane",
        "lastName": "Doe",
        "email": "jane.doe@gmail.com",
      }
    ]

@pytest.fixture
def users_data():
    return [
      {
        "firstName": "Jane",
        "lastName": "Doe",
        "email": "jane.doe@gmail.com",
      },
      {
        "firstName": "Jane2",
        "lastName": "Doe2",
        "email": "jane.doe@gmail.com",
      },
    ]


pytestmark = pytest.mark.get_email
def test_get_user_by_no_email(user_data):
  mocked_dao = mock.MagicMock()
  mocked_dao.find.return_value = user_data

  user_controller = UserController(dao=mocked_dao)
  with pytest.raises(ValueError, match="Error: invalid email address"):
        user_controller.get_user_by_email("")

def test_get_user_by_wrong_format_email(user_data):
  mocked_dao = mock.MagicMock()
  mocked_dao.find.return_value = user_data

  user_controller = UserController(dao=mocked_dao)
  with pytest.raises(ValueError, match="Error: invalid email address"):
        user_controller.get_user_by_email("jane.doegmail")

def test_get_user_by_email(user_data):
  mocked_dao = mock.MagicMock()
  mocked_dao.find.return_value = user_data

  user_controller = UserController(dao=mocked_dao)
  result = user_controller.get_user_by_email(user_data[0]["email"])



  assert result == {'email': 'jane.doe@gmail.com', 'firstName': 'Jane', 'lastName': 'Doe'}

def test_get_users_by_email(users_data, capsys):
  mocked_dao = mock.MagicMock()
  mocked_dao.find.return_value = users_data

  user_controller = UserController(dao=mocked_dao)
  result = user_controller.get_user_by_email(users_data[0]["email"])

  assert result == {'email': 'jane.doe@gmail.com', 'firstName': 'Jane', 'lastName': 'Doe'}

def test_get_users_by_email_message(users_data, capsys):
  mocked_dao = mock.MagicMock()
  mocked_dao.find.return_value = users_data

  user_controller = UserController(dao=mocked_dao)
  result = user_controller.get_user_by_email(users_data[0]["email"])

  captured = capsys.readouterr()

  assert f"Error: more than one user found with mail {users_data[0]['email']}" in captured.out

def test_get_user_is_none_by_email():
  mocked_dao = mock.MagicMock()
  mocked_dao.find.return_value = []

  user_controller = UserController(dao=mocked_dao)
  with pytest.raises(IndexError, match=r".*None.*") as result:
    user_controller.get_user_by_email("hej@hej.com")