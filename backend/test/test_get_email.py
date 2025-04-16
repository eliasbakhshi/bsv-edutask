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

  print('result: ', result.value)

  assert str(result.value) == 'Error: invalid email address'

def test_get_user_by_wrong_format_email(user_data):
  mocked_dao = mock.MagicMock()
  mocked_dao.find.return_value = user_data

  user_controller = UserController(dao=mocked_dao)
  with pytest.raises(ValueError) as result:
    user_controller.get_user_by_email("jane.doegmail")

  print('result: ', result.value)

  assert str(result.value) == 'Error: invalid email address'

# def test_get_user_by_email(user_data):
#   mocked_dao = mock.MagicMock()
#   mocked_dao.find.return_value = user_data

#   user_controller = UserController(dao=mocked_dao)
#   result = user_controller.get_user_by_email(user_data[0]["email"])

#   print('result: ', result)

#   assert result == {'email': 'jane.doe@gmail.com', 'firstName': 'Jane', 'lastName': 'Doe'}

# def test_get_user_by_email(user_data):
#   mocked_dao = mock.MagicMock()
#   mocked_dao.find.return_value = user_data

#   user_controller = UserController(dao=mocked_dao)
#   result = user_controller.get_user_by_email(user_data[0]["email"])

#   print('result: ', result)

#   assert result == {'email': 'jane.doe@gmail.com', 'firstName': 'Jane', 'lastName': 'Doe'}