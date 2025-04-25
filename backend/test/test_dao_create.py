import pytest
from unittest.mock import patch
import os
from src.util.dao import DAO
from pymongo.errors import WriteError


@pytest.fixture
def create_data():
    return {
        "name": "Jane",
        "age": 25,
        "email": "jane.doe@gmail.com",
    }


@pytest.fixture
def mock_getValidator():
    with patch('src.util.dao.getValidator') as mock_getValidator:
        # Mock the return value of getValidator
        mock_getValidator.return_value = {
            "$jsonSchema": {
                "bsonType": "object",
                "required": ["name", "age", "email"],
                "properties": {
                    "name": {
                        "bsonType": "string",
                        "description": "The first name of a user must be a string."
                    },
                    "age": {
                        "bsonType": "number",
                        "description": "The age of a user must be a number."
                    },
                    "email": {
                        "bsonType": "string",
                        "description": "The email address of a user must be a string.",
                        "uniqueItems": True
                    }
                }
            }
        }
        os.environ['MONGO_URL'] = "mongodb://root:root@localhost:27017"

        yield mock_getValidator

        del os.environ['MONGO_URL']


pytestmark = pytest.mark.create_collection
# def test_create_collection(mock_getValidator):
#     # Create an instance of the DAO class
#     dao = DAO('test_users')

#     print(f"Collection name: {dao.collection.name}")

#     # Assert that the collection was created successfully
#     assert dao.collection.name == 'test_users'


def test_create_user(mock_getValidator, create_data):
    dao = DAO('test_users')
    created_user = dao.create(create_data)
    create_data_with_id = {**create_data, "_id": created_user["_id"]}
    assert created_user == create_data_with_id

    dao.delete(created_user["_id"])


def test_create_user_same_email(mock_getValidator, create_data):
    dao = DAO('test_users')
    created_user = dao.create(create_data)
    created_user2 = dao.create(create_data)
    with pytest.raises(WriteError) as result:
        print(result)
    # check the the email does not exist
    # existing_user = dao.collection.find_one({"email": create_data["email"]})
    # print(f"Existing user 222222222222222222222222: {existing_user}")
    # assert existing_user is None, f"User with email {create_data['email']} already exists."

    dao.delete(created_user["_id"])


# def test_create_user(mock_getValidator, create_data):
#     dao = DAO('test_users')
#     created_user = dao.create(create_data)
#     create_data_with_id = {**create_data, "_id": created_user["_id"]}
#     assert created_user == create_data_with_id

# def test_create_user(mock_getValidator, create_data):
#     dao = DAO('test_users')
#     created_user = dao.create(create_data)
#     create_data_with_id = {**create_data, "_id": created_user["_id"]}
#     assert created_user == create_data_with_id
