import hashlib
import redis
import hashlib
# import subprocess
# import json
# 连接到 Redis 服务器
r = redis.Redis(host='redis', port=6379, db=0,password = '123456789')

def generate_cache_key(command: str) -> str:
    # 使用 SHA-256 哈希函数生成唯一标识符
    return hashlib.sha256(command.encode('utf-8')).hexdigest()



# 生成缓存 key
def generate_cache_key(command: str) -> str:
    return hashlib.sha256(command.encode('utf-8')).hexdigest()

# 存储缓存结果到 Redis
def store_in_cache(key: str, result: str, ttl: int = 3600):
    # 使用 SET 命令存储缓存，并设置过期时间（TTL，默认为24小时）
    r.setex(key, ttl*24, result)

# 从 Redis 获取缓存的代码
def get_from_cache(key: str) -> str:
    cached_result = r.get(key)
    if cached_result:
        return cached_result.decode('utf-8')  # Redis 返回的结果是字节类型，需解码为字符串
    return None