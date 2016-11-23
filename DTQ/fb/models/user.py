import import_package
from database import db, User
from helpers.user.profile import get_profile
class UserRecord:
  
  class UserState:
    NONE = 0
    LEARNING_WORDS = 1
    DOING_EXERSICE = 2
    CHOOSE_CATEGORY = 3
    TESTING_WORD = 4
    TESTING_LISTEN = 5

  @staticmethod
  def get(user_id):
    user = db.session.query(User)\
      .filter(User.user_id == user_id).first()
    if user:
      return user
    else:
      user = User(user_id, UserRecord.UserState.NONE)
      profile = get_profile(user_id)
      name = profile["first_name"] + " " + profile["last_name"]
      gender = profile["gender"]
      user.name = name
      user.gender = gender
      db.session.add(user)
      db.session.commit()
      return user

  @staticmethod
  def set_state(user_id, state):
    user = UserRecord.get(user_id)
    user.state = state
    db.session.commit()

  @staticmethod
  def get_state(user_id):
  	user = UserRecord.get(user_id)
  	return user.state
