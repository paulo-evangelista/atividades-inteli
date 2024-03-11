import json
import psycopg2
import paho.mqtt.client as mqtt
from psycopg2 import sql

broker = 'localhost'
port = 1883 
topic = "sensor/data"
client_id = 'subscriber'

pg_conn = psycopg2.connect(
    dbname='db',
    user='username',
    password='password',
    host='localhost'
)
pg_cursor = pg_conn.cursor()

def ensure_table_exists():
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS air_quality (
        id SERIAL PRIMARY KEY,
        timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
        pm1 INTEGER,
        pm2 INTEGER,
        pm4 INTEGER,
        pm10 INTEGER
    );
    '''
    pg_cursor.execute(create_table_query)
    pg_conn.commit()

def on_connect(mqttc, obj, flags, reason_code, properties):
    print("Connected with result code")

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload)
        pm1 = payload['mc_pm1_0']
        pm2 = payload['mc_pm2_5']
        pm4 = payload['mc_pm4_0']
        pm10 = payload['mc_pm10']
        print(pm1, pm2, pm4)
        
        insert_query = sql.SQL("INSERT INTO air_quality (pm1, pm2, pm4, pm10) VALUES (%s, %s, %s, %s);")
        record_to_insert = (pm1, pm2, pm4, pm10)
        pg_cursor.execute(insert_query, record_to_insert)
        pg_conn.commit()
        
        print(f"Data inserted: {record_to_insert}")
    except Exception as e:
        print(f"Failed to insert data: {e}")

def connect_mqtt():
    client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, port)
    return client

def subscribe(client):
    client.subscribe(topic)
    client.loop_forever()

if __name__ == '__main__':
    ensure_table_exists()
    client = connect_mqtt()
    subscribe(client)
