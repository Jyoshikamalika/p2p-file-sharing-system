import sys
import os

# Allow importing utils folder
sys.path.append(os.path.abspath(".."))

from utils.chunk_manager import merge_chunks

chunk_folder = "../downloads"

output_file = "../downloads/reconstructed_test.txt"

merge_chunks(
    chunk_folder,
    output_file
)

print("[FILE RECONSTRUCTED SUCCESSFULLY]")