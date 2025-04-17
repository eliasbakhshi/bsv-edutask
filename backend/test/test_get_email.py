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

# def test_hasAttribute_true(user_data):
#     result = hasAttribute(user_data, 'email')
#     assert result == True

pytestmark = pytest.mark.get_email
def test_get_user_by_no_email(user_data):
  mocked_dao = mock.MagicMock()
  mocked_dao.find.return_value = user_data

  user_controller = UserController(dao=mocked_dao)
  with pytest.raises(ValueError) as result:
    user_controller.get_user_by_email("")

  # print('result: ', result.value)

  assert str(result.value) == 'Error: invalid email address'

def test_get_user_by_wrong_format_email(user_data):
  mocked_dao = mock.MagicMock()
  mocked_dao.find.return_value = user_data

  user_controller = UserController(dao=mocked_dao)
  with pytest.raises(ValueError) as result:
    user_controller.get_user_by_email("jane.doegmail")

  # print('result: ', result.value)

  assert str(result.value) == 'Error: invalid email address'

def test_get_user_by_email(user_data):
  mocked_dao = mock.MagicMock()
  mocked_dao.find.return_value = user_data

  user_controller = UserController(dao=mocked_dao)
  result = user_controller.get_user_by_email(user_data[0]["email"])

  # print('result: ', result)

  assert result == {'email': 'jane.doe@gmail.com', 'firstName': 'Jane', 'lastName': 'Doe'}

def test_get_users_by_email(users_data, capsys):
  mocked_dao = mock.MagicMock()
  mocked_dao.find.return_value = users_data

  user_controller = UserController(dao=mocked_dao)
  result = user_controller.get_user_by_email(users_data[0]["email"])

  captured = capsys.readouterr()

  assert f"Error: more than one user found with mail {users_data[0]['email']}" in captured.out

  assert result == {'email': 'jane.doe@gmail.com', 'firstName': 'Jane', 'lastName': 'Doe'}
  

# def test_get_user_is_none_by_email():
#   mocked_dao = mock.MagicMock()
#   mocked_dao.find.return_value = None

#   user_controller = UserController(dao=mocked_dao)
#   with pytest.raises(TypeError) as result:
#     user_controller.get_user_by_email("hej@hej.com")

#   print('test_get_user_is_none_by_email result:', result)

#   assert str(result.value) == "object of type 'NoneType' has no len()"

def test_get_user_is_none_by_email():
  mocked_dao = mock.MagicMock()
  mocked_dao.find.return_value = []

  user_controller = UserController(dao=mocked_dao)
  with pytest.raises(IndexError) as result:
    user_controller.get_user_by_email("hej@hej.com")

  # print('test_get_user_is_none_by_email result:', result.value)

  assert str(result.value) == "None"






