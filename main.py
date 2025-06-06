# main.py

import os
import threading
import tkinter as tk
from tkinter import ttk, messagebox
from pynput import keyboard
import pygame

SOUND_DIR = "sounds"
DEFAULT_SOUND = "click.wav"

pygame.mixer.init()

def get_sound_files():
    if not os.path.exists(SOUND_DIR):
        os.makedirs(SOUND_DIR)
    return [f for f in os.listdir(SOUND_DIR) if f.endswith(".wav")]

class KeyboardSoundEmulator:
    def __init__(self):
        self.current_sound = DEFAULT_SOUND
        self.listener = None
        self.running = False
        self.sound_lock = threading.Lock()
        self.load_sound(self.current_sound)

    def load_sound(self, sound_file):
        with self.sound_lock:
            try:
                path = os.path.join(SOUND_DIR, sound_file)
                self.sound = pygame.mixer.Sound(path)
            except Exception as e:
                print(f"Error loading sound: {e}")
                self.sound = None

    def play_sound(self):
        if self.sound:
            with self.sound_lock:
                self.sound.play()

    def on_key_press(self, key):
        if key == keyboard.Key.esc:
            self.stop()
            return False
        threading.Thread(target=self.play_sound).start()

    def start(self):
        if self.running:
            return
        self.running = True
        self.listener = keyboard.Listener(on_press=self.on_key_press)
        self.listener.start()

    def stop(self):
        self.running = False
        if self.listener:
            self.listener.stop()
            self.listener = None

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Keyboard Sound Emulator")
        self.root.geometry("350x150")
        self.kse = KeyboardSoundEmulator()
        self.build_ui()
        self.update_sound_options()

    def build_ui(self):
        self.style = ttk.Style()
        self.style.configure("TButton", padding=6)

        ttk.Label(self.root, text="Select Sound Profile:").pack(pady=5)
        self.sound_var = tk.StringVar()
        self.dropdown = ttk.Combobox(self.root, textvariable=self.sound_var, state="readonly")
        self.dropdown.pack()

        ttk.Button(self.root, text="Apply Sound", command=self.apply_sound).pack(pady=5)

        self.toggle_btn = ttk.Button(self.root, text="Start Sound Emulation", command=self.toggle)
        self.toggle_btn.pack(pady=5)

    def update_sound_options(self):
        files = get_sound_files()
        if not files:
            messagebox.showwarning("Missing Sounds", f"No .wav files found in '{SOUND_DIR}' folder.")
        self.dropdown['values'] = files
        self.sound_var.set(DEFAULT_SOUND if DEFAULT_SOUND in files else (files[0] if files else ""))

    def apply_sound(self):
        selected = self.sound_var.get()
        self.kse.load_sound(selected)

    def toggle(self):
        if self.kse.running:
            self.kse.stop()
            self.toggle_btn.config(text="Start Sound Emulation")
        else:
            self.kse.start()
            self.toggle_btn.config(text="Stop Sound Emulation")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.protocol("WM_DELETE_WINDOW", root.quit)
    root.mainloop()
