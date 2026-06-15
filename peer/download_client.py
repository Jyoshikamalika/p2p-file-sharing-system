import socket
import os

CHUNK_DIR = "chunks"

def download_chunk(ip, port, chunk_name, save_dir="downloads"):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.send(chunk_name.encode())
        path = os.path.join(save_dir, os.path.basename(chunk_name))
        with open(path, "wb") as f:
            while True:
                data = s.recv(4096)
                if not data:
                    break
                f.write(data)
        s.close()
        return True
    except Exception as e:
        print(f"Failed to download {chunk_name} from {ip}:{port} -> {e}")
        return False