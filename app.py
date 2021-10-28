import database

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies.
4) Watch a movie.
5) View watched movies.
6) Exit.

Your selection:
"""
welcome = "Welcome to the watchlist app!"


# def prompt_new_entry():
#     entry_content = input("What have you learned today?")
#     entry_date = input("Enter the date: ")

#     add_entry(entry_content, entry_date)

# def view_entries(entries):
#     for entry in entries:
#         print(f"{entry[1]}\n{entry[0]}\n\n")



print(welcome)
database.create_tables()

while (user_input := input(menu)) != "6":
    if user_input == "1":
        pass
    elif user_input == "2":
        pass
    elif user_input == "3":
        pass
    elif user_input == "4":
        pass
    elif user_input == "5":
        pass
    else:
        print("Invalid option, please try again!")
