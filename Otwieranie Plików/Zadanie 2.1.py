# Program to write movie details to a text file

# Variables containing movie details
movie_title = "Inception"
director = "Christopher Nolan"
lead_actor = "Leonardo DiCaprio"

# Writing movie details to the file
with open("C:/Users/tomza/Desktop/Programowanie/Python/Otwieranie Plików/movie_details.txt", 'a') as file:
   file.write(f"Movie Title: {movie_title}\n")
   file.write(f"Director: {director}\n")
   file.write(f"Lead Actor: {lead_actor}\n")

print(f"Movie details have been written to file.")