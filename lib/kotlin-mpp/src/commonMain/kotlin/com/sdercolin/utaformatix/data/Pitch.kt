package com.sdercolin.utaformatix.data

import kotlinx.serialization.Serializable

/**
 * Pitch data model. Only points with changed values are included
 * @param ticks Tick positions of the data points
 * @param values Semitone values of the data points. Items could be `null` only when [isAbsolute] is true. In this case,
 *               it represents the end of the previous value's lasting.
 * @param isAbsolute True if the semitone value is absolute, otherwise it's relative to the note's key
 */
@Serializable
data class Pitch(
    val ticks: List<Long> = emptyList(),
    val values: List<Double?> = emptyList(),
    val isAbsolute: Boolean = false,
)
