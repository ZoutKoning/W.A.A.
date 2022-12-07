#Activities List
# Joesph Suter,  Tirth Patel
import random

def Activites(weatherIcon):
#Arrays/Lists contian weather terms
    hot_dry_weather = ["dust.png", "dustn.png", "hot.png"]
    good_weather = ["clear.png", "clearn.png", "clearw.png", "clearwn.png", "cloudy.png", "cloudyn.png", "fair.png", "fairn.png",
                    "flurries.png", "flurriesn.png", "hazy.png", "hazyn.png", "mcloudy.png", 'mcloudyn.png', "pcloudy.png",
                    "pcloudyn.png", "sunny.png", "sunnyn.png", "sunnyw.png", "sunnywn.png", "wind.png", "windn.png"]
    cold_weather = ["cloudyw.png", "cloudywn.png", "cold.png", "coldn.png", "flurriesw.png", "flurrieswn.png", 
                    "mcloudyw.png", "mcloudywn.png", "pcloudyw.png", "pcloudywn.png"]
    rainy_weather = ["drizzle.png", "drizzlef.png", "drizzlen.png", "fdrizzle.png", "fdrizzlen.png", "fog.png", "fogn.png",
                     "freezingrain.png", "freezingrainn.png", "mcloudyr.png", "mcloudyrn.png", "mcloudyrw.png", "mcloudrwn.png",
                     "pcloudyr.png", "pcloudyrn.png", "pcloudyrw.png", "pcloudyrwn.png", "rain.png", "rainn.png", 
                     "rainandsnow.png", "rainandsnown.png", "raintosnow.png", "raintosnown.png", "rainw.png",
                     "showers.png", "showersn.png", "showersw.png", "showerswn.png", "wintrymix.png", "wintrymixn.png"]
    snowy_weather = ["blizzard.png", "blizzardn.png", "blowingsnow.png", "blowingsnown.png","mcloudys.png", "mcloudysn.png",
                     "mcloudysf.png", "mcloudysfn.png", "mcloudysfw.png", "mcloudysfwn.png", "mcloudysw.png", "mcloudswn.png",
                     "pcloudys.png", "pcloudysn.png", "pcloudysf.png", "pcloudysfn.png", "pcloudysfw.png", "pcloudrsfwn.png",
                     "pcloudysw.png", "pcloudyswn.png", "sleet.png", "sleetn.png", "sleetsnow.png", "sleetsnown.png", 
                     "snow.png", "snown.png", "snowshowers.png", "snowshowersn.png", "snowshowersw.png", "snowshowerswn.png",
                     "snowtorain.png", "snowtorainn.png", "snoww.png", "snowwn.png"]
    stormy_weather = ["mcloudyt.png", "mcloudytn.png", "mcloudytw.png", "mcloudytwn.png", "pcloudyt.png", "pcloudytn.png",
                      "pcloudytw.png", "pcloudytwn.png", "tstorm.png", "tstormn.png", "tstorms.png", "tstormsn.png",
                      "tstormsw.png", "tstormswn.png"]
    na_weather = ["na.png", "smoke.png", "smoken.png"]
    
    # Variable to call for the GUI to get the returns 
    ret_act = ""
    # String Compare passed in weather to lists
    if(weatherIcon in hot_dry_weather):
        #HotWeather act  (swim, pool, lake, beach)...
        hot_weather_acts = ["Go for a Swim", "Locate (nearest) Icecream place and hace some icecream", "Stand infront of A/C"]
        
        ret_act = random.choice(hot_weather_acts)
        return ret_act
    
    elif(weatherIcon in good_weather):
        #good weather (go for a walk, run, park, picnic, bike, rip some kickball)...
        good_weather_acts = ["Go for a Walk", "Go for a Run", "Go to the Park", "Go on a Picnic", "Go for a Bike Ride", "Play some Outdoor Sports"]
        
        ret_act = random.choice(good_weather_acts)
        return ret_act
    
    elif(weatherIcon in cold_weather):
        #good weather (go for a walk, run, park, picnic, bike, rip some kickball)...
        cold_weather_acts = ["Have Bonfire and eat some marshmellow", "Have Hot-Coco", "Have a movie night at home"]
        
        ret_act = random.choice(cold_weather_acts)
        return ret_act
    
    elif(weatherIcon in rainy_weather):
        #rainy weather acts (go to gym, go see a movie, go shopping, do a puzzle, read a book, video games)...
        good_rainy_acts = ["Go to the Gym", "Go See a Movie", "Go Shopping", "Do a Puzzle", "Read a Book", "Play a Video Game"]
        
        #Replace pass with the return value
        ret_act = random.choice(good_rainy_acts)
        return ret_act
    
    elif(weatherIcon in snowy_weather):
        #snowy weather acts (sledding, build a snowman, ski, sled)(Building Snow man Snowball fights Snowboard)...
        good_snowy_acts = ["Go Sledding", "Have Hot-Coco", "Build a Snowman", "Have a Snowball Fight", "Go Skiing","Go Snowboarding"]
        
        ret_act = random.choice(good_snowy_acts)
        return ret_act
    
    elif(weatherIcon in stormy_weather):
        #stormy weather acts
        stormy_weather_acts = ["Read a book", "Watch a Movie at home", "Do a Puzzle", "Play a Video Game", "Bake Cookies"]
        
        ret_act = random.choice(stormy_weather_acts)
        return ret_act
    
    elif(weatherIcon in na_weather):
        # NA weather acts
        na_weather_acts = ["For once, decide yourself what activity would you like to do. :) "]
        
        ret_act = random.choice(na_weather_acts)
        return ret_act
    
    else:
        ret_act = "Exception while deciding on activity based on weather.\n"
        ret_act = ret_act + "Please try again later or choose an activity yourself based on the weather"
        return ret_act

