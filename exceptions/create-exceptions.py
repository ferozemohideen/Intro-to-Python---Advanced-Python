class MissingLabelError(KeyError):
    pass

class PageNotFoundError(LookupError):
    pass

class IncorrectPasswordError(ValueError):
    pass

class IncorrectUsernameError(ValueError):
    pass

def login():
    raise IncorrectUsernameError

try:
    login()
except IncorrectUsernameError:
    print("Your username was incorrect. Try Again")
except IncorrectPasswordError:
    print("Your password was incorrect. Try Again")