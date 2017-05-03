# encoding:utf-8

import requests

class Client:
  def __init__(self, api_key, user_id):
    self.api_key = api_key
    self.user_id = user_id

  def weather_now(self, location):
    r = requests.get('https://api.seniverse.com/v3/weather/now.json?key=%s&location=%s&language=zh-Hans&unit=c' % (self.api_key, location))
    if r.status_code == 200:
      return r.json()
    else:
      return None
