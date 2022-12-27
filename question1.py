def name_display(firstname,lastname):
    display = f'"{firstname[:1]}.{lastname[:1]}", "{firstname} {lastname}","{firstname[:1]}{lastname}"'
    return display

def main():
    firstname= input("Enter your first name:")
    lastname = input("Enter your last name:")

    final_display = name_display(firstname,lastname)


    print(final_display)


main()

