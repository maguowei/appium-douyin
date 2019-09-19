import json
from pprint import pprint
import mitmproxy.http
import mitmproxy.proxy.protocol
from app.service.mongo_service import db
from app.service.redis_service import redis_client
from app.douyin_driver import DouyinDriver, desired_caps


class Events:
    def __init__(self):
        # self.driver = DouyinDriver(desired_caps)
        # self.driver.click_by_name('同城')
        pass

    def response(self, flow: mitmproxy.http.HTTPFlow):
        response = flow.response
        content = response.text
        url = flow.request.url
        # print(url)
        # 附近列表
        if '/aweme/v1/nearby/feed/' in url:
            data = json.loads(content)
            # pprint(data)
            if data['status_code'] == 0 and data['has_more'] == 1:
                # db['nearby'].insert_one(data)
                # db['nearby_videos'].insert_many(data['aweme_list'])
                for aweme in data['aweme_list']:
                    aweme_id = aweme['aweme_id']
                    db['nearby_videos'].replace_one({'aweme_id': aweme_id}, aweme, upsert=True)
                    redis_client.sadd('users', aweme['author_user_id'])

        # 关注
        elif '/v2/follow/feed/' in url:
            data = json.loads(content)
            # pprint(data)
            db['follow'].insert_one(data)

        # 关注列表
        elif '/aweme/v1/user/follower/list/' in url:
            data = json.loads(content)
            db['followers'].insert_one(data)
            followers = data['followers']
            for follower in followers:
                user = {
                    'uid': follower['uid'],
                    'nickname': follower['nickname'],
                }
                redis_client.sadd('users', user['uid'])
                # print(user)
