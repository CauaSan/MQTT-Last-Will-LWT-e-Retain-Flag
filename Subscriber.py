import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883

def on_connect(client, userdata, flags, rc):
    print("Monitor conectado!")

    # 🔥 QoS 1 para garantir entrega
    client.subscribe("iot/device1/status", qos=1)
    client.subscribe("iot/device1/temperature", qos=1)

def on_message(client, userdata, msg):
    print(f"[{msg.topic}] {msg.payload.decode()}")

# 🔥 SESSÃO PERSISTENTE (ESSENCIAL)
client = mqtt.Client(
    client_id="monitor",
    clean_session=False,
    protocol=mqtt.MQTTv311
)

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT)

client.loop_forever()