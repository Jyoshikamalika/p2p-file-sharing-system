from parallel_download import parallel_download

# Peer connection details
PEER_IP = "127.0.0.1"
PORT = 7001

# List of chunks to download
chunk_list = [
    "chunk_0"
]

# Folder where chunks will be saved
SAVE_FOLDER = "../downloads"

# Start parallel download
parallel_download(
    PEER_IP,
    PORT,
    chunk_list,
    SAVE_FOLDER
)

print("[PARALLEL DOWNLOAD TEST COMPLETED]")