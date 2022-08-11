package com.sdercolin.utaformatix.data

import kotlinx.serialization.Serializable

/**
 * Time signature model
 * @param measurePosition Measure (bar) position of the time signature
 * @param numerator Beats per measure
 * @param denominator Note value per beat
 */
@Serializable
data class TimeSignature(
    val measurePosition: Int,
    val numerator: Int,
    val denominator: Int
)
