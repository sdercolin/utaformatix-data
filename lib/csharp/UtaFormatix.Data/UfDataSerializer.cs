using System.Text.Encodings.Web;
using System.Text.Json;
using System.Text.Unicode;

namespace UtaFormatix.Data;

/// <summary>Helper class to handle serialization or deserialization of
/// UfData classes.</summary>
public static class UfDataSerializer
{
    /// <summary>
    /// Default <c>JsonSerializerOptions</c> for serialization or
    /// deserialization of UfData classes.</summary>
    /// </summary>
    public static JsonSerializerOptions DefaultOptions
        => new JsonSerializerOptions
        {
            PropertyNamingPolicy = JsonNamingPolicy.CamelCase,
            Encoder = JavaScriptEncoder.Create(UnicodeRanges.All)
        };

    /// <summary>
    /// Serialize a UfData class instance to JSON string with default options.
    /// </summary>
    public static string Serialize<T>(T obj, JsonSerializerOptions? options = null) =>
        JsonSerializer.Serialize<T>(obj, options: options ?? DefaultOptions);

    /// <summary>
    /// Deserialize a JSON string to a UfData class instance with default options.
    /// </summary>
    public static T? Deserialize<T>(string json, JsonSerializerOptions? options = null) =>
        JsonSerializer.Deserialize<T>(json, options: options ?? DefaultOptions);
}
