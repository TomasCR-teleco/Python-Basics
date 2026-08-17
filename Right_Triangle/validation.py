from output import error_message
################################################################################
def ask_float(text):
    """Asks for the user to input a number (float), repeating itself in case it isn't a number"""
    while True:
        try:
            value = float(input(text))
            break
        except ValueError:
            error_message("invalid_input", "float")
    return value

def ask_type(text):
    """Asks for the user to input a certain string, repeating itself in case it isn't one of those."""
    valid_types = ("hypotenuse", "leg")
    while True:
        value = input(text).strip().lower()
        if value in valid_types:
            return value
        error_message("invalid_type", valid_types)