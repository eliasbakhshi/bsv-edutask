import pytest
from unittest.mock import patch
import os
from src.util.dao import DAO
from pymongo.errors import WriteError


@pytest.fixture
def create_data():
    return {
        "name": "Jane",
        "age": 1,
        "email": "jane.doe@gmail.com",
    }

@pytest.fixture
def invalid_data():
    return {
        "name": 1,
        "age": "Jane",
        "email": 1,
    }

@pytest.fixture
def partially_invalid_data():
    return {
        "name": 1,
        "age": 1,
        "email": "jane.doe@gmail.com",
    }

@pytest.fixture
def dao(mock_getValidator):
    os.environ['MONGO_URL'] = "mongodb://root:root@localhost:27017"
    dao = DAO('test_users')
    dao.collection.create_index("email", unique=True)
    yield dao
    dao.collection.drop()
    del os.environ['MONGO_URL']

@pytest.fixture
def mock_getValidator():
    with patch('src.util.dao.getValidator') as mock_getValidator:
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
                        "description": "the email address of a user must be determined",
                        "uniqueItems": True
                    },
                }
            }
        }
        yield mock_getValidator


pytestmark = pytest.mark.create_collection

def test_create_user(dao, mock_getValidator, create_data):
    created_user = dao.create(create_data)
    create_data_with_id = {**create_data, "_id": created_user["_id"]}
    dao.delete(str(created_user["_id"]["$oid"]))
    assert created_user == create_data_with_id

def test_create_user_invalid_data(dao, mock_getValidator, invalid_data):
    with pytest.raises(WriteError) as result:
        dao.create(invalid_data)
    assert "Document failed validation" in str(result.value)

def test_create_user_partially_invalid_data(dao, mock_getValidator, partially_invalid_data):
    with pytest.raises(WriteError) as result:
        dao.create(partially_invalid_data)
    assert "Document failed validation" in str(result.value)

@pytest.mark.new
def test_create_user_same_email(dao, mock_getValidator, create_data):
    created_user = dao.create(create_data)
    with pytest.raises(WriteError) as result:
        dao.create(create_data)

    dao.delete(str(created_user["_id"]["$oid"]))
