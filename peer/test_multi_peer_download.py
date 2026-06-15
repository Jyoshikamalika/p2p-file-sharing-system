from multi_peer_download import multi_peer_download

# List of peers and chunks
peer_list = [

    ("127.0.0.1", 7001, "chunk_0")

]

SAVE_FOLDER = "../downloads"

multi_peer_download(
    peer_list,
    SAVE_FOLDER
)

print("[MULTI-PEER TEST FINISHED]")