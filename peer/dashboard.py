import tkinter as tk
from tkinter import ttk

class Dashboard:
    def __init__(self, peers):
        self.peers = peers
        self.root = tk.Tk()
        self.root.title("P2P Dashboard")

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both')

        self.peer_vars = {}
        for peer in self.peers:
            frame = ttk.Frame(self.notebook)
            self.notebook.add(frame, text=peer["id"])

            label_var = tk.StringVar()
            label_var.set("Initializing...")
            ttk.Label(frame, textvariable=label_var).pack(pady=5)

            tree = ttk.Treeview(frame, columns=("Status",), show="headings")
            tree.heading("Status", text="Status")
            tree.pack(expand=True, fill='both', padx=10, pady=10)

            speed_var = tk.StringVar()
            speed_var.set("Download: 0 B/s | Upload: 0 B/s")
            ttk.Label(frame, textvariable=speed_var).pack(pady=5)

            self.peer_vars[peer["id"]] = {"label_var": label_var, "tree": tree, "speed_var": speed_var}

        self.update_gui_loop()

    def update_gui_loop(self):
        for peer in self.peers:
            cm = peer["chunk_manager"]
            dc = peer["download_client"]
            peer_id = peer["id"]

            owned = set(cm.chunk_map.keys())
            total_chunks = len(cm.chunk_availability)
            self.peer_vars[peer_id]["label_var"].set(f"Downloaded {len(owned)}/{total_chunks} chunks")

            tree = self.peer_vars[peer_id]["tree"]
            tree.delete(*tree.get_children())
            for chunk in cm.chunk_availability:
                status = "✅" if chunk in owned else "❌"
                tree.insert("", "end", values=(chunk, status))

            self.peer_vars[peer_id]["speed_var"].set(
                f"Download: {dc.download_speed:.1f} B/s | Upload: {dc.upload_speed:.1f} B/s"
            )

        self.root.after(1000, self.update_gui_loop)

    def run(self):
        self.root.mainloop()