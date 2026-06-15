import sys
import os

# Allow importing utils folder
sys.path.append(os.path.abspath(".."))

from utils.chunk_manager import split_file


file_path = "../shared_files/test.txt"
output_folder = "../data/chunks"

chunks, hashes = split_file(
    file_path,
    output_folder
)

print("Chunks created:")
print(chunks)

print("\nChunk hashes:")
print(hashes)