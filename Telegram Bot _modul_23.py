import redis
import \
    json  # так-так-так, кто это тут у нас? Наш старый друг Джейсон заглянул на огонёк! Ну привет, чем ты сегодня нас порадуешь?

red = redis.Redis(
    host='redis-17970.c302.asia-northeast1-1.gce.redns.redis-cloud.com',
    port=17970,
    password='AEUoOaZJx30cH0fPwiMQZY3fFJL1O1Uw'
)

dict1 = {'key1': 'value1', 'key2': 'value2'}  # создаём словарь для записи
red.set('dict1', json.dumps(dict1))  # с помощью функции dumps() из модуля json превратим наш словарь в строчку
converted_dict = json.loads(
    red.get('dict1'))  # с помощью знакомой нам функции превращаем данные полученные из кэша обратно в словарь
print(type(converted_dict))  # убеждаемся, что получили действительно словарь
print(converted_dict)  # ну и выводим его содержание