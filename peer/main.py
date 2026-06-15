# main.py
import os
import threading
from file_chunks_manager import ChunkManager, split_file

# -----------------------------
# Peer Configuration
# -----------------------------
cfg = {
    "id": "peer1",       # Change this to each peer's unique ID
    "port": 5001         # Example port for peer
}

# Initialize Chunk Manager
cm = ChunkManager()

# -----------------------------
# Ask user for file to share
# -----------------------------
while True:
    file_path = input("Enter the full path of the file to share: ").strip()
    
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue
    
    if os.path.isdir(file_path):
        print(f"This is a folder, not a file: {file_path}")
        continue
    
    if os.path.getsize(file_path) == 0:
        print(f"The file is empty: {file_path}")
        continue
    
    # File exists, is not a folder, and has content
    break

# -----------------------------
# Split File into Chunks
# -----------------------------
chunk_size = 1024 * 1024  # 1MB per chunk
file_chunks = split_file(file_path, chunk_size)

print(f"File split into {len(file_chunks)} chunks.")

# -----------------------------
# Add Chunks to Chunk Manager
# -----------------------------
for chunk_name, chunk_data in file_chunks.items():
    cm.add_chunk(chunk_name, chunk_data, cfg["id"])

print("All chunks added successfully!")

# -----------------------------
# (Optional) Parallel Download Worker
# -----------------------------
def download_worker(peer_ip, port, chunk_name, save_folder):
    """
    Worker thread to download one chunk from a peer.
    Replace download_chunk() with your actual P2P download logic.
    """
    # download_chunk(peer_ip, port, chunk_name, save_folder)
    print(f"Downloading {chunk_name} from {peer_ip}:{port} into {save_folder}")