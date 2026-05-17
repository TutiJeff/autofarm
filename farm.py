import requests
import threading
import time

# PONÉ TU TOKEN ACÁ
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTUwNTYsImlhdCI6MTc3ODkxMTYxOCwiZXhwIjoxNzc5NTE2NDE4fQ.fai9PW7j66cRF7JvXI9BEjSuTaBItqLt4LINN4_KyTg"

def atacar():
    for _ in range(50):
        try:
            requests.post("http://187.45.255.120:3001/addpoints",
                json={"username": "TutiJeff", "points": 1},
                headers={"Authorization": token}, timeout=3)
        except: pass

print("AutoFarm 0.40 iniciado para TutiJeff")

while True:
    for _ in range(10):
        threading.Thread(target=atacar).start()
    time.sleep(65)