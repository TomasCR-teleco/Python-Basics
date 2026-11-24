def save(user, text,):
    """Saves the result in the chosen file, associating it to the username"""
    with open("data.txt", "a") as file:
        file.write(f"{user} - {text}\n")