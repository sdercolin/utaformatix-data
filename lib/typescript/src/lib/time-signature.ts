/**
 * Time signature model.
 * @param measurePosition - Int32. Measure (bar) position of the time signature.
 * @param numerator - Int32. Beats per measure.
 * @param denominator - Int32. Note value per beat.
 */
export type TimeSignature = {
  measurePosition: number;
  numerator: number;
  denominator: number;
};
