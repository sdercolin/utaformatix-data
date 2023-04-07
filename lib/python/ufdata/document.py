#!/usr/bin/python
# -*- coding: utf-8 -*-

import humps
import json
from .project import Project, load_project_from_dict


class UfData:
    """UtaFormatix Data Document (root model).
    format_version (int): The version of the format.
    project (Project): Content of the project.
    """
    format_version: int
    project: Project

    def __init__(self, format_version: int, project: Project):
        self.format_version = format_version
        self.project = project

    def to_dict(self) -> dict:
        return {
            "format_version": self.format_version,
            "project": self.project.to_dict()
        }

    def dump(self) -> str:
        """Dump the UtaFormatix Data Document to JSON.
        Returns:
            str: The JSON string.
        """
        return json.dumps(humps.camelize(self.to_dict()), ensure_ascii=False)


def get_current_data_version() -> int:
    """Get the current version of the UtaFormatix Data Document format.
    Returns:
        int: The current version.
    """
    return 1


def load_ufdata_from_dict(data: dict) -> UfData:
    return UfData(
        format_version=data["format_version"],
        project=load_project_from_dict(data["project"])
    )


def load(text: str) -> UfData:
    """Load a UtaFormatix Data Document from JSON.
    Args:
        data (str): The JSON string.
    Returns:
        UfData: The UtaFormatix Data Document.
    """
    return load_ufdata_from_dict(humps.decamelize(json.loads(text)))
