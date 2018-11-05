#!/usr/bin/env python3

"""Digital Mistakes kata.

Correct the mistakes of the character recognition software.

Share this kata:
Character recognition software is widely used to digitize printed texts.
Thus the texts can be edited, searched and stored on a computer.

When documents (especially pretty old ones written with a typewriter), are
digitized character recognition softwares often make mistakes.

Your task is correct the errors in the digitized text.

You only have to handle the following mistakes:

* S is misinterpreted as 5
* O is misinterpreted as 0
* I is misinterpreted as 1
"""


import re


class Corrections:
    """Corrections Class."""

    corrections_map = {
        '5': 'S',
        '0': 'O',
        '1': 'I',
    }

    @classmethod
    def correct(self, word: str) -> str:
        """Correct the mistakes of the character recognition software.

        :return: String of the corrected word.
        """
        for k, v in self.corrections_map.items():
            word = re.sub(k, v, word)
        return word


def main():
    """Correct Mistakes Main function."""
    word_list = ['0UTD00R5',
                 '1NL1NE',
                 '0NL1NE',
                 '1NPUT',
                 '501L',
                 '01L5', ]
    for word in word_list:
        print(Corrections.correct(word))


if __name__ == "__main__":
    main()
