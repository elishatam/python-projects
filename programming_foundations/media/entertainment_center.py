import media
import fresh_tomatoes

#define instances of Class Movie
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4") #media = name of Python file. Movie = name of the class defined in file
                          # calls the init function. Self = toy_story
# print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=6ziBFh3V1aM")
#print(avatar.storyline)
#avatar.show_trailer()

lion_king = media.Movie("Lion King",
                        "The life of a young cub",
                        "https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",
                        "https://www.youtube.com/watch?v=4sj1MT05lAA")
# lion_king.show_trailer()

wonder_woman = media.Movie("Wonder Woman",
                           "Superhero stops villain from chemical attack to stop WW1",
                           "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",
                           "https://www.youtube.com/watch?v=1Q8fG0TtVAY")

fried_green_tomatoes = media.Movie("Fried Green Tomatoes",
                                   "Tells the story of a Depression-era friendship between two women",
                                   "https://upload.wikimedia.org/wikipedia/en/6/6e/Fried_Green_Tomatoes_%28poster%29.jpg",
                                   "https://www.youtube.com/watch?v=T2W0TeuHbJ0")

forrest_gump = media.Movie("Forrest Gump",
                           "Follows several decades of a slow-witted, but kind-hearted man from Alabama",
                           "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
                           "https://www.youtube.com/watch?v=bLvqoHBptjg")

movies = [toy_story, avatar, lion_king, wonder_woman, fried_green_tomatoes, forrest_gump]
# fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__) #Documentation of class
print(media.Movie.__name__) #Name of class
print(media.Movie.__module__) #Name of file module