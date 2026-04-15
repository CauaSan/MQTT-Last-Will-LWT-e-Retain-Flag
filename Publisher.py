import paho.mqtt.client as mqtt
import time
import random

BROKER = "broker.hivemq.com"
PORT = 1883

TOPIC_STATUS = "iot/device1/status"
TOPIC_TEMP = "iot/device1/temperature"

client = mqtt.Client(client_id="device1", protocol=mqtt.MQTTv311)

# 🔥 LWT (continua usando retain para status)
client.will_set(
    TOPIC_STATUS,
    payload="OFFLINE",
    qos=1,
    retain=True
)

client.connect(BROKER, PORT)

# 🔥 Status online (retain continua aqui)
client.publish(TOPIC_STATUS, "ONLINE", qos=1, retain=True)

print("Dispositivo conectado e ONLINE")

try:
    while True:
        temperatura = round(random.uniform(20, 30), 2)
        mensagem = f"{temperatura}°C"

        # 🔥 AGORA SEM RETAIN (histórico via QoS)
        client.publish(TOPIC_TEMP, mensagem, qos=1, retain=False)

        print("Enviado:", mensagem)
        time.sleep(5)

except KeyboardInterrupt:
    print("\nDesligando corretamente...")

    client.publish(TOPIC_STATUS, "OFFLINE", qos=1, retain=True)
    client.disconnect()