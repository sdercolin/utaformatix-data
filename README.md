# UtaFormatix Data (.ufdata)

Common data container for singing synthesis softwares used by [UtaFormatix](https://github.com/sdercolin/utaformatix3).

## Language-specific interfaces

- [Kotlin Multiplatform](lib/kotlin-mpp): Kotlin implementation for JVM/JavaScript/Native
- [TypeScript](lib/typescript): TypeScript definitions

## Data structure

The data is stored as JSON with file extension `.ufdata`.

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

| Variable name | Description                                                            | Type   | 
|---------------|------------------------------------------------------------------------|--------|
| formatVersion | The version code of the ufdata structure                               | int32  |
| project       | The project content. See [Project object](#project-object) for details | object |

### Project object

| Variable name  | Description                                                                                | Type           |
|----------------|--------------------------------------------------------------------------------------------|----------------|
| name           | Project name                                                                               | string         |
| tracks         | Track list. See [Track object](#track-object) for details                                  | array\<object> |
| timeSignatures | Time signatures. See [Time signature object](#time-signature-object) for details           | array\<object> |
| tempos         | Tempo changes. See [Tempo object](#tempo-object) for details                               | array\<object> |
| measurePrefix  | Count of measure prefixes (measures that cannot contain notes, restricted by some editors) | int32          |

### Track object

| Variable name | Description                                               | Type            | 
|---------------|-----------------------------------------------------------|-----------------|
| name          | Track name                                                | string          |
| notes         | Note list. See [Note object](#note-object) for details    | array\<object>  |
| pitch         | Pitch data. See [Pitch object](#pitch-object) for details | nullable object |

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

e.g. `[(1, 1.0),  (4, 3.0)]` implies ticks between (in this case, `2` and `3`) have the same value of `1.0`.

| Variable name | Description                                                                                                        | Type            |
|---------------|--------------------------------------------------------------------------------------------------------------------|-----------------|
| ticks         | Tick positions of the data points                                                                                  | array\<int64>   |
| values        | Semitone values of the data points. When `isAbsolute` is true, `null` can be included to represent default values. | array\<double?> |
| isAbsolute    | Whether the pitch values are absolute or relative to the note's key                                                | bool            |

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
