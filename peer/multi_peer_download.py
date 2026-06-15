import socket
import threading
import os

from utils import combine_chunks, calculate_hash


def download_chunk(peer_ip, peer_port,
                   chunk_name,
                   chunk_hash,
                   download_dir):

    try:
        client = socket.socket()
        client.connect((peer_ip, peer_port))

        # Request chunk
        client.send(chunk_name.encode())

        chunk_path = os.path.join(
            download_dir,
            chunk_name
        )

        with open(chunk_path, "wb") as f:
            while True:
                data = client.recv(4096)
                if not data:
                    break
                f.write(data)

        client.close()

        # Verify hash
        received_hash = calculate_hash(chunk_path)

        if received_hash != chunk_hash:
            raise ValueError(
                f"Hash mismatch for {chunk_path}"
            )

        print(
            f"[DOWNLOADED] {chunk_name} "
            f"from {peer_port}"
        )

        return chunk_path

    except Exception as e:
        print(
            f"[FAILED] {chunk_name} "
            f"from {peer_port}: {e}"
        )
        return None


def parallel_multi_peer_download(
        peers,
        chunk_names,
        chunk_hashes,
        output_file
):

    download_dir = "downloads"

    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    chunk_paths = [None] * len(chunk_names)

    downloaded_count = 0
    total_chunks = len(chunk_names)

    lock = threading.Lock()

    def worker(index):

        nonlocal downloaded_count

        chunk_name = chunk_names[index]
        chunk_hash = chunk_hashes[chunk_name]

        peer = peers[index % len(peers)]

        peer_ip = peer["ip"]
        peer_port = peer["port"]

        path = download_chunk(
            peer_ip,
            peer_port,
            chunk_name,
            chunk_hash,
            download_dir
        )

        if path:

            chunk_paths[index] = path

            with lock:

                downloaded_count += 1

                percent = int(
                    (downloaded_count /
                     total_chunks) * 100
                )

                bar_length = 20

                filled_length = int(
                    bar_length *
                    downloaded_count //
                    total_chunks
                )

                bar = (
                    "█" * filled_length +
                    "░" *
                    (bar_length - filled_length)
                )

                print(
                    f"Progress: "
                    f"{downloaded_count}/"
                    f"{total_chunks} "
                    f"({percent}%)"
                )

                print(f"[{bar}]")

    threads = []

    for i in range(len(chunk_names)):

        t = threading.Thread(
            target=worker,
            args=(i,)
        )

        threads.append(t)

        t.start()

    for t in threads:
        t.join()

    print("[ALL CHUNKS DOWNLOADED]")

    # Combine chunks
    combine_chunks(
        chunk_paths,
        output_file
    )

    print(
        "[FILE COMBINED SUCCESSFULLY]"
    )