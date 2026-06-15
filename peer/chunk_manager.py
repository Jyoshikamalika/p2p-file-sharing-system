from collections import defaultdict
from utils import compute_hash

class ChunkManager:
    def __init__(self):
        self.chunk_map = {}
        self.chunk_availability = defaultdict(set)
        self.chunk_hash = {}

    def add_chunk(self, chunk_name, data, peer_id):
        self.chunk_map[chunk_name] = data
        self.chunk_availability[chunk_name].add(peer_id)
        if chunk_name not in self.chunk_hash:
            self.chunk_hash[chunk_name] = compute_hash(data)

    def update_peer_chunks(self, peer_id, peer_chunks):
        for chunk_name in peer_chunks:
            self.chunk_availability[chunk_name].add(peer_id)

    def get_rarest_chunk(self, owned_chunks):
        rarest_chunk = None
        min_count = float('inf')
        for chunk, peers in self.chunk_availability.items():
            if chunk in owned_chunks:
                continue
            if 0 < len(peers) < min_count:
                min_count = len(peers)
                rarest_chunk = chunk
        return rarest_chunk

    def get_chunk_hash(self, chunk_name):
        return self.chunk_hash.get(chunk_name)

    def has_chunk(self, chunk_name):
        return chunk_name in self.chunk_map