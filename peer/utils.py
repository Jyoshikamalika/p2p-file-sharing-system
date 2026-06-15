import hashlib
import os


# -----------------------------
# HASH FUNCTION
# -----------------------------

def calculate_hash(file_path):

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as f:

        while True:

            data = f.read(4096)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()


# -----------------------------
# SPLIT FILE FUNCTION
# -----------------------------

def split_file(
        file_path,
        chunk_size=1024,
        output_folder="chunks"
):

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    chunk_paths = []

    file_name = os.path.basename(file_path)

    with open(file_path, "rb") as f:

        index = 0

        while True:

            chunk = f.read(chunk_size)

            if not chunk:
                break

            chunk_name = f"{file_name}_chunk{index}"

            chunk_path = os.path.join(
                output_folder,
                chunk_name
            )

            with open(chunk_path, "wb") as cf:
                cf.write(chunk)

            chunk_paths.append(chunk_path)

            index += 1

    print(f"[SPLIT DONE] {len(chunk_paths)} chunks created")

    return chunk_paths


# -----------------------------
# COMBINE CHUNKS FUNCTION
# -----------------------------

def combine_chunks(
        chunk_paths,
        output_file
):

    with open(output_file, "wb") as outfile:

        for chunk_path in chunk_paths:

            if chunk_path is None:

                raise FileNotFoundError(
                    "Some chunks failed to download."
                )

            with open(chunk_path, "rb") as infile:

                outfile.write(
                    infile.read()
                )

    print("[FILE COMBINED SUCCESSFULLY]")