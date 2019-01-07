#!/usr/bin/env python3

"""Useful Information.

Collection of useful information.
"""

from copy import copy


class Conversions:
    """Conversion Tables."""

    conversion_values = (
        ('milli', 0.001,),
        ('centi', 0.01,),
        ('deci', 0.1,),
        ('deca', 10.0,),
        ('hecto', 100.0,),
        ('kilo', 1000.0,),
    )

    conversion_abbreviations = (
        ('milli', 'm',),
        ('centi', 'c',),
        ('deci', 'd',),
        ('deca', 'dk',),
        ('hecto', 'h',),
        ('kilo', 'k',),
    )


class Length(Conversions):
    """Length Conversions."""

    def __init__(self):
        measurement = 'meter'
        conversion_values = super().conversion_values
        length = {}
        for key, value in conversion_values:
            length[f'{key}{measurement}'] = value

        length[measurement] = 1.0
        self.length = length

        conversion_abbreviations = super().conversion_abbreviations
        abbreviations = {}
        for key, value in conversion_abbreviations:
            abbreviations[f'{key}{measurement}'] = value + 'm'

        abbreviations[measurement] = 'm'
        self.abbreviations = abbreviations


class Capacity(Conversions):
    """Capcity Conversions."""

    capacity = {
        'liter': 1.0,
        'milliliter': 0.001,
        'centiliter': 0.01,
        'deciliter': 0.1,
        'decaliter': 10.0,
        'hectoliter': 100.0,
        'kiloliter': 1000.0,
    }

    abbreviations = {
        'liter': 'l',
        'milliliter': 'ml',
        'centiliter': 'cl',
        'deciliter': 'dl',
        'decaliter': 'dkl',
        'hectoliter': 'hl',
        'kiloliter': 'kl',
    }


class Weight(Conversions):
    """Weight Conversions."""

    weight = {
        'gram': 1.0,
        'milligram': 0.001,
        'centigram': 0.01,
        'decigram': 0.1,
        'decagram': 10.0,
        'hectogram': 100.0,
        'kilogram': 1000.0,
    }
    abbreviations = {
        'gram': 'g',
        'milligram': 'mg',
        'centigram': 'cg',
        'decigram': 'dg',
        'decagram': 'dkg',
        'hectogram': 'hg',
        'kilogram': 'kg',
    }


if __name__ == "__main__":
    # print(Capacity.capacity)
    # print(Length.length)

    l = Length()
    print(l.length)
    print(l.abbreviations)
    # print(Weight.weight)
