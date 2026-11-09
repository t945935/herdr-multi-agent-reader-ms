"""Bab 1: kontrak ringkas untuk latihan pembangunan dan semakan."""

from math import isfinite


def _number(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("Nilai mesti angka; bool tidak diterima")
    if not isfinite(value):
        raise ValueError("Nilai mesti terhingga")
    return value


def add(a, b):
    return _number(a) + _number(b)


def subtract(a, b):
    return _number(a) - _number(b)


def multiply(a, b):
    return _number(a) * _number(b)


def divide(a, b):
    a, b = _number(a), _number(b)
    if b == 0:
        raise ZeroDivisionError("Tidak boleh membahagi dengan sifar")
    return a / b
