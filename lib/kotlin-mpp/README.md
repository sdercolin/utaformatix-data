# UtaFormatix Data in Kotlin

[![Maven Central](https://img.shields.io/maven-central/v/com.sdercolin.utaformatix/utaformatix-data/1.1.0)](https://search.maven.org/artifact/com.sdercolin.utaformatix/utaformatix-data/1.1.0/pom)

Kotlin implementation of [UtaFormatix Data Format](https://github.com/sdercolin/utaformatix-data).

## Import

This library has full support of Kotlin multiplatform projects.

Kotlin DSL:

```kotlin
repositories {
    mavenCentral()
}

dependencies {
    implementation("com.sdercolin.utaformatix:utaformatix-data:1.1.0")
}
```

Groovy DSL:

```gradle
repositories {
    mavenCentral()
}

dependencies {
    implementation "com.sdercolin.utaformatix:utaformatix-data:1.1.0"
}
```

### Use Kotlin's Serialization library

The classes are marked `@Serializable` so you can
use [kotlinx.serialization](https://github.com/Kotlin/kotlinx.serialization) to serialize/deserialize them.

#### Example

In your `build.gradle.kts`:

```kotlin
// Note: The latest version requires K2 compiler. If you are using K1, please use version 1.0.0.
plugins {
    kotlin("jvm") version "2.1.20"
    kotlin("plugin.serialization") version "2.1.20"
}

// ...

dependencies {
    // ...
    implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.5.0")
    // ...
}
```

In your code:

```kotlin
import com.sdercolin.utaformatix.data.Document

val jsonSerializer = Json {
    isLenient = true
    ignoreUnknownKeys = true
    encodeDefaults = true
    explicitNulls = false
    coerceInputValues = true
}

fun deserialize(json: String): Document {
    return jsonSerializer.decodeFromString(Document.serializer(), json)
}

fun serialize(document: Document): String {
    return jsonSerializer.encodeToString(Document.serializer(), document)
}
```
