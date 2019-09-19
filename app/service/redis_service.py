import redis

redis_client = redis.Redis(host='127.0.0.1', port=6379, db=0, decode_responses=True)


class RedisService:
    @classmethod
    def user_nums(cls):
        return redis_client.scard('users')

    @classmethod
    def aweme_nums(self):
        return redis_client.scard('awemes')


if __name__ == '__main__':
    print(RedisService.user_nums())
    print(RedisService.aweme_nums())
