namespace UtaFormatix.Data.Tests;

public class Tests
{

    [Test]
    public void TestNote()
    {
        var note = new Note(
            Key: 60,
            TickOn: 0,
            TickOff: 480,
            Lyric: "あ",
            Phoneme: null);

        var jsonString = UfDataSerializer.Serialize(note);

        var expected = @"{""key"":60,""tickOn"":0,""tickOff"":480,""lyric"":""あ"",""phoneme"":null}";

        Assert.That(jsonString, Is.EqualTo(expected));

        var noteDeserialized = UfDataSerializer.Deserialize<Note>(jsonString);

        Assert.That(noteDeserialized, Is.Not.Null);
        Assert.That(noteDeserialized, Is.EqualTo(note));
    }

    [Test]
    public void TestPitch()
    {
        var pitch = new Pitch(
            Ticks: new long[] { 1, 4, 5 },
            Values: new double?[] { 1.0, null, 2.5 },
            IsAbsolute: true);

        var jsonString = UfDataSerializer.Serialize(pitch);

        var expected = @"{""ticks"":[1,4,5],""values"":[1,null,2.5],""isAbsolute"":true}";

        Assert.That(jsonString, Is.EqualTo(expected));

        var pitchDeserialized = UfDataSerializer.Deserialize<Pitch>(jsonString);

        Assert.That(pitchDeserialized, Is.Not.Null);
        Assert.That(pitchDeserialized.Ticks, Is.EquivalentTo(pitch.Ticks));
        Assert.That(pitchDeserialized.Values, Is.EquivalentTo(pitch.Values));
        Assert.That(pitchDeserialized.IsAbsolute, Is.EqualTo(pitch.IsAbsolute));
    }

    [Test]
    public void TestTrack()
    {
        var pitch = new Pitch(
            Ticks: new long[] { 1, 4, 5 },
            Values: new double?[] { 1.0, null, 2.5 },
            IsAbsolute: true);

        var notes = new Note[]
        {
            new Note(
                Key: 60,
                TickOn: 0,
                TickOff: 480,
                Lyric: "あ",
                Phoneme: null),
            new Note(
                Key: 60,
                TickOn: 480,
                TickOff: 960,
                Lyric: "あ",
                Phoneme: null)
        };

        var track1 = new Track(Name: "Track", Notes: notes, Pitch: null);
        var track2 = new Track(Name: "Track", Notes: notes, Pitch: pitch);

        var trackString1 = UfDataSerializer.Serialize(track1);
        var trackString2 = UfDataSerializer.Serialize(track2);

        var expected1 = @"{""name"":""Track"",""notes"":[{""key"":60,""tickOn"":0,""tickOff"":480,""lyric"":""あ"",""phoneme"":null},{""key"":60,""tickOn"":480,""tickOff"":960,""lyric"":""あ"",""phoneme"":null}],""pitch"":null}";
        var expected2 = @"{""name"":""Track"",""notes"":[{""key"":60,""tickOn"":0,""tickOff"":480,""lyric"":""あ"",""phoneme"":null},{""key"":60,""tickOn"":480,""tickOff"":960,""lyric"":""あ"",""phoneme"":null}],""pitch"":{""ticks"":[1,4,5],""values"":[1,null,2.5],""isAbsolute"":true}}";

        Assert.That(trackString1, Is.EqualTo(expected1));
        Assert.That(trackString2, Is.EqualTo(expected2));

        var deserialized1 = UfDataSerializer.Deserialize<Track>(trackString1);
        var deserialized2 = UfDataSerializer.Deserialize<Track>(trackString2);
        Assert.That(deserialized1, Is.Not.Null);
        Assert.That(deserialized2, Is.Not.Null);
        Assert.That(deserialized1.Notes, Is.EquivalentTo(notes));
        Assert.That(deserialized2.Notes, Is.EquivalentTo(notes));
        Assert.That(deserialized1.Pitch, Is.Null);
        Assert.That(deserialized2.Pitch, Is.Not.Null);
        Assert.That(deserialized2.Pitch.Ticks, Is.EquivalentTo(pitch.Ticks));
        Assert.That(deserialized2.Pitch.Values, Is.EquivalentTo(pitch.Values));
    }
}
