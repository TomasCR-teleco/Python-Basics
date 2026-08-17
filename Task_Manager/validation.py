def ask_text(prompt):
    """Asks for a non-empty text input from the user."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This can't be empty, please try again.")