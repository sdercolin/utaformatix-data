# UtaFormatix Data in C#

[![Nuget](https://img.shields.io/nuget/v/UtaFormatix.Data)](https://www.nuget.org/packages/UtaFormatix.Data/)

C# implementation of [UtaFormatix Data Format](https://github.com/sdercolin/utaformatix-data).

## Framework Requirements

- .NET 6.0

## Install

This package is published on [NuGet](https://www.nuget.org/packages/UtaFormatix.Data/).

```bash
dotnet add package UtaFormatix.Data
```

Or install it from Visual Studio's NuGet Package Manager.

## Example

The classes are implemented as records, so please check
out [C# 9.0's new features](https://docs.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-9#record-types) to access
members and create new instances.

```csharp
using UtaFormatix.Data;

var text = "..."; // load from somewhere
var data = UfDataSerializer.Deserialize<UfData>(text);

if (data == null)
{
    return;
}

Console.WriteLine(data.FormatVersion); // format version of the data
Console.WriteLine(UfData.CurrentFormatVersion); // format version of the library

// access members
Console.WriteLine(data.Project.Name); 

// change a track name
var track = data.Project.Tracks[0] with { Name = "My Track" };
var tracks = data.Project.Tracks.ToList();
tracks[0] = track;
var newData = data with { Project = data.Project with { Tracks = tracks.ToArray() } };

// serialize the new data
var newText = UfDataSerializer.Serialize(newData);
```
