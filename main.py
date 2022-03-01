from tkinter import *
from tkinter import filedialog, messagebox
from pytube import YouTube
import os


class YouTubeDownloader:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("600x500")
        self.root.title("YouTube Downloader")
        self.root.tk.call('wm', 'iconphoto', self.root._w, PhotoImage(file="Pictures/yt.png"))
        self.root.resizable(0, 0)  # Window's resize feature is disabled


        self.url = StringVar()
        self.dest = StringVar()


        self.canvas = Canvas(self.root, bg="red", height=200, width=200)
        self.filename = PhotoImage(file="Pictures/background.png")
        self.bg_label = Label(self.root, image=self.filename)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)


        self.link_label = Label(self.root, text="YouTube URL:", bg="#8b0000", fg="white", width=15, height=2)
        self.link_label.place(relx = 0.24, rely = 0.5, anchor = 'center')

        self.link_text = Entry(self.root, width=40, textvariable=self.url, font=("Calibri 12"))
        self.link_text.place(relx = 0.64, rely = 0.5, anchor = 'center', height=36)


        self.destination_label = Label(self.root, text="Destination:", bg="#ff8c00", fg="white", width=15, height=2)
        self.destination_label.place(relx = 0.24, rely = 0.65, anchor = 'center')

        self.destination_text = Entry(self.root, width=40, textvariable=self.dest, font=("Calibri 12"))
        self.destination_text.place(relx = 0.64, rely = 0.65, anchor = 'center', height=36)


        self.download_but = Button(self.root, text="Download", command=self.download_video, width=10, bg="#ffa500", activebackground="#ff8c00")
        self.download_but.place(relx = 0.42, rely = 0.78, anchor = 'center', height=36)

        self.browse_but = Button(self.root, text="Browse", command=self.browse, width=10, bg="#ffa500", activebackground="#ff8c00")
        self.browse_but.place(relx = 0.60, rely = 0.78, anchor = 'center', height=36)


        self.canvas.pack()

        self.root.mainloop()

    
    def browse(self):
        download_dir = filedialog.askdirectory(initialdir="Yoru Directory Path")
        self.dest.set(download_dir)

    def download_video(self):
        try:
            if (os.path.isdir(folder := self.dest.get()) == True):
                video = YouTube(url=self.url.get())
                video = video.streams.get_highest_resolution()
                video.download(folder)

                messagebox.showinfo("Success!", f'Successfully downloaded "{video.title}"\n at {folder}')
            else:
                messagebox.showerror("Fail!", f'Directory not found!')

        except:
            messagebox.showerror("Fail!", f'Video not found!')


if __name__ == "__main__":
    YouTubeDownloader()