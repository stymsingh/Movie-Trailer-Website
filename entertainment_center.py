import fresh_tomatoes
import medias

toy_story = medias.Movie("Toy Story","A story of a boy and his toys that come to life"
            , "1234.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")
#self = toy_story
print(toy_story.storyline)
#toy_story.show_trailer()

avataar = medias.Movie("Avatar","A marine on an alien planet"
            , "5678.jpg","https://www.youtube.com/watch?v=cRdxXPV9GNQ")
#self = avataar
print(avataar.storyline)
#avataar.show_trailer()

shawshank_redemption = medias.Movie("Shashank redemption","A touching story on the life of two criminals"
            , "6754.jpg","https://www.youtube.com/watch?v=6hB3S9bIaco")
#self = shawshank_redemption
print(shawshank_redemption.storyline)
#shawshank_redemption .show_trailer()


fast_and_furious5 = medias.Movie("fast_and_furious5","An action packed movie!!!"
            , "9632.jpg","https://www.youtube.com/watch?v=4PspF_GA-9U")
#self = fast_and_furious5
print(fast_and_furious5.storyline)
#fast_and_furious5.show_trailer()

movies = [toy_story , avataar, shawshank_redemption ,fast_and_furious5]
#fresh_tomatoes.open_movies_page(movies)
#print(medias.Movie.VALID_RATINGS)
print(medias.Movie.__doc__)