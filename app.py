import turtle
import css
from tkinter import filedialog
import os
import time

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

    # Adds delay to the turtle
    turtle.delay(1000)

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

# This function will save the user written code in a txt file
def save_file():
    # Ask the directory to save the file
    directory = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save as...", filetypes=[("Text file", "*.txt")])

    # Check if directory was chosen
    if directory != "":
        directory += ".txt"

        # Open that txt file
        file = open(directory, "a")

        # Write the user's code
        for i in ENCODED_FILE:
            file.write(f"{i}\n")

        # Close the text file
        file.close()

# This function will open a file and save it to the ENCODED_FILE variable
def open_file():
    global ENCODED_FILE
    ENCODED_FILE.clear()

    # Ask the dialogue box for opening a file
    directory = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open file...", filetypes=[("Text file", "*.txt")])

    # Open that file
    with open(directory, "r") as file:
        # Read each line and append it to the ENCODED_FILE variable
        for i in file.readlines():
            line = i.replace("\n", "") # Removes the new line

            ENCODED_FILE.append(line)

# This function will add user's code to the ENCODED_FILE variable
def edit_file(move):
    global ENCODED_FILE

    command = move.split(",")[0] # "move forward, 10" ==> ["move forward", "10") ==> "move forward"
    steps = move.split(",")[1] # "move forward, 10" ==> ["move forward", "10") ==> "10"
    hint_command = command.split()[0] # This is the hint command to see what type of command it is. For example "move", "pen", "turn" or "delete"

    if hint_command == "move":
        ENCODED_FILE.append(f"{command} {steps} steps")

    elif hint_command == "pen":
        ENCODED_FILE.append(command)

    elif hint_command == "turn":
        ENCODED_FILE.append(f"{command} {steps} degrees")

    elif hint_command == "delete":
        index = int(steps) - 1 # This will convert the steps to an index

        ENCODED_FILE.pop(index) # Delete the element in the index position
    else:
         print("Wrong syntax")

# Greet
print("Hi. Welcome to Turtle Nursery where you can create python turtle files without writing a single line of code")
print()
time.sleep(2)
os.system("cls")

# The main part

while True:
    # Display command panel: What do you want to do run [r] edit [e] file settings [f]
    part_1 = css.color("run [r]", css.RED)
    part_2 = css.color("edit [e]", css.YELLOW)
    part_3 = css.color("file settings [f]", css.GREEN)
    ask_text = f"What do you want to do {part_1} {part_2} {part_3} exit [ex]: "
    command = input(ask_text)

    # Check what is the command
    if (command == "r") or (command == "run"):
        print(css.color("Running...", css.RED))
        run()
        continue

    elif command == "ex":
        break

    elif (command == "edit") or (command == "e"):
        os.system("cls")

        text_1 = css.color("move forward", css.RED)
        text_2 = css.color("move backward", css.RED)
        text_3 = css.color("turn right", css.YELLOW)
        text_4 = css.color("turn left", css.YELLOW)
        text_5 = css.color("pen up", css.GREEN)
        text_6 = css.color("pen down", css.GREEN)
        text_7 = css.color("delete", css.BLUE)

        code = ""
        line_number = 0
        while True:
            # Update the code for displaying
            line_number = 0
            code = ""
            for i in ENCODED_FILE:
                line_number += 1
                code += f"{line_number}. {i}\n"

            # Print the instructions and code
            total_text = f"{css.color('The commands', css.CYAN)} \n{text_1}, {text_2}, {text_3}, {text_4}, {text_5}, {text_6}, {text_7}\n\n{code}\n"
            print(total_text)

            # Ask the command
            total_move = input("Type your command here. Sytax: command,steps. For exiting mode [ex]: ")

            # Check if user want to exit
            if total_move != "ex":
                # Edit the file
                edit_file(total_move)

            elif total_move == "ex":
                # Break the loop will exit the program
                break

            os.system("cls")

        continue