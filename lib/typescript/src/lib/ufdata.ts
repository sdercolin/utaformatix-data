import { Project } from './project';

/**
 * UtaFormatix Data Document.
 * @param formatVersion - The version of the format. Current version is [UtaFormatixDataVersion].
 * @param project - Content of the project.
 */
export type UfData = {
  formatVersion: number;
  project: Project;
};
