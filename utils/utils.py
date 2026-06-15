import hashlib
import os

def compute_hash(data):
    """
    Returns SHA-256 hash of the data
    """
    return hashlib.sha256(data).hexdigest()

def split_file(file_path, chunk_size=1024*512):
    """
    Split a file into chunks (default 512KB each)
    Returns a dict: {chunk_name: bytes}
    """
    chunks = {}
    with open(file_path, "rb") as f:
        idx = 0
        while True:
            data = f.read(chunk_size)
            if not data:
                break
            chunk_name = f"chunk{idx}"
            chunks[chunk_name] = data
            idx += 1
    return chunks

def combine_chunks(chunks_dict, output_path):
    """
    Combine chunks back into a single file
    """
    with open(output_path, "wb") as f:
        for idx in range(len(chunks_dict)):
            chunk_name = f"chunk{idx}"
            f.write(chunks_dict[chunk_name])