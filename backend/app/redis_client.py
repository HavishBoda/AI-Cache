import redis
import os 
from typing import Optional, Dict, Any
import json 

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
CACHE_SIZE = int(os.getenv("CACHE_SIZE", "1000"))  # Max items in LRU cache

redis_client = redis.Redis.from_url(
    REDIS_URL, 
    decode_responses=True
)

# configure LRU cache
try:
    redis_client.config_set('maxmemory', f'{os.getenv("CACHE_SIZE", "1000")}mb')
    redis_client.config_set('maxmemory-policy', 'allkeys-lru')
    redis_client.ping()
except as e:
    print(f"Redis connection error: {e}")
    raise

def get_cached(key: str) -> str:
    try:
        if value := redis_client.get(key):
            return json.loads(value)
    except (json.JSONDecodeError, redis.RedisError) as e:
        print(f"Cache get error for key {key}: {e}")
    return None

def set_cached(key: str) -> str:
    try:
        return redis_client.set(key, json.dumps(value), ex=ttl)
    except (TypeError, redis.RedisError) as e:
        print(f"Cache set error for key {key}: {e}")
        return False 

    

