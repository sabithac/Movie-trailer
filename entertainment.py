
import fresh_tomatoes
import media

vivegam = media.Movie("VIVEGAM","A group of counter-terrorism agents are brought in to track down a man who was once the head of their squad, and is believed to have gone rogue.",
                  "https://upload.wikimedia.org/wikipedia/en/b/be/Vivegam_poster.jpg",
                  "https://www.youtube.com/watch?v=yJdHR8nCYWk")
#print(vivegam.storyline)
alien_covenant =media.Movie("ALIEN COVENANT","The crew of a colony ship, bound for a remote planet, discover an uncharted paradise with a threat beyond their imagination, and must attempt a harrowing escape",
                    "https://upload.wikimedia.org/wikipedia/en/3/33/Alien_Covenant_Teaser_Poster.jpg",
                    "https://www.youtube.com/watch?v=svnAD0TApb8")
#print(alien_covenant.storyline)
#alien_covenant.show.trailer()
xxx=media.Movie("XXX","The story of gangsters",
                        "https://upload.wikimedia.org/wikipedia/en/9/9c/Xxx_return_of_xander_cage_film_poster.jpeg",
                        "https://www.youtube.com/watch?v=MQEFmHsseaU")
jagga_jasoos=media.Movie("JAGGA JASOOS","A story of mystery and comedy adventure",
                 "https://upload.wikimedia.org/wikipedia/en/9/94/JaggaJasoosPoster.jpg",
                 "https://www.youtube.com/watch?v=YheC-4Qgoro")
sanam_teri_kasam=media.Movie("SANAM TERI KASAM","It is an romantic drama film",
                          "https://upload.wikimedia.org/wikipedia/en/7/72/Sanam_Teri_Kasam_2016.jpeg",
                          "https://www.youtube.com/watch?v=1IpBoMWRjm8")
the_beauty_and_the_beast=media.Movie("THE BEAUTY AND THE BEAST","A chemistry between the lady and the beast",
                                     "https://upload.wikimedia.org/wikipedia/en/d/d6/Beauty_and_the_Beast_2017_poster.jpg",
                                     "https://www.youtube.com/watch?v=OvW_L8sTu5E")
movies = [vivegam,alien_covenant,xxx,jagga_jasoos,sanam_teri_kasam,the_beauty_and_the_beast]
fresh_tomatoes.open_movies_page(movies)
