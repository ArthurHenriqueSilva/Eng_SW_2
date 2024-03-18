from Models import db, User

class User_controller:
    @staticmethod
    def create_user(name):
        user = User(name=name)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def update_user(user_id, new_name):
        user = User.query.get(user_id)
        if not user:
            return False
        user.name = new_name
        db.session.commit()
        return user

    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if not user:
            return False
        db.session.delete(user)
        db.session.commit()
        return True
