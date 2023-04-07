#!/usr/bin/python
# -*- coding: utf-8 -*-

class Pitch:
    """Pitch data model. Only points with changed values are included.

    Attributes:
        ticks (list[int]): int64[]. Tick positions of the data points.
        values (list[float | None]): Semitone values of the data points. Items could be `null` only when [is_absolute] is true.
            In this case, it represents the end of the previous value's lasting.
        is_absolute (bool): True if the semitone value is absolute, otherwise it's relative to the note's key.
    """
    ticks: list[int]
    values: list[float | None]
    is_absolute: bool

    def __init__(self, ticks: list[int], values: list[float | None], is_absolute: bool):
        self.ticks = ticks
        self.values = values
        self.is_absolute = is_absolute

    def to_dict(self) -> dict:
        return {
            "ticks": self.ticks,
            "values": self.values,
            "is_absolute": self.is_absolute
        }


def load_pitch_from_dict(dict: dict) -> Pitch:
    return Pitch(
        ticks=dict["ticks"],
        values=dict["values"],
        is_absolute=dict["is_absolute"]
    )
