movies = [{
    'name': "ex1",
    'director': "ex2",
    'year': 1337
}]
def add_movie():
    name = raw_input("Enter the movie name: ")
    director = raw_input("Enter the movie director: ")
    year = int(raw_input("Enter the movie release year: "))
    
    movies.append({
        'name': name,
        'director': director,
        'year': year
    })


def show_movies():
    for movie in movies:
        show_movie_details(movie)


def show_movie_details(movie):
    print("Name: %s" % (movie['name']))
    print("Director: %s" % (movie['director']))
    print("Release year: %s" % (movie['year']))


def find_movie():
    find_by = raw_input("What property of the movie are you looking for? ")
    looking_for = raw_input("What are you searching for? ")
    found_movies = find_by_attribute(movies, looking_for, lambda x: x[find_by])

    show_movies(found_movies)


def find_by_attribute(expected, finder):
    found = []

    for movie in movies:
        if finder[find_by] == expected:

            found.append(movie)

    return found


def menu():
    user_input = raw_input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie and 'q' to quit: ")
    
    while user_input != "q":
        if user_input == "a":
            add_movie()
        elif user_input == "l":
            show_movies()
        elif user_input == "f":
            find_movie()
        else:
            print('Unkown command-please try again.')

        user_input = raw_input(
            "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie and 'q' to quit: ")




menu()
