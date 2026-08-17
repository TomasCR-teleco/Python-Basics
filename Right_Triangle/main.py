#Calculate every angle of a right triangle when given 2 of its angles. Or calculate the sides and angles of the triangle when given 2 of its sides.
################################################################################
#Analysis:
#   Data input: side1 (float), side2 (float), type1 (string), type2 (string) / angle1 (float), angle2 (float).
#   Data output: angles (list), sides (list).
# Design:
#   1. Ask the user to choose between angle mode(a) or side mode(s).
#   2.1 Angle mode:
#       2.1.1 Ask the user to input the two angles.
#       2.1.2 Calculate the third angle.
#       2.1.3 Save the results in a file.
#   2.2 Side mode:
#       2.2.1 Ask the user to input the two sides and their types.
#       2.2.2 Calculate the third side.
#       2.2.3 Calculate all the angles.
#       2.2.4 Save the results in a file.
#   3. Display the results.
################################################################################
from calculus import calculate_sides, angle_sorter, calculate_angles
from validation import ask_float, ask_type
from data_saving import save
from output import inicial_menu, display_results, error_message
#####################################################################

def angle_mode(name):
    angle1 = ask_float("Write the first angle of the triangle:")
    angle2 = ask_float("Write the second angle of the triangle:")
    given_angles = [angle1, angle2]
    right_angle = 90
    if right_angle in given_angles:
            angle3 = 180 - (angle1 + angle2)
            angles = angle_sorter(angle1, angle2, angle3)
    else:
            angle3 = 90
            angles = [angle1, angle3, angle2]
    result = [given_angles, angles]
    save(name, f"Angle mode - Input: {given_angles} - Result: {angles}")
    display_results("angle_mode", result)

def side_mode(name):
    side1 = ask_float("Write the first side of the triangle:")
    side2 = ask_float("Write the second side of the triangle:")
    type1 = ask_type("Write the type of the first side (hypotenuse, leg):")
    type2 = ask_type("Write the type of the second side (hypotenuse, leg):")
    given_sides = [side1, side2]
    given_types = [type1, type2]
    sides = calculate_sides(side1, side2, type1, type2)
    if sides is None:
        return
    angles = calculate_angles(sides[0], sides[2])
    result = [given_sides, given_types, sides, angles]
    save(name, f"Side mode - Input: sides:{given_sides} - Result: sides:{sides}, angles:{angles}")
    display_results("side_mode", result)

#######################################################################################

def main():
    name = inicial_menu("username")
    valid_modes = ("a", "s")
    while True:
        mode = inicial_menu("mode")
        if mode == "a":
            inicial_menu("angle")
            angle_mode(name)
            break
        elif mode == "s":
            inicial_menu("side")
            side_mode(name)
            break
        else:
            error_message("invalid_mode", valid_modes)
if __name__ == "__main__":
    main()