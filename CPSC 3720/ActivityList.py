#Activities List
import random

def Activites(weather):
#Arrays/Lists contian weather terms
    hot_weather = ["hot", "dust", "dustn", "smoke", "smoken", "sunny", "sunnyn", "sunnyw", "sunnywn"]
    good_weather = ["clear","fair", "clearn", "fairn", "hazy", "hazyn", "pcloudy", "pcloudyn", "sunny", "sunnyw", "wind", "windn"]
    rainy_weather = ["rain", "rainandsnow", "showers", "showersw", "wintrymix", "snowtorain","rainn", "rainandsnown", "showersn", "showerswn", "wintrymixn", "snowtorainn", "pcloudyr", "pcloudyrn", "pcloudyrw", "pcloudyrwn"],
    snowy_weather = ["blizzard","blowingsnow", "blizzardn", "blowingsnown", "sleet", "sleetn", "pcloudys", "pcloudysn"],
    stormy_weather = ["tstorm","tstorms", "tstormsw","tstormn", "tstormsn", "tstormswn"],
   
    # String Compare passed in weather to lists
    if(weather in hot_weather):
        #HotWeather act  (swim, pool, lake, beach)
        hot_weather_acts = ["Go for a Swim", "Locate (nearest) Icecream", "Stand infront of A/C"]
        pass
    if(weather in good_weather):
        #good weather (go for a walk, run, park, picnic, bike, rip some kickball) acts
        good_weather_acts = ["Go for a Walk", "Go for a Run", "Go to the Park", "Go on a Picnic", "Go for a Bike Ride", "Play some Outdoor Sports"]
        pass
    if(weather in rainy_weather):
        #rainy weather acts (go to gym, go see a movie, go shopping, do a puzzle, read a book, video games)
        good_rainy_acts = ["Go to the Gym", "Go See a Movie", "Go Shopping", "Do a Puzzle", "Read a Book", "Play a Video Game"]
        pass
    if(weather in snowy_weather):
        good_snowy_acts = ["Go Sledding", "Have Hot-Coco", "Build a Snowman", "Have a Snowball Fight", "Go Skiing","Go Snowboarding"]
        #snowy weather acts (sledding, build a snowman, ski, sled)(Building Snow man Snowball fights Snowboard)
        pass
    if(weather in stormy_weather):
        stormy_weather_acts = ["Read a book", "Watch a Movie", "Do a Puzzle", "Play a Video Game","Bake Cookies"]
        #stormy weather acts (go see a movie, go shopping, do a puzzle, read a book, video games) 
        # (Reading book at home Playing board games at home Watching movies/TV shows at home Bake cookies

        pass
    