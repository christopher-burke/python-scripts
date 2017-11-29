#!/usr/bin/python

"""Get the numbers for the superbowl box pools."""


from random import shuffle


if __name__ == "__main__":

    team1 = input("Who is the home team? ")
    team2 = input("Who is the away team? ")

    teams = {'home': team1, 'away': team2}

    away = range(0, 10)
    home = range(0, 10)

    shuffle(away)
    shuffle(home)

    home_nums = ' '.join(map(str, home))
    away_nums = ' '.join(map(str, away))

    print("{0} \tnumbers are: {1}".format(teams['home'], " ".join(home_nums)))
    print("{0} \tnumbers are: {1}".format(teams['away'], " ".join(away_nums)))
