/**
 * Pitch data model. Only points with changed values are included.
 *
 * @param ticks - Int64[]. Tick positions of the data points.
 * @param values - (Double|null)[]. Semitone values of the data points.
 *   Items could be `null` only when [isAbsolute] is true.
 *   In this case, it represents the end of the previous value's lasting.
 * @param isAbsolute - True if the semitone value is absolute, otherwise it's relative to the note's key.
 */
export type Pitch = {
  ticks: number[];
  values: (number | null)[];
  isAbsolute: boolean;
};
