# seniverse-sdk
python sdk for seniverse

```python
from seniverse.client import Client

c = Client('api_key', 'user_id')
c.weather_now('beijing')

# {'results': [{'location': {'id': 'WX4FBXXFKE4F', 'name': '北京', 'country': 'CN', 'path': '北京,北京,中国', 'timezone': 'Asia/Shanghai', 'timezone_offset': '+08:00'}, 'now': {'text': '晴', 'code': '0', 'temperature': '28'}, 'last_update': '2017-04-30T15:55:00+08:00'}]}
```