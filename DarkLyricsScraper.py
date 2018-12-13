from tkinter import *
from tkinter import ttk
from darklyrics import *

window = Tk()
window.title("DarkLyric Scraper")

artistPrompt = Label(window, text="What is the Artist you are looking for?")
artistPrompt.grid(column=0, row=1)

artistName = StringVar()
artistEntry = Entry(window, width=30, textvariable=artistName)
artistEntry.grid(column=1, row=1)
songName = StringVar()
albumName = StringVar()
albumsCB = ttk.Combobox(window, width=27, state="readonly", textvariable=albumName)
songsCB = ttk.Combobox(window, width=27, state="readonly", textvariable=songName)

lyrics = StringVar()
lyricsLabel = Label(window, text="", textvariable=lyrics)
lyricsLabel.grid(column=0, row=4)

blah = get_songs("kayo dot")
print(blah)

def getAlbums(self):
    try:
        albumsCB['values'] = get_albums(artistName.get())
        albumPrompt.grid(column=0, row=2)
        albumsCB.grid(column=1, row=2)
        albumsCB.configure(state="readonly")
        artistEntry.configure(state=DISABLED)
        unlockBtn.grid(column=2, row=1)
        albumsCB.focus()
    except LyricsNotFound:
        lyrics.set("Artist not found... Check Spelling")
        return


def getSongs(self):
    songPrompt.grid(column=0, row=3)
    songsCB['values'] = get_songs(artistName.get(), albumName.get())
    songsCB.grid(column=1, row=3)
    songsCB.configure(state="readonly")
    songsCB.focus()


def displayLyrics(self):
    lyrics.set(get_lyrics(songName.get(), artistName.get()))


def unlockArtist():
    artistEntry.configure(state="normal")
    artistName.set("")
    albumName.set("")
    albumsCB.configure(state=DISABLED)
    songName.set("")
    songsCB.configure(state=DISABLED)


songPrompt = Label(window, text="What is the Song you are looking for?")
unlockBtn = Button(window, text="New Artist", command=unlockArtist)
albumPrompt = Label(window, text="What is the Album you are looking for?")

artistEntry.bind("<Return>", getAlbums)
albumsCB.bind("<<ComboboxSelected>>", getSongs)
songsCB.bind("<<ComboboxSelected>>", displayLyrics)


artistEntry.focus()

window.mainloop()
