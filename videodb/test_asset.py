"""TestAsset model for VideoDB SDK"""
import logging

logger = logging.getLogger(__name__)


class TestAsset:
    """TestAsset class to interact with test assets."""

    def __init__(
        self,
        _connection,
        id: str,
        name: str = None,
        url: str = None,
        collection_id: str = None,
        created_at: str = None,
    ) -> None:
        self._connection = _connection
        self.id = id
        self.name = name
        self.url = url
        self.collection_id = collection_id
        self.created_at = created_at

    def __repr__(self) -> str:
        return (
            f"TestAsset(id={self.id}, name={self.name}, url={self.url}, "
            f"collection_id={self.collection_id}, created_at={self.created_at})"
        )
