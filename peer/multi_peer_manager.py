class MultiPeerManager:
    def __init__(self, self_peer_id):
        self.self_peer_id = self_peer_id
        self.peers = {}

    def add_peer(self, peer_id, ip, port, chunks=None):
        if chunks is None:
            chunks = set()
        self.peers[peer_id] = {"ip": ip, "port": port, "chunks": set(chunks)}

    def remove_peer(self, peer_id):
        if peer_id in self.peers:
            del self.peers[peer_id]

    def update_peer_chunks(self, peer_id, chunk_list):
        if peer_id in self.peers:
            self.peers[peer_id]["chunks"].update(chunk_list)

    def get_peer_for_chunk(self, chunk_name, chunk_manager):
        available_peers = chunk_manager.chunk_availability.get(chunk_name, set())
        available_peers = available_peers - {self_peer_id}
        if not available_peers:
            return None
        peer_id = next(iter(available_peers))
        return self.peers.get(peer_id)