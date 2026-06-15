# file_chunks_manager.py
import os

class ChunkManager:
    def __init__(self):
        self.chunks = {}  # Stores all chunks by name

    def add_chunk(self, chunk_name, data, peer_id):
        # Store the chunk with a tuple of (data, peer_id)
        self.chunks[chunk_name] = (data, peer_id)
        print(f"Chunk {chunk_name} added by {peer_id}")

def split_file(file_path, chunk_size=1024*1024):  # 1MB default
    """
    Splits a file into chunks and returns a dict with keys 'chunk0', 'chunk1', etc.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found!")

    file_chunks = {}
    with open(file_path, 'rb') as f:
        i = 0
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            chunk_name = f"chunk{i}"
            file_chunks[chunk_name] = chunk
            i += 1
    return file_chunks