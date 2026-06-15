import tkinter as tk
from tkinter import filedialog, messagebox
import os

from utils import split_file


class P2PGUI:

    def __init__(self, root):

        self.root = root
        self.root.title("P2P File Sharing GUI")

        self.file_path = None
        self.chunks = []

        # Title
        self.label = tk.Label(
            root,
            text="P2P File Sharing System",
            font=("Arial", 16)
        )
        self.label.pack(pady=10)

        # Select File Button
        self.select_button = tk.Button(
            root,
            text="Select File",
            command=self.select_file,
            width=20
        )
        self.select_button.pack(pady=5)

        # Status Label
        self.status_label = tk.Label(
            root,
            text="No file selected",
            fg="blue"
        )
        self.status_label.pack(pady=5)

        # Chunk List Display
        self.chunk_box = tk.Text(
            root,
            height=10,
            width=50
        )
        self.chunk_box.pack(pady=10)

        # Exit Button
        self.exit_button = tk.Button(
            root,
            text="Exit",
            command=root.quit,
            width=20
        )
        self.exit_button.pack(pady=5)


    def select_file(self):

        file_path = filedialog.askopenfilename()

        if not file_path:
            return

        self.file_path = file_path

        self.status_label.config(
            text=f"Selected: {os.path.basename(file_path)}"
        )

        try:

            # Split file
            self.chunks = split_file(
                file_path,
                chunk_size=1024,
                output_folder="chunks"
            )

            self.display_chunks()

            messagebox.showinfo(
                "Success",
                "File split into chunks successfully!"
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )


    def display_chunks(self):

        self.chunk_box.delete(1.0, tk.END)

        for chunk_path in self.chunks:

            chunk_name = os.path.basename(
                chunk_path
            )

            self.chunk_box.insert(
                tk.END,
                chunk_name + "\n"
            )


# Run GUI
if __name__ == "__main__":

    root = tk.Tk()

    app = P2PGUI(root)

    root.mainloop()