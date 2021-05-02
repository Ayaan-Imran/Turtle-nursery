import turtle
import css

# Functions and global variables
ENCODED_FILE = []
DECODED_FILE = []

# Decodes it to python turtle language - Will be used for exporting
def decode():
    """
    This function will convert the user's code, which is in the ENCODED_FILE variable, to python
    turtle code and store it in the DECODED_FILE variable
    """

    global DECODED_FILE
    DECODED_FILE = []

    # Loop through each command in the ENCODED_FILE
    for i in ENCODED_FILE:
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
                decoded_line = "my_turtle.penup()"

                DECODED_FILE.append(decoded_line)

            if second_part == "down":
                decoded_line = "my_turtle.pendown()"

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

# Encodes it to user's code - Will be used for importing
def encode():
    """
    This function will convert the python turtle code, which is in the DECODED_FILE variable, to user's
    code and store it in the ENCODED_FILE variable
    """

    global ENCODED_FILE

    # Clear the encoded file variable
    ENCODED_FILE.clear()

    # Loop through each command in the DECODED_FILE
    for i in DECODED_FILE: # i = my_turtle.forward(20)
        main_line = i.split(".")[1]  # Remove the 'my_turtle.' part

        command = main_line.split("(")[0] # Gets the command: Example forward

        # This part gets the steps
        steps = ""
        for i in main_line:
            numbers = [f"{i}" for i in range(0, 11)] # Creates numbers: "1", "2", "3", "0" ...

            if i in numbers: # Checks if i is a number
                steps += i # Appends this to the steps variable

        if steps == "": # Cleans the steps. If command is penup, that means steps is None
            steps = None
        else:
            steps = int(steps)

        # Convert to user's code
        if (command == "forward") or (command == "backward"):
            user_code = f"move {command} {steps} steps"

        elif command == "penup":
            user_code = "pen up"

        elif command == "pendown":
            user_code = "pen down"

        elif (command == "left") or (command == "right"):
            user_code = f"turn {command} {steps} degrees"

        # Append it to the ENCODED_FILE
        ENCODED_FILE.append(user_code)

    return ENCODED_FILE

# This will run the program with the help of the ENCODED_FILE
def run():
    """
    This will add some additional lines of code to the DECODED_FILE and will run the program
    """

    # Initialize turtle
    my_turtle = turtle.Turtle()

    for i in ENCODED_FILE:
        first_part = i.split()[0] # This is the command: Example "pen", "move", "turn"
        second_part = i.split()[1] # This is the 2nd part of the command: "forward", "up", "left"

        if first_part == "move":
            if second_part == "forward":
                steps = i.split()[2]
                my_turtle.forward(int(steps))

            if second_part == "backward":
                steps = i.split()[2]

                my_turtle.backward(int(steps))

        elif first_part == "pen":
            if second_part == "up":
                my_turtle.penup()

            if second_part == "down":
                my_turtle.pendown()

        elif first_part == "turn":
            if second_part == "left":
                degrees = i.split()[2]
                my_turtle.left(int(degrees))

            if second_part == "right":
                degrees = i.split()[2]
                my_turtle.right(int(degrees))

    turtle.done()

# Greet
print("Hi. Welcome to Turtle Nursery where you can create python turtle files without writing a single line of code")
print()

# The main part
while True:
    pass