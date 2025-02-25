#----- USER CLASS -----#
class User():

    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

#----- LOGIC -----#
def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user: User):
    print(f"This is {user.name}'s new blog post")

new_user = User("Davide")
new_user.is_logged_in = True
create_blog_post(new_user)
