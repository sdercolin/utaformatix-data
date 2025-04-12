package com.sdercolin.utaformatix.data

import kotlinx.serialization.Serializable

/**
 * Note model
 * @param key Semitone value of the note's key (Center C = 60)
 * @param tickOn Tick position of the note's start
 * @param tickOff Tick position of the note's end
 * @param lyric Lyric of the note
 * @param phoneme Phoneme of the note (if available)
 */
@Serializable
data class Note(
    val key: Int,
    val tickOn: Long,
    val tickOff: Long,
    val lyric: String = "",
    val phoneme: String? = null,
)
