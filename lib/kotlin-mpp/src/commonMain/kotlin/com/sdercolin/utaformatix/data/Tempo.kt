package com.sdercolin.utaformatix.data

import kotlinx.serialization.Serializable

/**
 * Tempo label model
 * @param tickPosition Tick position of the tempo label
 * @param bpm Tempo in beats-per-minute
 */
@Serializable
data class Tempo(
    val tickPosition: Long,
    val bpm: Double
)
