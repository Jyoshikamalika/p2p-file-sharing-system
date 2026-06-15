import socket
import threading
import os
import sys

def handle_client(conn, chunk_folder):
    """
    Handles incoming chunk requests.
    """

    try:
        # Receive requested chunk name
        chunk_name = conn.recv(1024).decode()

        print(f"[REQUEST] {chunk_name}")

        chunk_path = os.path.join(
            chunk_folder,
            chunk_name
        )

        # Check if chunk exists
        if os.path.exists(chunk_path):

            print(f"[SENDING] {chunk_name}")

            with open(chunk_path, "rb") as f:

                while True:

                    data = f.read(4096)

                    if not data:
                        break

                    conn.sendall(data)

            print(f"[DONE] {chunk_name}")

        else:

            print(f"[NOT FOUND] {chunk_name}")

            conn.send(b"ERROR")

    except Exception as e:

        print("[ERROR]", e)

    finally:

        conn.close()


def start_server(port, chunk_folder):
    """
    Starts peer server.
    """

    # Check folder exists
    if not os.path.exists(chunk_folder):
        print(f"[ERROR] Folder not found: {chunk_folder}")
        return

    s = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    # Important fix for port reuse
    s.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1
    )

    s.bind(
        ("127.0.0.1", port)
    )

    s.listen(5)

    print(
        f"[SERVER RUNNING] Port {port} | Folder: {chunk_folder}"
    )

    while True:

        conn, addr = s.accept()

        print(f"[CONNECTED] {addr}")

        threading.Thread(

            target=handle_client,

            args=(conn, chunk_folder)

        ).start()


if __name__ == "__main__":

    # Default values
    port = 5001
    folder = "chunks_peer1"

    # Read arguments
    if len(sys.argv) >= 3:

        port = int(sys.argv[1])
        folder = sys.argv[2]

    else:

        print(
            "Usage:\n"
            "python server.py <port> <chunk_folder>\n"
            "Example:\n"
            "python server.py 5001 chunks_peer1"
        )
        sys.exit()

    start_server(port, folder)