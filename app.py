import paho.mqtt.client as paho
import time
import streamlit as st
import json
import platform

# Mostrar la versión actual de Python
st.markdown(f"### Versión de Python: `{platform.python_version()}`")

# Variables globales
values = 0.0
act1 = "OFF"
message_received = ""

# Función callback para publicación
def on_publish(client, userdata, result):
    print("📤 Dato publicado con éxito.\n")

# Función callback para recepción de mensajes
def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received = str(message.payload.decode("utf-8"))
    st.info(f"📩 Mensaje recibido: {message_received}")

# Parámetros del broker MQTT
broker = "157.230.214.127"
port = 1883
client_id = "GIT-HUB"

# Título de la app
st.title("🔌 Control MQTT")

# Botón ON
if st.button('Encender 🔛'):
    act1 = "ON"
    client = paho.Client(client_id)
    client.on_publish = on_publish
    client.connect(broker, port)
    msg = json.dumps({"Act1": act1})
    client.publish("cmqtt_s", msg)

# Botón OFF
if st.button('Apagar 🔴'):
    act1 = "OFF"
    client = paho.Client(client_id)
    client.on_publish = on_publish
    client.connect(broker, port)
    msg = json.dumps({"Act1": act1})
    client.publish("cmqtt_s", msg)

# Selector de valor analógico
values = st.slider('🎚 Selecciona un valor analógico', 0.0, 100.0)
st.write(f'Valor seleccionado: `{values}`')

# Botón para enviar valor analógico
if st.button('Enviar valor analógico 📤'):
    client = paho.Client(client_id)
    client.on_publish = on_publish
    client.connect(broker, port)
    msg = json.dumps({"Analog": float(values)})
    client.publish("cmqtt_a", msg)




