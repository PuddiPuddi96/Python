from time import sleep

def delay_decorator(function):
    def wrapper_function():
        #Do something before
        sleep(2)
        function()
        #Do something after
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello!")

@delay_decorator
def say_bye():
    print("Bye!")

def say_greeting():
    print("How are you?")

say_bye()

#Alternative
decorated_function = delay_decorator(say_greeting)
decorated_function()
