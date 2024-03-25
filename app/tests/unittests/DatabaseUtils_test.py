from app.database.db_utils import DatabaseUtils
import os
import pytest

class TestCase_createDatabase:
    @pytest.fixture
    def setup(self):
        if os.path.exists('./result.db'):
            os.remove('./result.db')
        yield
        if os.path.exists('./result.db'):
            os.remove('./result.db')

    def test_valid_normal(self, setup):
        excepted = True
        excepted_message = 'База данных создана'

        actual, actual_message = DatabaseUtils.create_database()

        assert actual == excepted
        assert actual_message == excepted_message
        assert os.path.exists('./result.db')

