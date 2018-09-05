# https://stackoverflow.com/questions/15300550/python-return-return-none-and-no-return-at-all
# http://dev.dafan.info/detail/537154?p=


# This tells that the function is indeed meant to return a value for later use, and in this case it returns None.
def return_none():
    print("Hello World")
    return None


# This is used for the same reason as break in loops.
# The return value doesn't matter and you only want to exit the whole function.
def find_prisoner_with_knife(prisoners):
    for prisoner in prisoners:
        if "knife" in prisoner.items:
            prisoner.move_to_inquisition()
            return  # no need to check rest of the prisoners nor raise an alert
    raise_alert()


# This will also return None, but that value is not meant to be used or caught.
def no_return():
    print("Hello World")


# the return value is () itself.
def return_bracket():
    print("Hello world")
    return ()
