import tkinter as tk
from tkinter import filedialog
from pygame import mixer

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("600x400")

        self.dsply = tk.Frame(self.root)
        self.dsply.pack(fill=tk.BOTH, expand=True)

        self.sdbdsply = tk.Frame(self.root, width=200, bg='lightgrey')
        self.sdbdsply.pack(side=tk.RIGHT, fill=tk.Y)

        self.mscbtn = tk.Button(self.dsply, text="Add Music", command=self.add_music)
        self.mscbtn.pack(pady=10)

        self.music_listbox = tk.Listbox(self.dsply, selectmode=tk.MULTIPLE)
        self.music_listbox.pack(fill=tk.BOTH, expand=True)

        self.media_controls = tk.Frame(self.root, bg='grey')
        self.media_controls.pack(side=tk.BOTTOM, fill=tk.X)

        self.play_button = tk.Button(self.media_controls, text="Play", command=self.play_music)
        self.play_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(self.media_controls, text="Stop", command=self.stop_music)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        mixer.init()

    def add_music(self):
        files = filedialog.askopenfilenames(filetypes=[("Music Files", "*.mp3 *.wav")])
        for file in files:
            self.music_listbox.insert(tk.END, file)

    def play_music(self):
        selected_files = self.music_listbox.curselection()
        if selected_files:
            file = self.music_listbox.get(selected_files[0])
            mixer.music.load(file)
            mixer.music.play()
            self.update_sidebar(file)

    def stop_music(self):
        mixer.music.stop()

    def update_sidebar(self, file):
        for widget in self.sdbdsply.winfo_children():
            widget.destroy()
        music_label = tk.Label(self.sdbdsply, text=file, bg='lightgrey')
        music_label.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()