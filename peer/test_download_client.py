from download_client import download_chunk

# Localhost testing
PEER_IP = "127.0.0.1"

# Same port as upload server
PEER_PORT = 6001

# Request this chunk
CHUNK_NAME = "chunk_0"

download_chunk(
    PEER_IP,
    PEER_PORT,
    CHUNK_NAME
)