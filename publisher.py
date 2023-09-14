import sys

import paho.mqtt.client as mqtt

MQTT_BROKER_HOST = "localhost"
MQTT_BROKER_PORT = 1883
MQTT_BROKER_KEEPALIVE = 60
TOPIC = "keyboard/input"


# 接続が完了したときのコールバック
def on_connect(_client, userdata, flags, rc):
    if rc != 0:
        print("Connection failed")
        sys.exit(1)
    else:
        print("Connected")


# クライアントの設定
client = mqtt.Client()
client.on_connect = on_connect

# MQTTブローカーに接続
client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT, MQTT_BROKER_KEEPALIVE)

while True:
    message = input("Enter message to send (type 'exit' to quit): ")

    # "exit"が入力されたらループを抜ける
    if message.lower() == 'exit':
        client.publish(TOPIC, message)
        break

    # メッセージをPublish
    client.publish(TOPIC, message)

client.disconnect()
