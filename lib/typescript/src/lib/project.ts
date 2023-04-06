import { Tempo } from './tempo';
import { TimeSignature } from './time-signature';
import { Track } from './track';

/**
 * Project model.
 * @param name - Project name.
 * @param tracks - List of track models in the project.
 * @param timeSignatures - List of time signatures in the project.
 * @param tempos - List of tempo labels in the project.
 * @param measurePrefix - Int32. Count of measure prefixes (measures that cannot contain notes, restricted by some editors).
 */
export type Project = {
  name: string;
  tracks: Track[];
  timeSignatures: TimeSignature[];
  tempos: Tempo[];
  measurePrefix: number;
};
