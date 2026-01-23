"""Voice module for text-to-speech voice operations."""
from typing import Optional
from videodb._constants import ApiPath


class Voice:
    """Voice class to interact with text-to-speech voices

    :ivar str id: Unique identifier for the voice
    :ivar str name: Name of the voice
    :ivar str provider: TTS provider (elevenlabs, openai, azure)
    :ivar str language: Language code (e.g., en-US)
    :ivar str gender: Gender of the voice (male, female, neutral)
    :ivar str preview_url: URL for voice preview audio
    :ivar bool is_cloned: Whether the voice is a cloned voice
    :ivar str created_at: Creation timestamp of the voice
    """

    def __init__(self, _connection, id: str, **kwargs) -> None:
        self._connection = _connection
        self.id = id
        self.name = kwargs.get("name")
        self.provider = kwargs.get("provider")
        self.language = kwargs.get("language")
        self.gender = kwargs.get("gender")
        self.preview_url = kwargs.get("preview_url")
        self.is_cloned = kwargs.get("is_cloned")
        self.created_at = kwargs.get("created_at")

    def __repr__(self) -> str:
        return (
            f"Voice(id={self.id}, name={self.name}, provider={self.provider}, "
            f"language={self.language}, gender={self.gender})"
        )
