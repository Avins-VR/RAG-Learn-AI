from typing import Dict, Any, Tuple, Optional

_cache: Dict[str, Tuple[Any, Any]] = {}

def get_cached(file_hash: str) -> Optional[Tuple[Any, Any]]:
    return _cache.get(file_hash)

def set_cached(file_hash: str, chunks: Any, index: Any) -> None:
    _cache[file_hash] = (chunks, index)

def has_cached(file_hash: str) -> bool:
    return file_hash in _cache