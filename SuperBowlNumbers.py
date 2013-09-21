#!/usr/bin/python

'''

    Get the numbers for the superbowl box pools.

'''

__author__ = "Christopher James Burke"
__copyright__ = ""
__credits__ = ["Christopher James Burke"]
__license__ = ""
__version__ = "1.0.0"
__maintainer__ = "Christopher James Burke"
__email__ = "christopherjamesburke@gmail.com"
__status__ = "Production" # __status__  one of "Prototype", "Development", or "Production"
__date__ = "2013/05/24 21:57:32"


from random import shuffle


if __name__ == "__main__":

    team1 = raw_input("Who is the home team? ")
    team2 = raw_input("Who is the away team? ")
    
    teams = {'home':team1,'away': team2}
    
    away  =   range(0,10)
    home  =   range(0,10)
    
    shuffle(away)
    shuffle(home)
    
    home_nums = ' '.join(map(str, home))
    away_nums = ' '.join(map(str, away))
    
    print ("{0} \tnumbers are: {1}".format(teams['home']," ".join(home_nums)))
    print ("{0} \tnumbers are: {1}".format(teams['away']," ".join(away_nums)))