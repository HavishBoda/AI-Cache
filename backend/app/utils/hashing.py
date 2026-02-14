import hashlib

def make_cache_key(prefix: str, text: str) -> str:
    """
    Generates fixed-length Redis cache key for given text

    Args: 
        prefix: rag_query or rag_response
        text: the string to hash
    
    Returns:
        str: Redis key in hashed format
    """

    text_bytes = text.encode('utf-8')

    # create SHA256 hash
    hash_obj = hashlib.sha256(text_bytes)
    hash_hex = hash_obj.hexdigest()

    # combine with prefix to return
    return f"{prefix}:{hash_hex}"
