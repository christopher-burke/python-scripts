#!/usr/bin/env python3

"""Abstract Base Class (ABC) testing."""

from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
    @abstractmethod
    def main():
        raise NotImplemented


class TestMainMissing(Base):
    pass


class TestMain(Base):

    def main(self):
        print('Main Implemented')

    def __repr__(self):
        return f'{self.__class__.__name__}()'



if __name__ == "__main__":
    tm = TestMain()
    tm.main()

    try:
        TestMainMissing()
    except TypeError as e:
        print(e)

    try:
        Base()
    except TypeError as e:
        print(e)
