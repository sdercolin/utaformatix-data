package com.sdercolin.utaformatix.data

import kotlinx.serialization.Serializable

/**
 * Track model
 * @param name Track name
 * @param notes Notes in the track
 * @param pitch Pitch data bound to the track (if any)
 */
@Serializable
data class Track(
    val name: String,
    val notes: List<Note>,
    val pitch: Pitch?
)
