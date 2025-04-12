package com.sdercolin.utaformatix.data

import kotlinx.serialization.Serializable

/**
 * Project model
 * @param name Project name
 * @param tracks List of track models in the project
 * @param timeSignatures List of time signatures in the project
 * @param tempos List of tempo labels in the project
 * @param measurePrefix Count of measure prefixes (measures that cannot contain notes, restricted by some editors)
 */
@Serializable
data class Project(
    val name: String,
    val tracks: List<Track> = emptyList(),
    val timeSignatures: List<TimeSignature>,
    val tempos: List<Tempo>,
    val measurePrefix: Int = 0,
)
