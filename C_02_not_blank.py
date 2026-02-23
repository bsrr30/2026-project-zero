def not_blank(question):
    """checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Im not asking. write your name, like right NOW. \n")


# main routine starts here
who = not_blank("write your name here please :): ")
print(f"Hello, {who}!")