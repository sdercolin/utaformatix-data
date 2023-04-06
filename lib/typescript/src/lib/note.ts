/**
 * Note model.
 * @param key - Int32. Semitone value of the note's key (Center C = 60).
 * @param tickOn - Int64. Tick position of the note's start.
 * @param tickOff - Int64. Tick position of the note's end.
 * @param lyric - Lyric of the note.
 * @param phoneme - Phoneme of the note (if available).
 */
export type Note = {
  key: number;
  tickOn: number;
  tickOff: number;
  lyric: string;
  phoneme?: string;
};
