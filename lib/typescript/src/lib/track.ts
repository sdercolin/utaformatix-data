import { Note } from './note';
import { Pitch } from './pitch';

/**
 * Track model.
 * @param name - Track name.
 * @param notes - Notes in the track.
 * @param pitch - Pitch data bound to the track (if any).
 */
export type Track = {
  name: string;
  notes: Note[];
  pitch?: Pitch;
};
