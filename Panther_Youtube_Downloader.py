#!/usr/bin/env python
"""
#######################################################
# Panther Youtube Downloader
# Author: Rajender Kumar
# VERSION: 0.1

Panther Youtube Downloader allows you to convert & download video from YouTube, Facebook, Dailymotion, Youku, etc. to Mp3, Mp4 in HD. Panther Youtube Downloader supports downloading all video formats such as: ".3GP", ".FLV", ".MP4", ".OGG", ".WEBM", etc. and many standard audio formats such as: ".MP3", ".WAV", ".MP4A", ".FLAC", ".OPUS", ".VORBIS" , etc. You can easily download thousands of videos from YouTube and other websites. You can also convert and download the video into audio format.  Panther Youtube Downloader is the simple and easy to use downloader which is designed using Tkinter for Windows, Linux and OSX.

#######################################################
"""
version = '0.1'
revision = '0'
######################################################

from tkinter import *
from subprocess import call, Popen, PIPE, STDOUT
from os import listdir, popen, remove, mkdir
from os.path import realpath, isdir
from getpass import getuser
from shutil import move
from time import sleep
from tkinter import messagebox
import os

from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import ttk
from ttkthemes import themed_tk as tk

# import pygame
import threading
import time

class PantherDownloader:
    """
        An example of a youtube downloader app developed using the
        Tkinter GUI.
        """
    def __init__(self, master):
        self.colors = {
            'white': '#FFFFFF',
            'blue': '#2B547E',
            'black': '#000000',
            'red': '#FF3346',
            'green': '#306754',
            'grey': '#E5E4E2',
        }
        self.master = master
        self.master.title("Panther YouTube Downloader")
        self.master.configure(bg="white")
        self.master.geometry("1280x700")
        self.check_wav = IntVar()
        self.check_mp3 = IntVar()
        self.check_m4a = IntVar()
        self.base_url, self.link, self.playing = '', '', ''
        self.file_type, self.f_name = '', ''
        # self.downloads = realpath(__file__)[:-29] + 'downloads/'
        # if not isdir(self.downloads):
        #     mkdir(self.downloads)
        # print(realpath(__file__)[:-29])
        # self.img1 = Image.open(realpath(__file__)[:-29] + 'logo.png')

        # def find_data_file(filename):
        #     if getattr(sys, 'frozen', False):
        #         # The application is frozen
        #         datadir = os.path.dirname(sys.executable)
        #     else:
        #         # The application is not frozen
        #         # Change this bit to match where you store your data files:
        #         datadir = os.path.dirname(__file__)
        #     return os.path.join(datadir, filename)

        self.downloads = os.path.join(os.getcwd()) + "\downloads\\"
        if not isdir(self.downloads):
            mkdir(self.downloads)
        # datadir = os.path.dirname(__file__)
        # print(realpath(__file__)[:-29] + " - printed")
        self.img1 = Image.open(os.path.join(os.getcwd()) + '\logo.png')

        self.img_copy = self.img1.copy()
        self.imagePath1 = ImageTk.PhotoImage(self.img1)
        self.image1 = ttk.Label(logo_frame, image=self.imagePath1)

        # widgets/UI elements for changing theme and select audio or video downloader
        self.theme_label = ttk.Label(
            select_frame,
            text="Change Theme: ", width=57,
            font="Helvetica 10 bold")
        self.theme_option = ttk.Combobox(
            select_frame, values=['itft1', 'scidgrey', 'clam', 'blue', 'kroc', 'aquativo', 'ubuntu', 'equilux', 'scidgreen', 'scidpurple', 'winxpblue', 'vista', 'clearlooks', 'scidblue', 'black', 'arc', 'keramik', 'default', 'scidmint', 'smog', 'winnative', 'xpnative', 'plastik', 'radiance', 'alt', 'scidpink', 'classic', 'elegance', 'scidsand']
, width=57, height=1)
        self.theme_option.bind("<<ComboboxSelected>>", self.themeset)

        self.downloader_label = ttk.Label(
            select_frame,
            text="Select Downloader: ",
            width=57, font="Helvetica 10 bold")
        self.downloader_option = ttk.Combobox(
            select_frame, values=[
                                    "Audio Download",
                                    "Video Download"], width=57, height=1)
        self.downloader_option.bind("<<ComboboxSelected>>", self.downloaderset)
        self.downloader_option.set("Audio Download")

        # Select your filetype for download
        self.filetype_label = ttk.Label(
            control_frame,
            text="Select File-Type: ",
            width=57, font="Helvetica 10 bold")

        self.filetype_option = ttk.Combobox(
            control_frame, values=[ ".wav", ".mp3", ".mp4a", ".flac", ".opus", ".vorbis"], width=57, height=1)
        self.filetype_option.set(".mp3")


        # widgets/UI elements
        self.link_label = ttk.Label(
            control_frame,
            text="Enter your YouTube link: ", width=57,
            font="Helvetica 10 bold")
        self.youtube_link = Text(
            control_frame, fg=self.colors['blue'],
            bg=self.colors['grey'], width=57, height=1)
        self.file_name_label = ttk.Label(
            control_frame,
            text="Enter a name for your file: ",
            width=57, font="Helvetica 10 bold")
        self.file_name = Text(
            control_frame, fg=self.colors['blue'],
            bg=self.colors['grey'], width=57, height=1)

        s = ttk.Style()
        s.configure('my.TButton', font=('Helvetica', 14, 'bold'))

        self.go_button = ttk.Button(
            control_frame, text="START DOWNLOAD", width=48, style='my.TButton', command=self.go)
        self.clear_button = ttk.Button(
            control_frame,
             text="RESET",
            width=48, style='my.TButton',
            command=self.clear)

        self.explorer_label1 = ttk.Label(
            list_frame,
            width=50, text="Downloaded Tracks:")

        self.explorer_label2 = ttk.Label(
            list_frame,
            width=50, text='')
        self.explorer = Listbox(
            list_frame, fg=self.colors['blue'], bg=self.colors['grey'],
            width=100, height=15, highlightcolor=self.colors['green'])

        self.delete_button = ttk.Button(
            list_frame,
             text="DELETE", width=31,
             command=self.delete)
        self.stop_button = ttk.Button(
            list_frame,  text="STOP", width=31,
             command=self.stop)
        self.play_button = ttk.Button(
            list_frame,  text="PLAY", width=31,
             command=self.play)

        self.status_label = ttk.Label(
            statusbar_frame,
            width=60, text="Hello " + getuser() + ",  Welcome to Panther Youtube Downloader", font="Helvetica 14 bold")

        # begin layout placement

        # self.image1.place(relx= 0, rely= 0, relheight= 1, relwidth= 1)
        # self.image11.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.image1.pack(side=LEFT, fill=BOTH, expand=YES)
        self.image1.bind('<Configure>', self._resize_image)


        # self.image11.pack(side=RIGHT, fill=X)

        # self.theme_label.place(relx=0.1, rely=0.2, relheight=0.2, relwidth=0.35)
        # self.theme_option.place(relx=0.55, rely=0.2, relheight=0.2, relwidth=0.35)
        # self.downloader_label.place(relx=0.1, rely=0.6, relheight=0.2, relwidth=0.35)
        # self.downloader_option.place(relx=0.55, rely=0.6, relheight=0.2, relwidth=0.35)

        self.theme_label.place(relx=0.1, rely=0.1, relheight=0.9, relwidth=0.17)
        self.theme_option.place(relx=0.28, rely=0.1, relheight=0.9, relwidth=0.17)
        self.downloader_label.place(relx=0.55, rely=0.1, relheight=0.9, relwidth=0.17)
        self.downloader_option.place(relx=0.73, rely=0.1, relheight=0.9, relwidth=0.17)

        self.link_label.place(relx= 0.1, rely= 0.1, relheight= 0.1, relwidth= 0.35)
        self.youtube_link.place(relx= 0.55, rely= 0.1, relheight= 0.1, relwidth= 0.35)
        self.file_name_label.place(relx= 0.1, rely= 0.3, relheight= 0.1, relwidth= 0.35)
        self.file_name.place(relx= 0.55, rely= 0.3, relheight= 0.1, relwidth= 0.35)
        self.filetype_label.place(relx=0.1, rely=0.5, relheight=0.1, relwidth=0.35)
        self.filetype_option.place(relx=0.55, rely=0.5, relheight=0.1, relwidth=0.35)

        # self.wav.place(relx= 0.1, rely= 0.5, relheight= 0.1, relwidth= 0.35)
        # self.mp3.place(relx= 0.55, rely= 0.5, relheight= 0.1, relwidth= 0.35)
        # self.m4a.place(relx= 0, rely= 0, relheight= 0.1, relwidth= 0.35)

        self.go_button.place(relx= 0.1, rely= 0.7, relheight= 0.17, relwidth= 0.35)
        self.clear_button.place(relx= 0.55, rely= 0.7, relheight= 0.17, relwidth= 0.35)

        self.explorer_label1.place(relx= 0.1, rely= 0.1, relheight= 0.1, relwidth= 0.2)
        self.explorer_label2.place(relx= 0.7, rely= 0.1, relheight= 0.1, relwidth= 0.2)
        self.explorer.place(relx= 0.1, rely= 0.2, relheight= 0.5, relwidth= 0.8)

        self.play_button.place(relx= 0.1, rely= 0.8, relheight= 0.1, relwidth= 0.2)
        self.stop_button.place(relx= 0.4, rely= 0.8, relheight= 0.1, relwidth= 0.2)
        self.delete_button.place(relx= 0.7, rely= 0.8, relheight= 0.1, relwidth= 0.2)

        # self.status_label.place(relx= 0, rely= 0, relheight= 1, relwidth= 1)
        self.status_label.pack(side=BOTTOM, fill=X)
        self.populate_explorer()

    def _resize_image(self, event):
            """
            Resize the image according to size of window.
            :param event: event occured when window is resized.
            :return: None
            """
            new_width = event.width
            new_height = event.height

            self.image = self.img_copy.resize((new_width, new_height))

            self.image12 = ImageTk.PhotoImage(self.image)
            self.image1.configure(image=self.image12)

    def finished(self):
        """
        Update the status bar with "FINISHED DOWNLOAD" when download is complete.
        :param: None
        :return: None
        """
        d = "FINISHED DOWNLOAD"
        for letter in enumerate(d):
            self.set_status_label(d[0:letter[0] + 1])
            self.status_label.update_idletasks()
            sleep(.1)

    def download_audio(self):
        """
        Define the command used to download the audio for a particular video link, then download the audio
        and move it to download folder under the path of Panther youtube downloader.
        :param: None
        :return: None
        """
        aac = self.f_name + '.' + 'aac'
        track = self.f_name + self.file_type
        youtube_cmd = [
            "youtube-dl", self.link, "-f",
            "bestaudio", "--extract-audio",
            "-o", track, "--audio-quality",
            "0", "--audio-format", "aac"
        ]
        cmd = ' '.join(youtube_cmd)
        for std_out in popen(cmd):
            self.set_status_label(std_out)
            self.status_label.update_idletasks()
        ffmpeg_cmd = ["ffmpeg", "-v", "quiet", "-i", aac, track]
        cmd = ' '.join(ffmpeg_cmd)
        for stdout in popen(cmd):
            self.set_status_label(stdout)
            self.status_label.update_idletasks()
        try:
            # if aac:
            #     remove(aac)
            move(track, self.downloads)
            # move(track, os.path.join(os.getcwd()) + '/downloads/')
        except Exception:
            self.set_status_label("ERROR DOWNLOADING")

    def download_video(self):
        """
        Define the command used to download the video for a particular video link, then move it to
        download folder under the path of Panther youtube downloader.
        :param: None
        :return: None
        """
        track = self.f_name + self.file_type
        # youtube_cmd = [
        #     "youtube-dl", self.link, "-f",
        #     self.file_type, "-o", track
        # ]

        youtube_cmd = [
            "youtube-dl", self.link, "-o", track, "-f", "webm"
        ]
        cmd = ' '.join(youtube_cmd)
        for std_out in popen(cmd):
            self.set_status_label(std_out)
            self.status_label.update_idletasks()
        try:
            move(track, self.downloads)
        except Exception:
            self.set_status_label("ERROR DOWNLOADING")

    def populate_explorer(self):
        """
        Populate the listbox (called explorer) with all the audio and video downloaded using Panther
        youtube downloader in a sorted manner.
        :param: None
        :return: None
        """
        self.explorer.delete(0, 'end')
        downloads = sorted(listdir(self.downloads))
        self.explorer.insert("end", *downloads)
        self.set_explorer_status_label(str(self.explorer.size()))

    def go(self):
        """
        Called on the click of "START DOWNLOAD" button. This function check whether video link and file
        name is provided or not, whether downloader type and file type selected or not. It then called the
        particular download function based on the the downloader type ("AUDIO DOWNLOAD",
        "VIDEO DOWNLOAD"). Update status in status-bar accordingly.
        :param: None
        :return: None
        """
        self.link = self.youtube_link.get("1.0", END).strip()
        self.f_name = self.file_name.get("1.0", END).strip()
        self.file_type = self.get_filetype()
        if not self.link or not self.f_name:
            messagebox.showwarning("Must need URL and File Name", "Please provide the URL and desired File Name")
        else:
            if self.file_type is not None:
                current_track = self.f_name + self.file_type
                self.set_status_label('DOWNLOADING ' + current_track)
                self.status_label.update_idletasks()
                if (self.downloader_option.get() == "Video Download"):
                    self.download_video()
                    # self.download()
                    self.populate_explorer()
                    # idx = sorted(listdir(self.downloads)).index(current_track)
                    self.explorer.selection_clear(0, END)
                    # self.explorer.selection_set(idx)
                    self.finished()
                elif (self.downloader_option.get() == "Audio Download"):
                    self.download_audio()
                    self.populate_explorer()
                    idx = sorted(listdir(self.downloads)).index(current_track)
                    self.explorer.selection_clear(0, END)
                    self.explorer.selection_set(idx)
                    self.finished()

    def clear(self):
        """
        Clear the file_name, youtube_link textbox and update the status bar to wish the user.
        :param: None
        :return: None
        """
        self.file_name.delete("1.0", END)
        self.youtube_link.delete("1.0", END)
        self.set_status_label("Hello " + getuser() + ",  Welcome to Panther Youtube Downloader")

    def delete(self):
        """
        Delete the selected audio/ video file from the listbox (explorer) and update the status-bar.
        :param: None
        :return: None
        """
        try:
            track = self.explorer.get(self.explorer.curselection())
            path = self.downloads + track
            remove(path)
            d_message = track + " DELETED"
            self.set_status_label(d_message)
        except Exception:
            message = "Please select a track to delete"
            self.set_status_label(message)
        self.populate_explorer()

    def stop(self):
        """
        Stop the playing audio file and update the status-bar.
        :param: None
        :return: None
        """
        if self.playing:
            self.set_status_label('STOPPING ' + self.playing)
            self.status_label.update_idletasks()
            if os.name == 'nt':
                try:
                    call('taskkill /IM ffplay.exe /F', shell=True)
                except Exception as e:
                    self.set_status_label(e)
            else:
                psaux = []
                for line in popen("ps -aux | grep ffplay"):
                     if 'ffplay' in line:
                         psaux = line.split()
                         break
                try:
                    call('kill ' + psaux[1].strip(), shell=True)
                    # call('taskkill /IM ffplay.exe /F', shell=True)
                except Exception as e:
                    self.set_status_label(e)

    def play(self):
        """
        Play the selected audio file from the explorer and update the status-bar.
        :param: None
        :return: None
        """
        try:
            self.playing = self.explorer.get(self.explorer.curselection())
            self.set_status_label('PLAYING ' + self.playing)
            self.status_label.update_idletasks()
            ffplay = [
                "ffplay", self.downloads + self.playing,
                "-nodisp", "-autoexit"
            ]
            Popen(ffplay, stdout=PIPE, stderr=STDOUT)
        except Exception:
            self.set_status_label("Please select a track to play")

    # def play(self):
    #         pygame.mixer.init()
    #         pygame.mixer.music.load(self.explorer[3])
    #         pygame.mixer.music.play()
    #         #self.playing = self.explorer.get(self.explorer.curselection())
    #         self.set_status_label('PLAYING ' + self.playing)
    #         self.status_label.update_idletasks()
    #         ffplay = [
    #             "ffplay", self.downloads + self.playing,
    #             "-nodisp", "-autoexit"
    #         ]
    #         Popen(ffplay, stdout=PIPE, stderr=STDOUT)
    #     # except Exception:
    #     #     self.set_status_label("Please select a track to play")

    def set_status_label(self, incoming_message1):
        """
        Set the status-bar according to the argument passed.
        :param incoming_message1: Message to display on the status-bar.
        :return: None
        """
        self.status_label.config(text=incoming_message1)

    def set_explorer_status_label(self, incoming_message2):
        """
        Set the explorer label equal to the number of files in the list-box.
        :param incoming_message2: Variable to set the value of label
        :return: None
        """
        incoming_message2 += " Files Found"
        self.explorer_label2.config(text=incoming_message2)

    def themeset(self, event):
        """
        Set the different theme as chosen by the user using Combo-box.
        :param event: event to get the selected theme name from the Combo-box.None
        :return: None
        """
        root.set_theme(self.theme_option.get())

    def downloaderset(self, event):
        """
        Change the values in the file-type Combo-box based on the selection of downloader type i.e. update
        the file-type format according to "AUDIO DOWNLOADER" and "VIDEO DOWNLOADER" selection.
        :param event: variable to get the value of the selected downloader type.
        :return: None
        """
        if(self.downloader_option.get()=="Video Download"):
            value_list = [".3gp", ".flv", ".mp4", ".ogg", ".webm"]
        elif (self.downloader_option.get()=="Audio Download"):
            value_list = [".mp3", ".wav", ".mp4a", ".flac", ".opus", ".vorbis"]
        self.filetype_option.config(values=value_list)

    def get_filetype(self):
        """
        Get the file-type format (.mp3, .mp4, .flv, .ogg etc.) to download.
        :param: None
        :return: None
        """
        if self.filetype_option.get():
            return self.filetype_option.get()
        else:
            messagebox.showwarning("Select File Type", "Please choose a file type")


#root = Tk()
root = tk.ThemedTk() # media player window using tkinter package
root.get_themes()
# print(root.get_themes())
root.set_theme("kroc")
root.minsize(1280,600)
root.iconbitmap('panther.ico')
# root.resizable(False, False)

logo_frame = ttk.Frame(root)
logo_frame.place(relx= 0, rely= 0, relheight= 0.22, relwidth= 1 )

select_frame = Frame(root, bg= "black")
select_frame.place(relx= 0, rely= 0.22, relheight= 0.05, relwidth= 1 )

main_frame = Frame(root, bg= "black")
main_frame.place(relx= 0, rely= 0.27, relheight= 0.7, relwidth= 1 )

control_frame = Frame(main_frame, bg= "black")
control_frame.place(relx= 0, rely= 0, relheight= 0.5, relwidth= 1 )

list_frame = ttk.Frame(main_frame)
list_frame.place(relx= 0, rely= 0.5, relheight= 0.5, relwidth= 1 )

statusbar_frame = ttk.Frame(root)
statusbar_frame.place(relx= 0, rely= 0.97, relheight= 0.03, relwidth= 1 )

panther_downloader = PantherDownloader(root)
root.mainloop()
