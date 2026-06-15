import hashlib
import os


def calculate_hash(file_path):
    """
    Calculates SHA-256 hash of file.
    """

    hasher = hashlib.sha256()

    with open(file_path, "rb") as file:

        while True:

            data = file.read(1024)

            if not data:
                break

            hasher.update(data)

    return hasher.hexdigest()


def verify_chunks(chunk_folder, original_hashes):
    """
    Verifies downloaded chunks using stored hashes.
    """

    chunk_files = [
        f for f in os.listdir(chunk_folder)
        if f.startswith("chunk_")
    ]

    chunk_files = sorted(
        chunk_files,
        key=lambda x: int(x.split("_")[1])
    )

    verified = True

    for i, chunk_file in enumerate(chunk_files):

        chunk_path = os.path.join(
            chunk_folder,
            chunk_file
        )

        new_hash = calculate_hash(chunk_path)

        if new_hash != original_hashes[i]:

            print(
                f"[HASH MISMATCH] {chunk_file}"
            )

            verified = False

        else:

            print(
                f"[HASH VERIFIED] {chunk_file}"
            )

    return verified