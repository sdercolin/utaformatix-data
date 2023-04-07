#!/usr/bin/python
# -*- coding: utf-8 -*-

from .track import Track, load_track_from_dict
from .time_signature import TimeSignature, load_time_signature_from_dict
from .tempo import Tempo, load_tempo_from_dict


class Project:
    """Project model.

    Attributes:
        name (str): Project name.
        tracks (list[Track]): List of track models in the project.
        time_signatures (list[TimeSignature]): List of time signatures in the project.
        tempos (list[Tempo]): List of tempo labels in the project.
        measure_prefix (int): Count of measure prefixes (measures that cannot contain notes, restricted by some editors).
    """
    name: str
    tracks: list[Track]
    time_signatures: list[TimeSignature]
    tempos: list[Tempo]
    measure_prefix: int

    def __init__(self, name: str, tracks: list[Track], time_signatures: list[TimeSignature], tempos: list[Tempo], measure_prefix: int):
        self.name = name
        self.tracks = tracks
        self.time_signatures = time_signatures
        self.tempos = tempos
        self.measure_prefix = measure_prefix

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "tracks": [track.to_dict() for track in self.tracks],
            "time_signatures": [time_signature.to_dict() for time_signature in self.time_signatures],
            "tempos": [tempo.to_dict() for tempo in self.tempos],
            "measure_prefix": self.measure_prefix
        }


def load_project_from_dict(dict: dict) -> Project:
    return Project(
        name=dict["name"],
        tracks=[load_track_from_dict(track) for track in dict["tracks"]],
        time_signatures=[load_time_signature_from_dict(
            time_signature) for time_signature in dict["time_signatures"]],
        tempos=[load_tempo_from_dict(tempo) for tempo in dict["tempos"]],
        measure_prefix=dict["measure_prefix"]
    )
