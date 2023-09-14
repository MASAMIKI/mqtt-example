import sys

import paho.mqtt.client as mqtt


MQTT_BROKER_HOST = "localhost"
MQTT_BROKER_PORT = 1883
MQTT_BROKER_KEEPALIVE = 1
TOPIC = "keyboard/input"


# 接続が完了したときのコールバック
def on_connect(_client, userdata, flags, rc):
    if rc != 0:
        print("Connection failed")
        sys.exit(1)
    else:
        print("Connected")
        _client.subscribe(TOPIC)


# メッセージが到着したときのコールバック
def on_message(_client, userdata, message):
    print(f"{message.topic}:'{message.payload.decode()}'")
    if message.payload.decode() == "exit":
        _client.loop_stop()
        _client.disconnect()


# クライアントの設定
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# MQTTブローカーに接続
client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT, MQTT_BROKER_KEEPALIVE)

# メッセージループの開始
client.loop_forever()
