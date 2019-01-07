#!/usr/bin/env python3

"""Useful Information.

Collection of useful information.
"""


class Conversions:
    """Conversion Tables."""

    conversion_value = {
        'base': 1.0,
        'milli': 0.001,
        'centi': 0.01,
        'deci': 0.1,
        'deca': 10.0,
        'hecto': 100.0,
        'kilo': 1000.0,
    }

    conversion_abbreviations = {
        'base': 1.0,
        'milli': 0.001,
        'centi': 0.01,
        'deci': 0.1,
        'deca': 10.0,
        'hecto': 100.0,
        'kilo': 1000.0,
    }


class Length(Conversions):
    """Length Conversions."""

    length = {
        'meter': 1.0,
        'millimeter': 0.001,
        'centimeter': 0.01,
        'decimeter': 0.1,
        'decameter': 10.0,
        'hectometer': 100.0,
        'kilometer': 1000.0,
    }

    abbreviations = {
        'meter': 'm',
        'millimeter': 'mm',
        'centimeter': 'cm',
        'decimeter': 'dm',
        'decameter': 'dkm',
        'hectometer': 'hm',
        'kilometer': 'km',
    }


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
    print(Capacity.capacity)
    print(Length.length)
    print(Weight.weight)
