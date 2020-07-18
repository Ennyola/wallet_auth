from django.contrib.auth.models import User

class EmailAuthentication(object):

    def authenticate(self, request, username, password):
        try:
            user = User.objects.get(email = username)
            password = user.check_password(password)
            if password:
                return user
            else:
                return None
        except User.DoesNotExist:
            pass
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk = user_id)
        except:
            return None
