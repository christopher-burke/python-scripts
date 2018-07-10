#!/usr/bin/python

"""NFL Quarterback Rating."""


class Nfl_Qb_Rating(object):
    """Nfl_Qb_Rating class."""

    def __init__(self, com=0, att=0, yds=0, tds=0, ints=0):
        """Quaterback Object to calculate the NFL QB Rating.

        Arguments:
                com  = Completed Passes
                att  = Attempted Passes
                yds  = Passing Yards
                tds  = TD Passes
                ints = Interceptions

        Usage:
                Nfl_Qb_Rating( com, att, yds, tds, ints )

        """
        if att > 0:
            self.completion_percentage = ((com / att))
            self.yards_per_attempt = ((yds / att))
            self.tds_per_attempt = ((tds / att))
            self.ints_per_attempt = ((ints / att))
        else:
            (	self.completion_percentage,
              self.yards_per_attempt,
              self.tds_per_attempt,
              self.ints_per_attempt) = 0, 0, 0, 0
        self.com = com
        self.att = att
        self.yds = yds
        self.tds = tds
        self.ints = ints

    def stat(self, stat):
        """Quaterback Object to calculate NFL QB Rating.

        Arguments:
                com  = Completed Passes
                att  = Attempted Passes
                yds  = Passing Yards
                tds  = TD Passes
                ints = Interceptions
                completion_percentage = Completion Percentage
                yards_per_attempt = Yards per Attempt
                tds_per_attempt = TDs per Attempt
                ints_per_attempt = Interceptions per Attempt

        Usage:
                Nfl_Qb_Rating(324,461,3969,35,10).stat( ints ) => 10
        """
        data = self.__dict__.get(stat.lower())
        if data:
            return data
        else:
            return "%s stat not found." % (stat.capitalize())

    def qb_rating(self):
        """Calculate and return the NFL QB rating."""
        qbr_one = (self.completion_percentage - 0.3) / (0.2)
        qbr_two = ((self.yards_per_attempt) - 3.0) / (4.0)
        qbr_three = (((self.tds_per_attempt)) / (0.05))
        qbr_four = ((0.095 - self.ints_per_attempt)) / (.04)

        # Rules one and two values between 2.375 and 0
        def rule_one_two(x): return 2.375 if x > 2.375 else 0 if x < 0 else x
        # Rule three has a max of 2.375

        def rule_three(x): return 2.375 if x > 2.375 else x
        # Rule four has a min of 0

        def rule_four(x): return 0 if x < 0 else x

        # Apply the rules to the four qbr parts.
        (qbr_one, qbr_two) = (map(rule_one_two, (qbr_one, qbr_two,)))
        (qbr_three) = rule_three(qbr_three)
        (qbr_four) = rule_four(qbr_four)

        return "%0.1f" % (((	qbr_one
                             + qbr_two
                             + qbr_three
                             + qbr_four) * 100) / 6.0)


if __name__ == "__main__":
    # Steve Young 1994 season test.
    x = Nfl_Qb_Rating(324, 461, 3969, 35, 10)
    qbrating = x.qb_rating()
    print("QB Rating", qbrating)
    print("TDs", x.stat('TDS'))
    print("INTs", x.stat('INTS'))
