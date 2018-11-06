#!/usr/bin/env python3


"""Indentor using context manager.

Exercise from Dan Bader's:
'Python Tricks: The Book. A Buffet of Awesome Python Features'.
"""


class Indenter:
    """Indent text with a context manager."""

    def __init__(self):
        """Create new Indenter."""
        self.level = 0

    def __enter__(self):
        """Context manager enter function."""
        self.level += 1
        return self

    def __exit__(self, *args, **kwargs):
        """Context manager exit function."""
        self.level -= 1

    def __repr__(self):
        """Indentor repr."""
        return f'{self.__class__.__name__}()'

    def __str__(self):
        """Indentor str."""
        return f'{self.level}'

    def print_text(self, text):
        """Print the text at the current level."""
        print(f'{self.level * "    "}{text}')

    def return_text(self, text):
        """Return the text at the current level."""
        return f'{self.level * "    "}{text}'


def main():
    """Return programming quote using Indenter."""
    with Indenter() as indent:
        indent.print_text('Premature optimization, that’s like a sneeze. '
                          'Premature abstraction is like ebola; '
                          'it makes my eyes bleed.'
                          )
        with indent:
            indent.print_text('— Christer Ericson')


if __name__ == "__main__":
    main()
