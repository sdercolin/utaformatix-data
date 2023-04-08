namespace UtaFormatix.Data;

/// <summary>Note model.</summary>
///
/// <param name="Key">Semitone value of the note's key (Center C = 60).</param>
/// <param name="TickOn">Tick position of the note's start.</param>
/// <param name="TickOff">Tick position of the note's end.</param>
/// <param name="Lyric">Lyric of the note.</param>
/// <param name="Phoneme">Phoneme of the note (if available).</param>
public record Note(
    int Key,
    long TickOn,
    long TickOff,
    string Lyric,
    string? Phoneme);
