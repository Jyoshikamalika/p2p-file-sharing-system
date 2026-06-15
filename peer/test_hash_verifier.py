import sys
import os

sys.path.append(os.path.abspath(".."))

from utils.chunk_manager import generate_chunk_hashes
from hash_verifier import verify_chunks

chunk_folder = "../downloads"

# Generate original hashes
original_hashes = generate_chunk_hashes(
    chunk_folder
)

# Verify hashes
result = verify_chunks(
    chunk_folder,
    original_hashes
)

if result:

    print("[ALL CHUNKS VERIFIED SUCCESSFULLY]")

else:

    print("[CHUNK VERIFICATION FAILED]")