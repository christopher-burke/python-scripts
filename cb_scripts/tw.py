#!/usr/bin/env python3

"""Wrapper for textwrap module.

Working with the textwrap module and creating a wrapper that includes
all functionality while keeping the original text.
"""

from textwrap import TextWrapper, dedent, indent

GLOBAL_LEN = 72


class MyTextWrapper:
    """My wrapper for the textwrap.TextWrapper class."""

    def __init__(self, text, width=GLOBAL_LEN):
        self.text = text
        self.width = width
        self.tw = TextWrapper(width=width)

    def _renew(self, **kwargs):
        self.tw = TextWrapper(**kwargs)

    def _fill(self, word_list):
        return "\n".join(word_list)

    def wrap(self, width=GLOBAL_LEN, as_string=True, shorten=False):
        """Return a string/list of wrapped text."""

        if shorten:
            self.max_lines = 1
            shorten_text = ' '.join(self.text.strip().split())
        else:
            self.max_lines = None
            shorten_text = None

        if width != self.width or bool(self.max_lines) is shorten:
            self.width = width
            self._renew(**{'width': self.width, 'max_lines': self.max_lines})

        text = shorten_text if shorten_text else self.text

        word_list = self.tw.wrap(text=text)
        if as_string is True:
            return self._fill(word_list)
        else:
            return word_list
        raise ValueError("as_string value error!")

    def shorten(self, width=GLOBAL_LEN):
        """Shorten the original text."""
        return self.wrap(width=width, as_string=True, shorten=True)

    def dedent(self):
        """Remove leading whitespace from every line."""
        return dedent(self.text)

    def indent(self, prefix, predicate=None, dedent=False):
        """Add a prefix to each line of text."""
        if dedent:
            return indent(self.dedent(), prefix=prefix, predicate=predicate)
        return indent(self.text, prefix=prefix, predicate=predicate)

    def __repr__(self):
        """__repr__ of MyTextWrapper."""
        self.__class__.__name__
        return f"{self.__class__.__name__}('''{self.text}''')"

    def __str__(self):
        """__str__ of MyTextWrapper."""
        return self.wrap()


if __name__ == "__main__":
    # From Macbeth
    text = """Tomorrow, and tomorrow, and tomorrow,
            Creeps in this petty pace from day to day,
            To the last syllable of recorded time;
            And all our yesterdays have lighted fools
            The way to dusty death. Out, out, brief candle!
            Life's but a walking shadow, a poor player,
            That struts and frets his hour upon the stage,
            And then is heard no more. It is a tale
            Told by an idiot, full of sound and fury,
            Signifying nothing.
            """

    # Print to console.
    tw = MyTextWrapper(text=text)

    print(tw.wrap())
    print(tw.wrap(width=20))
    print(tw.wrap(width=20, as_string=False))
    print(tw.wrap(width=GLOBAL_LEN, as_string=True, shorten=True))

    print(tw.indent(prefix="+  "))
    print(tw.indent(prefix="+  ", dedent=True))
    tw.text = tw.dedent()
    print(tw.dedent())
    print(tw.wrap())
    print()
    print(tw.wrap(shorten=True))
