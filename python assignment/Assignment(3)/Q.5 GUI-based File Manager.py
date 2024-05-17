# Q.5 Create a GUI-based file manager that allows users to browse directories, view files, and perform basic file operations like copy, move, and delete.

import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import os

class FileManager:
    def __init__(self, root):
        self.root = root
        self.root.title("File Manager")

        self.path_label = tk.Label(root, text="Directory Path")
        self.path_label.pack()

        self.path_entry = tk.Entry(root, width=50)
        self.path_entry.pack()

        self.browse_button = tk.Button(root, text="Browse", command=self.browse_directory)
        self.browse_button.pack()

        self.listbox = tk.Listbox(root, width=100, height=20)
        self.listbox.pack()

        self.copy_button = tk.Button(root, text="Copy", command=self.copy_file)
        self.copy_button.pack()

        self.move_button = tk.Button(root, text="Move", command=self.move_file)
        self.move_button.pack()

        self.delete_button = tk.Button(root, text="Delete", command=self.delete_file)
        self.delete_button.pack()

    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, directory)
            self.list_files(directory)

    def list_files(self, directory):
        self.listbox.delete(0, tk.END)
        for file in os.listdir(directory):
            self.listbox.insert(tk.END, file)

    def copy_file(self):
        selected_file = self.listbox.get(tk.ACTIVE)
        src = os.path.join(self.path_entry.get(), selected_file)
        dest = filedialog.askdirectory()
        if dest:
            shutil.copy(src, dest)
            messagebox.showinfo("Info", "File copied successfully")

    def move_file(self):
        selected_file = self.listbox.get(tk.ACTIVE)
        src = os.path.join(self.path_entry.get(), selected_file)
        dest = filedialog.askdirectory()
        if dest:
            shutil.move(src, dest)
            self.list_files(self.path_entry.get())
            messagebox.showinfo("Info", "File moved successfully")

    def delete_file(self):
        selected_file = self.listbox.get(tk.ACTIVE)
        file_path = os.path.join(self.path_entry.get(), selected_file)
        if os.path.exists(file_path):
            os.remove(file_path)
            self.list_files(self.path_entry.get())
            messagebox.showinfo("Info", "File deleted successfully")

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    file_manager = FileManager(root)
    root.mainloop()
