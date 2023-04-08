namespace UtaFormatix.Data
{

    /// <summary>UtaFormatix Data Document.</summary>
    ///
    /// <param name="FormatVersion">The format version of this document.</param>
    /// <param name="Project">Content of the project.</param>
    public record UfData(int FormatVersion, Project Project)
    {
        /// <summary>
        /// Current format version implemented by this library.
        /// </summary>
        public const int CurrentFormatVersion = 1;
    }
}
