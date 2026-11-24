import math
#############################################################################################################################################
def angle_sorter(a1, a2, a3):
    """This function will find which angle is the right one, and will make it be in the middle of the list, between the other two angles."""
    if a1 == 90:
        angles = [a2, a1, a3]
    else:
         angles = [a1, a2, a3]
    return angles

def calculate_sides(s1, s2, t1, t2):
    """This function will calculate the third side of the triangl."""
    if t1 == "hypotenuse" and t2 == "leg":
        hypotenuse = s1
        leg1 = s2
        leg2 = math.sqrt(hypotenuse**2 - leg1**2)
    elif t1 == "leg" and t2 == "hypotenuse":
        leg1 = s1
        hypotenuse = s2
        leg2 = math.sqrt(hypotenuse**2 - leg1**2)
    elif t1 == "leg" and t2 == "leg":
        leg1 = s1
        leg2 = s2
        hypotenuse = math.sqrt(leg1**2 + leg2**2)
    else:
        print("Your triangle seems to have two hypotenuses, please restart the program.")
        return None
    sides = [leg1, hypotenuse, leg2]
    return sides

def calculate_angles(leg1, leg2):
    """This function will calculate the angles of the triangle."""
    angle1 = math.degrees(math.atan(leg1/leg2))
    angle2 = math.degrees(math.atan(leg2/leg1))
    angle3 = 180 - (angle1 + angle2)
    angles = [angle1, angle3, angle2]
    return angles