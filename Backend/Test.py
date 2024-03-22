import Controllers
from API import app

class UserTests:

    user_default_names = ["Freddie Mercury", "John Lennon", "Elvis Presley", "Michael Jackson", "David Bowie"]
    user_default_password = '12345'
    user_update_names = ["Freddie Mercury from Queen", "John Lennon from The Beatles", "Elvis Presley the King", "Michael Jackson the King of Pop", "David Bowie from Ziggy Stardust"]

    @staticmethod
    def generate_unique_email(username):
        return f"{username.replace(' ', '_')}@example.com"

    @staticmethod
    def test_create_user():
        with app.app_context():
            try:
                user_default_name = UserTests.user_default_names[0]
                user_email = UserTests.generate_unique_email(user_default_name)
                user = Controllers.User_controller.create_user(user_default_name, user_email, UserTests.user_default_password)
                assert user is not None
                assert user.name == user_default_name
                print("Test create_user passed.")
            except AssertionError as e:
                print("Test create_user failed:", e)

    @staticmethod
    def test_get_user_by_id():
        with app.app_context():
            try:
                user_default_name = UserTests.user_default_names[1]
                user_email = UserTests.generate_unique_email(user_default_name)
                user = Controllers.User_controller.create_user(user_default_name, user_email, UserTests.user_default_password)
                retrieved_user = Controllers.User_controller.get_user_by_id(user.id)
                assert retrieved_user is not None
                assert retrieved_user.name == user_default_name
                print("Test get_user_by_id passed.")
            except AssertionError as e:
                print("Test get_user_by_id failed:", e)

    @staticmethod
    def test_update_user():
        with app.app_context():
            try:
                user_default_name = UserTests.user_default_names[2]
                user_email = UserTests.generate_unique_email(user_default_name)
                user = Controllers.User_controller.create_user(user_default_name, user_email, UserTests.user_default_password)
                updated_user = Controllers.User_controller.update_user(user.id, UserTests.user_update_names[0])
                assert updated_user is not None
                assert updated_user.name == UserTests.user_update_names[0]
                print("Test update_user passed.")
            except AssertionError as e:
                print("Test update_user failed:", e)

    @staticmethod
    def test_delete_user():
        with app.app_context():
            try:
                user_default_name = UserTests.user_default_names[3]
                user_email = UserTests.generate_unique_email(user_default_name)
                user = Controllers.User_controller.create_user(user_default_name, user_email, UserTests.user_default_password)
                deleted = Controllers.User_controller.delete_user(user.id)
                assert deleted
                print("Test delete_user passed.")
            except AssertionError as e:
                print("Test delete_user failed:", e)
    
    @staticmethod
    def test_login():
        with app.app_context():
            try:
                user_default_name = UserTests.user_default_names[4]
                user_email = UserTests.generate_unique_email(user_default_name)
                response = app.test_client().post('/login', json={'email': user_email, 'password': UserTests.user_default_password})
                data = response.get_json()

                assert response.status_code == 200
                assert data['message'] == 'Login successful'

                user_data = data.get('user')
                assert user_data is not None
                assert 'id' in user_data
                assert 'name' in user_data
                assert 'email' in user_data

                print("Test login passed.")
            except AssertionError as e:
                print("Test login failed:", e)

    @staticmethod
    def run_all_tests():
        UserTests.test_create_user()
        UserTests.test_get_user_by_id()
        UserTests.test_update_user()
        UserTests.test_delete_user()

        print("All user tests completed.")

if __name__ == '__main__':
    UserTests.run_all_tests()
