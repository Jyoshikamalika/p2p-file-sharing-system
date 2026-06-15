import socket
import json

# Tracker details
TRACKER_HOST = "127.0.0.1"
TRACKER_PORT = 5000

# Peer details
peer_id = input("Enter Peer ID: ")

peer_ip = "127.0.0.1"

peer_port = int(input("Enter Peer Port: "))


def register_peer():

    try:

        # Create socket
        client = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        # Connect to tracker
        client.connect(
            (TRACKER_HOST, TRACKER_PORT)
        )

        # Create message
        message = {
            "command": "REGISTER",
            "peer_id": peer_id,
            "ip": peer_ip,
            "port": peer_port
        }

        # Send message
        client.send(
            json.dumps(message).encode()
        )

        # Receive response
        response = client.recv(4096)

        print(
            "Tracker Response:",
            response.decode()
        )

        client.close()

    except Exception as e:

        print("Error connecting to tracker:", e)


if __name__ == "__main__":

    register_peer()