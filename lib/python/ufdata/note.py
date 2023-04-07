#!/usr/bin/python
# -*- coding: utf-8 -*-

class Note:
    """Note model.

    Attributes:
        key (int): int32. Semitone value of the note's key (Center C = 60).
        tick_on (int): int64. Tick position of the note's start.
        tick_off (int): int64. Tick position of the note's end.
        lyric (str): Lyric of the note.
        phoneme (str | None): Phoneme of the note (if available).
    """
    key: int
    tick_on: int
    tick_off: int
    lyric: str
    phoneme: str | None

    def __init__(self, key: int, tick_on: int, tick_off: int, lyric: str, phoneme: str | None):
        self.key = key
        self.tick_on = tick_on
        self.tick_off = tick_off
        self.lyric = lyric
        self.phoneme = phoneme

    def to_dict(self) -> dict:
        return {
            "key": self.key,
            "tick_on": self.tick_on,
            "tick_off": self.tick_off,
            "lyric": self.lyric,
            "phoneme": self.phoneme
        }


def load_note_from_dict(dict: dict) -> Note:
    return Note(
        key=dict["key"],
        tick_on=dict["tick_on"],
        tick_off=dict["tick_off"],
        lyric=dict["lyric"],
        phoneme=dict["phoneme"] if "phoneme" in dict else None
    )
