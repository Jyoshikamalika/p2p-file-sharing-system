from utils import split_file

# File to split
file_path = "myfile.txt"

# Split file into chunks
chunks = split_file(file_path)

print("\nChunk Hashes:\n")

for chunk_path, chunk_hash in chunks:

    chunk_name = chunk_path.split("\\")[-1]

    print(
        f'"{chunk_name}": "{chunk_hash}",'
    )