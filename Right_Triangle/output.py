def inicial_menu(option):
    if option == "username":
        name = input("What's your name?")
        return name
    elif option == "mode":
        print("Hi, welcome to the Right Triangle Calculator")
        print("Here, you'll be able to calculate all the sides and angles of a right triangle, when given two of its sides, and the third angle when given 2 of its angles")
        print("Now, please, choose between the angle mode(a) or the side mode(s):")
        mode = input("Write 'a' for angle mode or 's' for side mode:")
        return mode
    elif option == "angle":
        print ("You have just chosen the angle mode")
    elif option == "side":
        print("You have chosen the side mode")

def display_results(mode, result):
    if mode == "angle_mode":
        print("With the angles you gave (", result[0], "), the program has calculated the third one, and here's the result:")
        print(result[1])
    if mode == "side_mode":
        print("With the sides you gave (", result[0], ",being: ", result[1], "), the program has calculated the third one, and here's the result:")
        print(result[2])
        print("Finally with those sides, it has calculated all the angles of the triangle:")
        print(result[3])

def error_message(error_type, expected_input):
    if error_type == "invalid_input":
        print("Your input is invalid, expected:", expected_input, ", please try again.")
    if error_type == "invalid_type":
        print("Your input is invalid, expected:", expected_input[0], ", or:", expected_input[1], ", please try again.")
    if error_type == "invalid_mode":
        print("Your input is invalid, expected:", expected_input[0], ", or:", expected_input[1], ", please try again.")
    if error_type == "impossible_triangle":
        print("The triangle you are trying to solve doesn't make sense, check your inputs and try again.")