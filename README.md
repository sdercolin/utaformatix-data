# UtaFormatix Data (.ufdata)

Common data container for singing synthesis softwares used by [UtaFormatix](https://github.com/sdercolin/utaformatix3).

## Language-specific interfaces

- [Kotlin Multiplatform](./lib/kotlin-mpp): Kotlin implementation for Jvm/JavaScript/Native

## Data structure

The data is stored in JSON with file extension `.ufdata`.

### Sample

```json
{
  "formatVersion": 1,
  "project": {
    "name": "project name",
    "tracks": [
      {
        "name": "track 1",
        "notes": [
          {
            "key": 60,
            "tickOn": 1920,
            "tickOff": 2400,
            "lyric": "あ",
            "phoneme": "a"
          },
          {
            "key": 61,
            "tickOn": 2400,
            "tickOff": 2880,
            "lyric": "い",
            "phoneme": null
          }
        ],
        "pitch": {
          "ticks": [
            1920,
            1925,
            1930
          ],
          "values": [
            62.8,
            null,
            62.90257538448604
          ],
          "isAbsolute": true
        }
      },
      {
        "name": "track 2",
        "notes": [
          {
            "key": 60,
            "tickOn": 1920,
            "tickOff": 2400,
            "lyric": "あ",
            "phoneme": "a"
          }
        ]
      }
    ],
    "timeSignatures": [
      {
        "measurePosition": 0,
        "numerator": 4,
        "denominator": 4
      }
    ],
    "tempos": [
      {
        "tickPosition": 0,
        "bpm": 118
      }
    ],
    "measurePrefix": 0
  }
}
```

### Root (Document) object

| Variable name | Description                              | Type   | 
|---------------|------------------------------------------|--------|
| formatVersion | The version code of the ufdata structure | int32  |
| project       | The [project](#project-object) content   | object |

### Project object

| Variable name  | Description                                                                                | Type           |
|----------------|--------------------------------------------------------------------------------------------|----------------|
| name           | Project name                                                                               | string         |
| tracks         | [Track](#track-object) list                                                                | array\<object> |
| timeSignatures | [Time signature](#time-signature-object)s                                                  | array\<object> |
| tempos         | [Tempo](#tempo-object) changes                                                             | array\<object> |
| measurePrefix  | Count of measure prefixes (measures that cannot contain notes, restricted by some editors) | int32          |

### Track object

| Variable name | Description                 | Type            | 
|---------------|-----------------------------|-----------------|
| name          | Track name                  | string          |
| notes         | [Note](#note-object) list   | array\<object>  |
| pitch         | [Pitch](#pitch-object) data | nullable object |

### Note object

| Variable name | Description                                      | Type   |
|---------------|--------------------------------------------------|--------|
| key           | Semitone value of the note's key (Center C = 60) | int32  |
| tickOn        | Tick position of the note's start                | int64  |
| tickOff       | Tick position of the note's end                  | int64  |
| lyric         | Lyric                                            | string |
| phoneme       | Phoneme (if available)                           | string |

### Pitch object

Only points with changed values are included.

| Variable name | Description                                                                                                                                                    | Type           |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| ticks         | Tick positions of the data points                                                                                                                              | array\<int64>  |
| values        | Semitone values of the data points. Items could be `null` only when `isAbsolute` is true. In this case, it represents the end of the previous value's lasting. | array\<double> |
| isAbsolute    | Whether the pitch values are absolute or relative to the note's key                                                                                            | bool           |

### Time signature object

| Variable name   | Description                                  | Type  |
|-----------------|----------------------------------------------|-------|
| measurePosition | Measure (bar) position of the time signature | int32 |
| numerator       | Beats per measure                            | int32 |
| denominator     | Note value per beat                          | int32 |

### Tempo object

| Variable name | Description                       | Type  |
|---------------|-----------------------------------|-------|
| tickPosition  | Tick position of the tempo change | int64 |
| bpm           | Tempo in beats-per-minute         | int32 |
