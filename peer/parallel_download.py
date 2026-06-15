import threading
from download_client import download_chunk

def parallel_download(peers_dict, progress_callback=None, max_threads=10):
    """Download chunks in parallel from multiple peers."""
    threads = []
    semaphore = threading.Semaphore(max_threads)

    def worker(chunk_name, peer_list):
        with semaphore:
            success = False
            for ip, port in peer_list:
                if download_chunk(ip, port, chunk_name):
                    success = True
                    break
            if progress_callback:
                progress_callback(chunk_name, success)

    for chunk_name, peer_list in peers_dict.items():
        t = threading.Thread(target=worker, args=(chunk_name, peer_list))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()