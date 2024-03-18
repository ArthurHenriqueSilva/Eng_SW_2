import Controllers
from API import app

class UserTests:

    user_default_name = "Freddie Mercury"
    user_update_name = "Freddie Mercury from Queen"

    @staticmethod
    def test_create_user():
        with app.app_context():
            try:
                user = Controllers.User_controller.create_user(UserTests.user_default_name)
                assert user is not None
                assert user.name == UserTests.user_default_name
                print("Test create_user passed.")
            except AssertionError as e:
                print("Test create_user failed:", e)

    @staticmethod
    def test_get_user_by_id():
        with app.app_context():
            try:
                user = Controllers.User_controller.create_user(UserTests.user_default_name)
                retrieved_user = Controllers.User_controller.get_user_by_id(user.id)
                assert retrieved_user is not None
                assert retrieved_user.name == UserTests.user_default_name
                print("Test get_user_by_id passed.")
            except AssertionError as e:
                print("Test get_user_by_id failed:", e)

    @staticmethod
    def test_update_user():
        with app.app_context():
            try:
                user = Controllers.User_controller.create_user(UserTests.user_default_name)
                updated_user = Controllers.User_controller.update_user(user.id, UserTests.user_update_name)
                assert updated_user is not None
                assert updated_user.name == UserTests.user_update_name
                print("Test update_user passed.")
            except AssertionError as e:
                print("Test update_user failed:", e)

    @staticmethod
    def test_delete_user():
        with app.app_context():
            try:
                user = Controllers.User_controller.create_user(UserTests.user_default_name)
                deleted = Controllers.User_controller.delete_user(user.id)
                assert deleted
                print("Test delete_user passed.")
            except AssertionError as e:
                print("Test delete_user failed:", e)

    @staticmethod
    def run_all_tests():
        UserTests.test_create_user()
        UserTests.test_get_user_by_id()
        UserTests.test_update_user()
        UserTests.test_delete_user()

        print("All user tests completed.")

if __name__ == '__main__':
    UserTests.run_all_tests()
