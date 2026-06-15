from resume_download import resume_download

PEER_IP = "127.0.0.1"
PORT = 7001

chunk_list = [
    "chunk_0"
]

SAVE_FOLDER = "../downloads"

resume_download(
    PEER_IP,
    PORT,
    chunk_list,
    SAVE_FOLDER
)

print("[RESUME DOWNLOAD TEST COMPLETED]")