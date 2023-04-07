#!/usr/bin/python
# -*- coding: utf-8 -*-

from .note import Note, load_note_from_dict
from .pitch import Pitch, load_pitch_from_dict


class Track:
    """Track model.

    Attributes:
        name (str): Track name.
        notes (list[Note]): Notes in the track.
        pitch (Pitch | None): Pitch data bound to the track (if any).
    """
    name: str
    notes: list[Note]
    pitch: Pitch | None

    def __init__(self, name: str, notes: list[Note], pitch: Pitch | None):
        self.name = name
        self.notes = notes
        self.pitch = pitch

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "notes": [note.to_dict() for note in self.notes],
            "pitch": self.pitch.to_dict() if self.pitch is not None else None
        }


def load_track_from_dict(dict: dict) -> Track:
    return Track(
        name=dict["name"],
        notes=[load_note_from_dict(note) for note in dict["notes"]],
        pitch=load_pitch_from_dict(dict["pitch"]) if "pitch" in dict else None
    )
