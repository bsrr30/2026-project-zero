# function go here
def yes_no(question):
    """make sure user enters yes / no"""

    while True:

        # ask user a yes / no question
        response = input(question).lower()

        # return response if it's valid, show an error if it's not
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")


# Main routine goes here
want_instructions = yes_no("Do you want to read the instructions? ")
print(f"You chose {want_instructions}")