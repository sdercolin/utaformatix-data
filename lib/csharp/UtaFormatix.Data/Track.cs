namespace UtaFormatix.Data;

/// <summary>Track model.</summary>
///
/// <param name="Name">Track name.</param>
/// <param name="Notes">Notes in the track.</param>
/// <param name="Pitch">Pitch data bound to the track (if any).</param>
public record Track(string Name, Note[] Notes, Pitch? Pitch);
