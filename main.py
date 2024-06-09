import os
import shutil
import tkinter as tk
from tkinter import filedialog


class BackupApp(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Backup App")
        self.geometry("400x200")

        self.source_label = tk.Label(self, text="Source")
        self.source_label.pack()
        self.source_entry = tk.Entry(self, width=50)
        self.source_entry.pack()
        self.source_button = tk.Button(self, text="Browse", command=self.browse_source)
        self.source_button.pack()

        self.destination_label = tk.Label(self, text="Destination")
        self.destination_label.pack()
        self.destination_entry = tk.Entry(self, width=50)
        self.destination_entry.pack()
        self.destination_button = tk.Button(self, text="Browse", command=self.browse_destination)
        self.destination_button.pack()

        self.backup_button = tk.Button(self, text="Backup Now", command=self.backup)
        self.backup_button.pack()

    def browse_source(self):
        self.source_entry.delete(0, tk.END)
        self.source_entry.insert(0, filedialog.askdirectory())

    def browse_destination(self):
        self.destination_entry.delete(0, tk.END)
        self.destination_entry.insert(0, filedialog.askdirectory())

    def backup(self):
        src = self.source_entry.get()
        dst = self.destination_entry.get()
        self.backup_files(src, dst)
        tk.messagebox.showinfo("Backup App", "Backup completed successfully!")


    def backup_files(self, src, dst):
        shutil.copytree(src, dst)

if __name__ == "__main__":
    app = BackupApp()
    app.mainloop()