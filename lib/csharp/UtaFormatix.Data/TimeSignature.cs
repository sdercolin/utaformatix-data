namespace UtaFormatix.Data;

/// <summary>Time signature model.</summary>
///
/// <param name="MeasurePosition">Measure (bar) position of the time signature.</param>
/// <param name="Numerator">Beats per measure.</param>
/// <param name="Denominator">Note value per beat.</param>
public record TimeSignature(int MeasurePosition, int Numerator, int Denominator);
