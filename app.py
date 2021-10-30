import database
import prompt_data

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies.
4) Watch a movie.
5) View watched movies.
6) Add user to the app.
7) Search for a movie.
8) Exit.


Your selection:
"""
welcome = "Welcome to the watchlist app!"

print(welcome)
database.create_tables()


while (user_input := input(menu)) != "8":
    if user_input == "1":
        prompt_data.prompt_add_movie()
    elif user_input == "2":
        movies = database.get_movies(True)
        prompt_data.print_movie_list("Upcoming", movies)
    elif user_input == "3":
        movies = database.get_movies()
        prompt_data.print_movie_list("All", movies)
    elif user_input == "4":
        #TODO: modify inserting movies to watched table to check if user exists - if not - add user to the users, then add movie to watched table
        prompt_data.prompt_watch_movie()
    elif user_input == "5":
        prompt_data.prompt_show_watched_movies()
    elif user_input == "6":
        prompt_data.prompt_add_user()
    elif user_input == "7":
        prompt_data.prompt_search_movies()
    else:
        print("Invalid option, please try again!")
