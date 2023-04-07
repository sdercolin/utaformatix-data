#!/usr/bin/python
# -*- coding: utf-8 -*-

class TimeSignature:
    """Time signature model.

    Attributes:
        measure_position(int): int32. Measure (bar) position of the time signature.
        numerator(int): int32. Beats per measure.
        denominator(int): int32. Note value per beat.
    """
    measure_position: int
    numerator: int
    denominator: int

    def __init__(self, measure_position: int, numerator: int, denominator: int):
        self.measure_position = measure_position
        self.numerator = numerator
        self.denominator = denominator

    def to_dict(self) -> dict:
        return {
            "measure_position": self.measure_position,
            "numerator": self.numerator,
            "denominator": self.denominator
        }


def load_time_signature_from_dict(dict: dict) -> TimeSignature:
    return TimeSignature(
        measure_position=dict["measure_position"],
        numerator=dict["numerator"],
        denominator=dict["denominator"]
    )
