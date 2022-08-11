package com.sdercolin.utaformatix.data

import kotlinx.serialization.Serializable

/**
 * UtaFormatix Data Document
 * @param formatVersion The version of the format. Current version is [UtaFormatixDataVersion].
 * @param project Content of the project.
 */
@Serializable
data class Document(
    val formatVersion: Int,
    val project: Project
)
