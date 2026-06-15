import socket
import threading
import json

TRACKER_IP = "127.0.0.1"
TRACKER_PORT = 6000
peers = {}  # file_name -> {chunk_name -> [(ip, port)]}

def handle_client(conn):
    try:
        data = conn.recv(4096).decode()
        req = json.loads(data)
        action = req.get("action")
        if action == "register":
            file_name = req["file_name"]
            chunk = req["chunk"]
            ip, port = req["ip"], req["port"]
            peers.setdefault(file_name, {}).setdefault(chunk, []).append((ip, port))
            conn.send(b"OK")
        elif action == "request":
            file_name = req["file_name"]
            conn.send(json.dumps(peers.get(file_name, {})).encode())
    except Exception as e:
        print("Tracker error:", e)
    finally:
        conn.close()

def start_tracker():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((TRACKER_IP, TRACKER_PORT))
    server.listen(5)
    print(f"Tracker running at {TRACKER_IP}:{TRACKER_PORT}")
    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn,)).start()

if __name__ == "__main__":
    start_tracker()