namespace UtaFormatix.Data;

/// <summary>Project model.</summary>
///
/// <param name="Name">Project name.</param>
/// <param name="Tracks">List of track models in the project.</param>
/// <param name="TimeSignatures">List of time signatures in the project.</param>
/// <param name="Tempos">List of tempo labels in the project.</param>
/// <param name="MeasurePrefix">Count of measure prefixes (measures that cannot
/// contain notes, restricted by some editors).</param>
public record Project(string Name, Track[] Tracks, TimeSignature[]? TimeSignatures, Tempo[] Tempos, int MeasurePrefix);
