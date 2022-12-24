import turtle
import termcolor
from tkinter import filedialog
import os
import time

# Functions and global variables
ENCODED_FILE = []
DECODED_FILE = []
my_turtle = turtle.Turtle()
positive = termcolor.colored('[', 'cyan') + termcolor.colored('+', 'green') + termcolor.colored(']', 'cyan') + ' '
neutral = termcolor.colored('[', 'cyan') + termcolor.colored('-', 'yellow') + termcolor.colored(']', 'cyan') + ' '
negative = termcolor.colored('[', 'cyan') + termcolor.colored('!', 'red') + termcolor.colored(']', 'cyan') + ' '

# Formatting tool
def number(number):
    return termcolor.colored('[', 'cyan') + termcolor.colored(str(number), 'yellow') + termcolor.colored(']', 'cyan') + ' '

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
    # Add delay to the turtle
    time.sleep(2)

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
        
        return True
        
    else:
        return None

# This function will open a file and save it to the ENCODED_FILE variable
def open_file():
    global ENCODED_FILE
    ENCODED_FILE.clear()

    # Ask the dialogue box for opening a file
    directory = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open file...", filetypes=[("Text file", "*.txt")])
    
    # Check if the user declined on chosing a file
    if directory == "":
        return None
    
    # Open that file
    with open(directory, "r") as file:
        # Read each line and append it to the ENCODED_FILE variable
        for i in file.readlines():
            line = i.replace("\n", "") # Removes the new line

            ENCODED_FILE.append(line)
            
    return True

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
        
    elif hint_command == "square":
        for _ in range(4):
            edit_file("move forward," + steps)
            edit_file("turn right,90")
        
    else:
         return False

# Greet the user
try:
    termcolor.cprint("Welcome to Turtle Nursery", "blue", attrs=["underline"])
    print(termcolor.colored("Turtle nursery", "cyan") + " helps a user to use the turtle module in python without coding.")

    while True:
        print("\r", end="\r")
        
except KeyboardInterrupt:
    dots = "" 
    for i in range(4):
        os.system("cls")
        print("\r" + termcolor.colored("Proceeding" + dots, "blue"), end="\r")
        dots += "."
        time.sleep(0.5)
    
# The main part
while True:
    # Clear screen everytime user enters main screen
    os.system("cls")
    
    # Display command panel: What do you want to do run [r] edit [e] file settings [f]
    print(number(1) + "Run commands")
    print(number(2) + "Edit commands")
    print(number(3) + "File settings [Save commands to file] [Open existing commands from file]")
    print()
    command = input(neutral + f"Enter the index number of the corresponding functions {termcolor.colored('[ENTER] to exit', 'grey')}: ")

    # Check what is the command
    if command == "1":
        print(positive + "Running...")

        run()
        continue

    elif command == "":
        break

    elif command == "2":
        os.system("cls")

        text_1 = termcolor.colored("move forward", "red")
        text_2 = termcolor.colored("move backward", "red")
        text_3 = termcolor.colored("turn right", "yellow")
        text_4 = termcolor.colored("turn left", "yellow")
        text_5 = termcolor.colored("pen up", "green")
        text_6 = termcolor.colored("pen down", "green")
        text_7 = termcolor.colored("delete", "blue")
        text_8 = termcolor.colored("square", "blue")

        code = ""
        line_number = 0
        while True:
            # Update the code for displaying
            line_number = 0
            code = ""
            for i in ENCODED_FILE:
                line_number += 1
                code += f"{number(line_number)}{i}\n"

            # Print the instructions and code
            print(termcolor.colored("Commands available", "cyan", attrs=["underline"]))
            total_text = f"{text_1}, {text_2}, {text_3}, {text_4}, {text_5}, {text_6}, {text_7}, {text_8}\n\n{code}\n"
            print(total_text)

            # Ask the command
            move = input(f"Enter the command from the list above {termcolor.colored('[ENTER] to exit', 'grey')}: ")
            if move == "":
                # Break the loop will exit the program
                break
            
            quantity = input(f"Enter the quantity [e.g. steps, degrees] relating to the command selected {termcolor.colored('[ENTER] to exit', 'grey')}: ")
            if quantity == "":
                # Break the loop will exit the program
                break
            
            # Edit the file
            total_move = move + "," + quantity
            edit_file(total_move)

            os.system("cls")

        continue

    elif command == "3":
        os.system("cls")
        termcolor.cprint("File settings", "blue", attrs=["underline"])
        text_1 = termcolor.colored("Open file [o]", "yellow")
        text_2 = termcolor.colored("Save file [s]", "yellow")

        while True:
            sub_command = input(f"{neutral}Enter command here {text_1}, {text_2} {termcolor.colored('[ENTER] to exit', 'grey')}: ")
            print()

            if (sub_command == "o") or (sub_command == "open"):
                result = open_file()
                
                # Check if None was returned (which means that the user did not select a file)
                if result == None:
                    print(negative + "Declining operation...\n")
                
                else:
                    print(positive + "File opened successfully.\n")
                
            elif (sub_command == "s") or (sub_command == "save"):
                result = save_file()
                
                # Check if the result is None
                if result == None:
                    print(negative + "Declining operation...\n")
                    
                else:
                    print(positive + "File saved successfully.\n")

            elif sub_command == "":
                break
            
            else:
                print(negative + "Invalid command!\n")
    
    continue