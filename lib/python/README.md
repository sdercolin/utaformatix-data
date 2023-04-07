# UtaFormatix Data in Python

[![PyPI version](https://badge.fury.io/py/utaformatix-data.svg)](https://badge.fury.io/py/utaformatix-data)

Serialization/Deserialization of [UtaFormatix Data Format](https://github.com/sdercolin/utaformatix-data) implemented in Python.

## Install

```bash
pip install utaformatix-data
```

## Example

```py

import ufdata 

# parse JSON text
jsonstr = "..." # load from somewhere
data = ufdata.load(jsonstr) # type: ufdata.UfData

# access memebers
print(data.project.tracks[0].notes[-1].lyric)

# dump to JSON text
dumped = data.dump()

# versions
print(data.format_version) # version of the data loaded
print(ufdata.get_current_data_version()) # version of the format used by current library version
```