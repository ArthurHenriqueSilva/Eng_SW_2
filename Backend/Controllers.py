from Models import db, User

class User_controller:
    @staticmethod
    def create_user(name, email, password):
        try:
            user = User(name=name, email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            return user
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def update_user(user_id, new_name=None, new_email=None, new_password=None):
        try:
            user = User.query.get(user_id)
            if not user: return False
            if new_name: user.name = new_name
            if new_email: user.email = new_email
            if new_password: user.set_password(new_password)
            db.session.commit()
            return user
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def delete_user(user_id):
        try:
            user = User.query.get(user_id)
            if not user: return False
            db.session.delete(user)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def login(email, password):
        try:
            user = User.query.filter_by(email=email).first()
            if not user: return None
            if not user.check_password(password): return False
            return user
        except Exception as e:
            db.session.rollback()
            raise e
