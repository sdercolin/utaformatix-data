namespace UtaFormatix.Data;

/// <summary>Pitch data model. 
/// Only points with changed values are included.</summary>
///
/// <param name="Ticks">Tick positions of the data points.</param>
/// <param name="Values">Semitone values of the data points.
/// Items could be `null` only when [isAbsolute] is true.
/// In this case, it represents the end of the previous value's lasting.</param>
/// <param name="IsAbsolute">True if the semitone value is absolute,
/// otherwise it's relative to the note's key.</param>
public record Pitch(long[] Ticks, double?[] Values, bool IsAbsolute);
