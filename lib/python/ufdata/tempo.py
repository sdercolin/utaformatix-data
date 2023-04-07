#!/usr/bin/python
# -*- coding: utf-8 -*-

class Tempo:
    """Tempo label model.

    Attributes:
        tick_position (int): int64. Tick position of the tempo label.
        bpm (float): Tempo in beats-per-minute.
    """
    tick_position: int
    bpm: float

    def __init__(self, tick_position: int, bpm: float):
        self.tick_position = tick_position
        self.bpm = bpm

    def to_dict(self) -> dict:
        return {
            "tick_position": self.tick_position,
            "bpm": self.bpm
        }


def load_tempo_from_dict(dict: dict) -> Tempo:
    return Tempo(
        tick_position=dict["tick_position"],
        bpm=dict["bpm"]
    )
