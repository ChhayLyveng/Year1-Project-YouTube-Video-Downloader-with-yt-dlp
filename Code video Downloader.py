from tkinter import *
import yt_dlp    # pip install yt-dlp
from tkinter import messagebox, filedialog

def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Warning", "Please enter a URL.")
        return

   
    download_location = filedialog.askdirectory()
    if not download_location:
        messagebox.showwarning("Warning", "Please select a download location.")
        return

    quality = quality_var.get()
    
    quality_video = {
        "1080p": "137+140",
        "720p": "136+140",
        "480p": "135+140",
        "360p": "134+140",
        "240p": "133+140",
        "144p": "160+140"
    }
    
    video_final_option = {
        'format': quality_video[quality],
        'outtmpl': f'{download_location}/%(title)s.%(ext)s',
    }

    
    with yt_dlp.YoutubeDL(video_final_option) as ydl:
        ydl.download([url])
    
    messagebox.showinfo("Success", "Download completed successfully!")

win = Tk()
win.title("YouTube Video Downloader")
win.geometry("500x300")

Label(win, text="YouTube", font=("Matura MT Script Capitals", 20), fg="red").place(x=50, y=10)
Label(win, text="Video", font=("Matura MT Script Capitals", 20), fg="aquamarine").place(x=175, y=10)
Label(win, text="Downloader", font=("Matura MT Script Capitals", 20), fg="seagreen").place(x=265, y=10)

url_label = Label(win, text="YouTube URL:", font=("AKbalthom HighSchool-Fun", 18), fg="Light blue")
url_label.place(x=10, y=50)

url_entry = Entry(win, width=40)
url_entry.place(x=175, y=55, height=30)

quality_var = StringVar(win)
quality_var.set("1080p")  

quality_label = Label(win, text="Select Quality:", font=("AKbalthom HighSchool-Fun", 18), fg="Light blue")
quality_label.place(x=10, y=100)

quality_video = ["1080p", "720p", "480p", "360p", "240p", "144p"]
quality_menu = OptionMenu(win, quality_var, *quality_video)
quality_menu.place(x=175, y=105, width=100, height=35)

download_button = Button(win, text="Download Video", command=download_video, font=("AKbalthom HighSchool-Fun", 15), fg="gray")
download_button.place(x=285, y=103, width=200, height=35)

Label(win, text="HAVE A NICE DAY ", font=("Franklin Gothic Demi Cond", 20), fg="cadetblue").place(x=100, y=160)

win.mainloop()