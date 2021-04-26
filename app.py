import turtle
import css

# Functions and global variables
ENDCODED_FILE = []

def decode():
    """
    This function will convert the user's code, which is in the ENCODED_FILE variable, to python
    turtle code and store it in the DECODED_FILE variable
    """

    global DECODED_FILE
    DECODED_FILE = []

    # Loop through each command in the ENCODED_FILE
    for i in ENDCODED_FILE:
        first_part = i.split()[0]
        second_part = i.split()[1]

        if first_part == "move":
            if second_part == "forward":
                steps = i.split()[2]
                decoded_line = f"my_turtle.forward({steps})"

                DECODED_FILE.append(decoded_line)

            if second_part == "backward":
                steps = i.split()[2]
                decoded_line = f"my_turtle.backward({steps})"

                DECODED_FILE.append(decoded_line)

        elif first_part == "pen":
            if second_part == "up":
                decoded_line = "my_turtle.pen_up()"

                DECODED_FILE.append(decoded_line)

            if second_part == "down":
                decoded_line = "my_turtle.pen_down()"

                DECODED_FILE.append(decoded_line)

        elif first_part == "turn":
            if second_part == "left":
                degrees = i.split()[2]
                decoded_line = f"my_turtle.left({degrees})"

                DECODED_FILE.append(decoded_line)
            if second_part == "right":
                degrees = i.split()[2]
                decoded_line = f"my_turtle.right({degrees})"

                DECODED_FILE.append(decoded_line)

    return DECODED_FILE

# Greet
print("Hi. Welcome to Turtle Nursery where you can create python turtle files without writing a single line of code")
print()

# The main part
while True:
    pass