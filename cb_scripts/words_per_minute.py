#!/usr/bin/env python3

"""Calculate the words per minute of text."""


import re
from math import ceil


class ReadingTime:
    """Class to calulate the reading time of text.

    The reading time is calulated based on
    words per minute and average word length.
    """

    def __init__(self, text: str, words_per_minute: int, word_length: int):
        self.text = text
        self.words_per_minute = words_per_minute
        self.word_length = word_length

    def word_count(self):
        """Calculate the average number of words.

        Find all the letters and divide by average word length to get count.
        """
        letters = len(re.compile(r"\w", re.I).findall(self.text))
        self.count = letters / self.word_length
        print(self.count)
        return self.count

    def reading_time(self):
        """Calculate the reading time.

        Round up to the neartest whole number
        """
        return ceil(self.count / self.words_per_minute)
