import os
from multi_peer_download import multi_peer_download


def get_missing_chunks(chunk_list, save_folder):
    """
    Returns list of missing chunks.
    """

    missing = []

    for chunk in chunk_list:

        chunk_path = os.path.join(
            save_folder,
            chunk
        )

        if not os.path.exists(chunk_path):

            missing.append(chunk)

    return missing


def resume_download(peer_ip, port, chunk_list, save_folder):
    """
    Resume download for missing chunks.
    """

    missing_chunks = get_missing_chunks(
        chunk_list,
        save_folder
    )

    if not missing_chunks:

        print("[NO MISSING CHUNKS]")
        return

    print(
        "[RESUMING DOWNLOAD FOR:]",
        missing_chunks
    )

    peer_list = []

    for chunk in missing_chunks:

        peer_list.append(
            (peer_ip, port, chunk)
        )

    multi_peer_download(
        peer_list,
        save_folder
    )