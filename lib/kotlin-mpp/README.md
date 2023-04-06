# UtaFormatix Data in Kotlin

[![Maven Central](https://img.shields.io/maven-central/v/com.sdercolin.utaformatix/utaformatix-data/1.0.0)](https://search.maven.org/artifact/com.sdercolin.utaformatix/utaformatix-data/1.0.0/pom)

Kotlin implementation of [UtaFormatix Data Format](https://github.com/sdercolin/utaformatix-data).

## Import

This library has full support of Kotlin multiplatform projects.

Kotlin DSL:

```kotlin
repositories {
    mavenCentral()
}

dependencies {
    implementation("com.sdercolin.utaformatix:utaformatix-data:1.0.0")
}
```

Groovy DSL:

```gradle
repositories {
    mavenCentral()
}

dependencies {
    implementation "com.sdercolin.utaformatix:utaformatix-data:1.0.0"
}
```

### Use Kotlin's Serialization library

The classes are marked `@Serializable` so you can
use [kotlinx.serialization](https://github.com/Kotlin/kotlinx.serialization) to serialize/deserialize them.

#### Example

In your `build.gradle.kts`:

```kotlin

plugins {
    kotlin("jvm") version "1.6.21"
    kotlin("plugin.serialization") version "1.6.21"
}

// ...

dependencies {
    // ...
    implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.3.3")
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
}

fun deserialize(json: String): Document {
    return jsonSerializer.decodeFromString(Document.serializer(), json)
}

fun serialize(document: Document): String {
    return jsonSerializer.encodeToString(Document.serializer(), document)
}
```
