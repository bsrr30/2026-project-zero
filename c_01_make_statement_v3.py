# The functions go here from main import print_hi
def make_statement(statement, decoration, lines=1):
    """Creates headings (3 lines), subheadings (2 lines) and
    emphasized text / mini-headings (1 line).    only use emoji for
    single line statement"""

    middle = f"{decoration * 3} {statement} {decoration * 3}"
    top_bottom = decoration * len(middle)

    if lines == 1:
        print(middle)
    elif lines == 2:
        print(middle)
        print(top_bottom)

    else:
        print(top_bottom)
        print(middle)
       

#main code here
make_statement("programing is fun", "=", 3 )
print()
make_statement("it is still fun", "*", 2)
print()
make_statement("emoji in action!", "👌", 1 )


