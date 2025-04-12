import org.jetbrains.kotlin.gradle.dsl.JvmTarget
import org.jetbrains.kotlin.gradle.plugin.mpp.KotlinNativeTarget

plugins {
    kotlin("multiplatform") version "2.1.20"
    kotlin("plugin.serialization") version "2.1.20"
    id("org.jetbrains.dokka") version "2.0.0"
    id("org.danilopianini.publish-on-central") version "8.0.6"
}

val libVersion by extra { "1.1.0" }
val groupId by extra { "com.sdercolin.utaformatix" }
val artifactId by extra { "utaformatix-data" }
group = groupId
version = libVersion

repositories {
    mavenCentral()
}

kotlin {
    jvmToolchain(21)
    jvm {
        testRuns["test"].executionTask.configure {
            useJUnitPlatform()
        }
        compilations.all {
            compileTaskProvider.configure {
                compilerOptions {
                    jvmTarget = JvmTarget.JVM_1_8
                }
            }
        }
    }
    js(IR) {
        browser()
        nodejs()
        binaries.library()
    }
    val nativeSetup: KotlinNativeTarget.() -> Unit = {
        binaries {
            sharedLib()
            staticLib()
        }
    }

    applyDefaultHierarchyTemplate()

    linuxX64(nativeSetup)
    linuxArm64(nativeSetup)
    mingwX64(nativeSetup)
    macosX64(nativeSetup)
    macosArm64(nativeSetup)
    iosArm64(nativeSetup)
    iosSimulatorArm64(nativeSetup)

    sourceSets {
        val commonMain by getting {
            dependencies {
                implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.5.0")
            }
        }
        val commonTest by getting
    }

    targets.all {
        compilations.all {
            compileTaskProvider.configure {
                compilerOptions {
                    allWarningsAsErrors = true
                    freeCompilerArgs.add("-Xexpect-actual-classes")
                }
            }
        }
    }
}

publishOnCentral {
    repoOwner.set("sdercolin")
    projectDescription.set("Common data container for singing synthesis softwares.")
    val user = findProperty("sonatypeUsername") as? String
    val password = findProperty("sonatypePassword") as? String
    mavenCentral.user.set(user)
    mavenCentral.password.set(password)
}

publishing {
    publications.withType<MavenPublication> {
        pom {
            name.set(artifactId)
            description.set("Common data container for singing synthesis softwares.")
            url.set("https://github.com/sdercolin/utaformatix-data")
            developers {
                developer {
                    name.set("sdercolin")
                    email.set("sder.colin@gmail.com")
                    url.set("https://github.com/sdercolin")
                }
            }
            scm {
                connection.set("git@github.com:sdercolin/utaformatix-data.git")
                developerConnection.set("git@github.com:sdercolin/utaformatix-data.git")
                url.set("https://github.com/sdercolin/utaformatix-data")
            }
        }
    }
}
