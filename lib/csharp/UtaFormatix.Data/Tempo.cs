namespace UtaFormatix.Data;

/// <summary>Tempo label model.</summary>
///
/// <param name="TickPosition">Tick position of the tempo label.</param>
/// <param name="Bpm">Tempo in beats-per-minute.</param>
public record Tempo(long TickPosition, double Bpm);
