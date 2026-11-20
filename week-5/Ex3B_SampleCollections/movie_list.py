# Alizon Martinez
# 11/11/26
# Create a list

movies = [
    "Black Panther",
    "Avatar",
    "The Batman",
    "Top Gun Maverick",
    "Spider-Man"
]

print("The list movies includes my top",
      len(movies),
      "favorite movies")

print(movies)
print(sorted(movies))
print(movies)

# sorted() displays a sorted version
# but does not permanently change the list

movies.sort()

print(movies)

# sort() permanently changes the list

movies.append("Creed III")

print("The list movies includes my top",
      len(movies),
      "favorite movies")

print(movies)

