#!/usr/bin/env python3

"""Sample of functools.singledispatch."""

from functools import singledispatch
from collections import abc
import numbers


@singledispatch  # <1>
def check(obj):
    """Check object type.

    When an object is not recoginzed, raise the NotImplementedError.
    """
    raise NotImplementedError('Unsupported type')


@check.register(str)
def _(text):
    """Single dispatch for Strings."""
    return f'{type(text)}. String single dispatch.'


@check.register(numbers.Integral)
def _(n):
    """Single dispatch for Integrals."""
    return f'{type(n)} numbers. Integral single dispatch.'


@check.register(tuple)
@check.register(abc.MutableSequence)
def _(seq):
    """Single dispatch for sequences."""
    return f'{type(seq)}.  Sequence type.'
