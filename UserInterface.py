import tkinter as tk
from dotenv import load_dotenv
import os
import DiscordBot
import Editor
import discord
from tkinter import filedialog

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


class UserInterface(tk.Tk):

    start_time = 0
    end_time = 0
    video_path = ""
    videoEntry = None
    startTimeEntry = None
    endTimeEntry = None

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        videoLabel = tk.Label(text="Video Path: ")
        videoLabel.grid(row=2, column=1)
        self.videoEntry = tk.Entry(font=40)
        self.videoEntry.grid(row=2, column=2)

        self.startTimeListener = tk.StringVar()
        self.startTimeListener.trace("w", self.startTimeChanged)
        startTimeEntryLabel = tk.Label(text="Start Time: ")
        startTimeEntryLabel.grid(row=3, column=1)
        self.startTimeEntry = tk.Entry(font=40, textvariable=self.startTimeListener)
        self.startTimeEntry.grid(row=3, column=2)

        self.endTimeListener = tk.StringVar()
        self.endTimeListener.trace("w", self.endTimeChanged)
        endTimeEntryLabel = tk.Label(text="End Time: ")
        endTimeEntryLabel.grid(row=4, column=1)
        self.endTimeEntry = tk.Entry(font=40, textvariable=self.endTimeListener)
        self.endTimeEntry.grid(row=4, column=2)
        chooseVideoB = tk.Button(text="Choose Video", font=40, command=self.browsefunc)
        chooseVideoB.grid(row=2, column=4)
        sendGifB = tk.Button(text="Send Gif", font=40, command=self.writeGif)
        sendGifB.grid(row=5, column=4)
        tk.mainloop()

    def browsefunc(self):
        filename = filedialog.askopenfilename(filetypes=(("MP4 Files", "*.mp4"), ("All files", "*.*")))
        self.videoEntry.insert(tk.END, filename)
        self.video_path = self.videoEntry.get()
        print(self.video_path)

    def startTimeChanged(self, *args, **kwargs):
        self.start_time = self.startTimeEntry.get()

    def endTimeChanged(self, *args, **kwargs):
        self.end_time = self.endTimeEntry.get()


    def writeGif(self):
        editor = Editor.Editor(self.video_path, self.start_time, self.end_time)
        editor.writeGif()
        client = DiscordBot.DiscordBot(intents=discord.Intents.default())
        client.run(TOKEN)
