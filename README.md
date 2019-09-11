# Panther_Youtube_Downloader

> Panther Youtube Downloader allows you to convert & download video from YouTube, Facebook, Dailymotion, Youku, etc. to Mp3, Mp4 in HD. Panther Youtube Downloader supports downloading all video formats such as: ".3GP", ".FLV", ".MP4", ".OGG", ".WEBM", etc. and many standard audio formats such as: ".MP3", ".WAV", ".MP4A", ".FLAC", ".OPUS", ".VORBIS" , etc. You can easily download thousands of videos from YouTube and other websites. You can also convert and download the video into audio format.  Panther Youtube Downloader is the simple and easy to use downloader which is designed using Tkinter for Windows, Linux and OSX.



<p align="center">
  <img src="https://user-images.githubusercontent.com/35782113/63805007-77d51f80-c8e6-11e9-8085-32d1c0b93943.png">
</p>



## Example 

&nbsp;

[![Calculator in use ](https://user-images.githubusercontent.com/35782113/63805012-786db600-c8e6-11e9-9e56-8eefbc18b6d3.gif)]()
&nbsp;

&nbsp;

------

## Table of Contents 

- [Panther_Youtube_Downloader](#pantheryoutubedownloader)
  * [Example](#example)
  * [Table of Contents](#table-of-contents)
  * [Getting Started](#getting-started)
    + [Prerequisites](#prerequisites)
    + [Clone](#clone)
    + [Running the Panther Youtube Downloader](#running-the-panther-youtube-downloader)
  * [Building the Windows installer](#building-the-windows-installer)
    + [Using pyinstaller](#using-pyinstaller)
    + [Using CX_FREEZE](#using-cxfreeze)
      - [Writing setup.py:](#writing-setuppy)
      - [Creating the Package:](#creating-the-package)
  * [Features](#features)
  * [How it works ? (Instructions)](#how-it-works--instructions)
  * [Usage](#usage)
      - [Downloading the audio and video from a youtube link:](#downloading-the-audio-and-video-from-a-youtube-link)
      - [Playing the audio directly from the "Panther Youtube Downloader":](#playing-the-audio-directly-from-the-panther-youtube-downloader)
        * [Changing the theme of the "Panther Youtube Downloader":](#changing-the-theme-of-the-panther-youtube-downloader)
  * [Executable](#executable)
      - [Version: v0.1](#version-v01)
  * [To-do](#to-do)
  * [Documentation](#documentation)
    + [Making the layout of the Panther Youtube Downloader](#making-the-layout-of-the-panther-youtube-downloader)
    + [Functions used in the Panther Youtube Downloader](#functions-used-in-the-panther-youtube-downloader)
  * [Tests](#tests)
  * [Contributing](#contributing)
  * [FAQ](#faq)
  * [Support](#support)
  * [Donations](#donations)
  * [License](#license)

------

## Getting Started

### Prerequisites

Although, I used the following software (with their corresponding versions) to run this program, Panther Youtube Downloader should be run with any version of Python 3 +. We need the following packages to run this program:

- Python 3.7.4 (This program should work fine with any installation of Python3+. Although, I used Python 3.7.4)
- python3-tk (apt-get install python-tk or pip install python-tk)
- youtube-dl==2019.8.13 (apt-get install youtube-dl==2019.8.13 or pip install youtube-dl==2019.8.13)
- ffmpeg==1.4 (apt-get install ffmpeg==1.4 or pip install ffmpeg==1.4)
- ffprobe==0.5 (apt-get install ffprobe==0.5 or pip install ffprobe==0.5)
- Pillow==6.1.0 (apt-get install Pillow==6.1.0 or pip install Pillow==6.1.0)
- ttkthemes==2.3.0 (apt-get install ttkthemes==2.3.0 or pip install ttkthemes==2.3.0)

> In addition to above, you need to put the following 3 files (ffmpeg ffplay ffprobe ) to the path where window can find it (after unziping it). This simply means put the following files in folder such as: "**C:\Windows\system32**" or "**C:\Windows**" or make a new folder, copy these 3 files there and add the path of that folder in window "path" environment variable (**Control Panel** >> **System** >> **Advanced system settings** >> **Environment Variables** >> **Path**).
>
> Here is the link: https://ffbinaries.com/downloads
>
> Here is the another link of latest version of ffmpeg, ffplay and ffprobe: https://ffmpeg.zeranoe.com/builds/

### Clone

- Clone this repo to your local machine using `https://github.com/rajenderk18/Panther_Youtube_Downloader.git`

### Running the Panther Youtube Downloader

You can run the program by following the below commands:

```
$ git clone https://github.com/rajenderk18/Panther_Youtube_Downloader.git
$ cd Panther_Youtube_Downloader
$ chmod +x Panther_Youtube_Downloader.py
$ ./Panther_Youtube_Downloader.py

```

or run the Panther_Youtube_Downloader.py using python in terminal or command prompt using below command:

```
python Panther_Youtube_Downloader.py
```

------

## Building the Windows installer

### Using pyinstaller

I use the pyinstaller for building the window installer for the Panther Youtube Downloader. You can install the pyinstaller by using the following command:

```
pip install pyinstaller
```

You will need pip to install the pyinstaller. After installing the pyinstaller, you have to run this command to create the window installer (.exe file) for the calculator:

```
pyinstaller --onefile -w Panther_Youtube_Downloader.py
```

When the command executed completely, you will see two folders (build and dist) in the folder of your project. Build folder contains the binary of your Panther_Youtube_Downloader program and you don't need them. Your installer (.exe file) is in the dist folder. Double click on it to check whether it is running or not. If it does not work, that means it is not able to find the required files like images, logo, icon, etc. In this case, you just have to copy the exe file and paste it outside the dist folder. Now it should work without any problem.

### Using CX_FREEZE

Some-time executable file built using pyinstaller give some error and it is difficult for many people to solve the error. **pyinstaller** had an issue with missing Universal CRT that kept erroring it out (this issue still seems unresolved, and the discussion can be found [here](https://github.com/pyinstaller/pyinstaller/issues/1566) on pyinstaller's GitHub).

 **cx_Freeze** is straightforward to use and its documentation is very clear. Here are the steps that should performed before building executable:

1. ***Place all of your code files in one folder.*** 
2. ***Correct any now-faulty import statements.*** 
3. (Optional) If you're using an icon, you can keep icon file in a separate icon folder. This just makes the final package look cleaner, as you don't have two items with the same icon creating confusion. But as this program has only one icon and one image, so I keep both in the same folder as the code.
4. ***Test your program*** once you've tweaked your imports and the structure is all set. If not: debug time.
5. ***Create a Python script named setup.py*** ***in your folder*****.** This script is the easiest way to compile with cx_Freeze, and contains all of the instructions necessary to get your file in the format you want, as well as some extra code needed for cx_Freeze to cooperate with Tkinter. 
6. ***Make sure cx_Freeze is installed.*** I just did pip install cx_Freeze in the console.

#### Writing setup.py:

Open your favorite text editor/IDE, and write something like the following into it (every line is essential):

```python
import sys
from cx_Freeze import setup, Executable
import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

# Dependencies are automatically detected, but it might need fine tuning.
additional_modules = []

build_exe_options = {"includes": additional_modules,
                      #"packages": ["youtube-dl", "ttkthemes", "Pillow", "os", "shutil", "subprocess", "getpass", "time", "os.path"],
                     #"excludes": ['tkinter'],
                     "include_files": [
                         os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
                         os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
                         'panther.ico', 'logo.png']}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="Panther_Youtube_Downloader",
      version="1.0",
      description="Panther Youtube Downloader",
      options={"build_exe": build_exe_options},
      executables=[Executable("Panther_Youtube_Downloader.py", targetName='Panther_Youtube_Downloader.exe',
			    icon='panther.ico',
			    copyright='Copyright (C) Rajender Kumar 2019', base=base)])
```

#### Creating the Package:

Open the console to your setup.py's directory and run the following command: 

```
python setup.py build
```

This will run the script to create your packaged program. It will create a new directory in the same directory as setup.py called 'build'. Inside of 'build', you'll find another folder with a name that starts with 'exe.' and ends with an identifier for the platform that distutils uses. Inside of that folder, you will find the contents of your package -- the .dlls, the folders, and your beloved .exe.

------

## Features

- Fast and convenient to download video with just a youtube link.
- Wide range of online video portals supported.
- Completely FREE, No purchase required.
- No registration required.
- High-speed conversions.
- Unlimited free conversions and downloads.
- Support high quality video and audio.
- Variety of Audio and Video format are supported.



| ![100free](https://user-images.githubusercontent.com/35782113/63811209-d86b5900-c8f4-11e9-9405-52171d1f6976.jpg) | ![100secure](https://user-images.githubusercontent.com/35782113/63811210-d903ef80-c8f4-11e9-954e-59cfaef04a4c.jpg) | ![1000websites](https://user-images.githubusercontent.com/35782113/63811211-d903ef80-c8f4-11e9-9570-3b76966c0046.jpg) | ![no_limitation](https://user-images.githubusercontent.com/35782113/63811212-d903ef80-c8f4-11e9-9518-8b3fe3ef5ecf.jpg) |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|                    **100% Free Download**                    |                       **100% Secure**                        |                  **Support 1000+ Websites**                  |                      **No limitations**                      |
| Panther Youtube Downloader is absolutely free, and No Ads, No in-app purchase. | 100% safe to download any videos without virus. Enjoy Panther Downloader freely. | Support most of video websites: Youtube, Facebook, Instagram, Vimeo, Dailymotion, etc. | Feel free to download, as many as you want. No Limitation on the number of downloads. |



------



## How it works ? (Instructions)

1. Select the downloader type based on what you want to download i.e. audio or video ("***Audio Download***", "***Video Download***").

2. Select a format of your choice ("***.mp3***", "***.flv***", etc.).

3. Enter the URL or link of the video that you wish to convert/download.

4. Enter the name you wish to give for the video.

5. Click the "***Start Download***" button to begin the conversion/download process.

6. You will get the status of download in the Status bar.

7. Upon successful completion of the conversion/download, your video will be saved in the "downloads" folder under the path of Panther Video Downloader.

8. You can play, stop or delete the audio file directly in the Panther Youtube Downloader by clicking the corresponding button. 

9. To play video files, go to the download folder under the path of Panther Youtube Downloader and play with any supported media player like "VLC Media Player", "Media Player Classic", "5KPlayer", "GOM Media Player", "KMPlayer", "PotPlayer", "5KPlayer", etc.

   

## Usage 

#### Downloading the audio and video from a youtube link:

![Calculator in use](https://user-images.githubusercontent.com/35782113/63805014-786db600-c8e6-11e9-99b1-f4d6a55876f2.gif)



#### Playing the audio directly from the "Panther Youtube Downloader":



![Calculator in use](https://user-images.githubusercontent.com/35782113/63805010-786db600-c8e6-11e9-9aa6-23c9c2851d01.gif)



##### Changing the theme of the "Panther Youtube Downloader":

![Calculator in use ](https://user-images.githubusercontent.com/35782113/63805012-786db600-c8e6-11e9-9e56-8eefbc18b6d3.gif)



## Executable

#### Version: v0.1

You can download the executable for window from here: <a href="#">Panther_Youtube_Downloader_v01.exe</a>

## To-do

- [x] Multi-theme feature implemented
- [x] Option for audio and video download added.
- [ ] Need to work on video player
- [ ] Implementation of more themes for the GUI
- [ ] Need to implement the multi-threading model so that program become more responsive
- [ ] need to work on progress-bar for showing download progress. 

## Documentation 

### Making the layout of the Panther Youtube Downloader

For making the layout of the Panther Youtube Downloader, I used the Tkinter widgets, "Frame" to divide the window area into different sizes. I divide the window into 4 frames:

1. Logo_frame: It is used to show the logo (or header) of the Panther Youtube Downloader
2. Select_frame: In this frame, I used 2 labels and 2 combo box for selection of theme and selection of downloader type.
3. Main_frame: This frame is divided into two sub-frame as given below:
   1. Control_frame: This frame contains all the control widgets. It contains a textbox for entering the youtube (or any other supported wbsites like facebook, instagram, dailymotion etc.) link of the video, a textbox for entering the name you wish to give to the downloaded video, a combo-box for file-type selection, a button to start download process (**START DOWNLOAD**) and a button to clear everything from the textboxes (**RESET**).
   2. List_frame: This frame contains a list-box to list all the downloaded audio/video in sorted order. It also contains three buttons to play the audio (**PLAY**), to stop the audio (**STOP**) and to delete the audio/video file (**DELETE**).
4. Statusbar_frame: This frame is used to show the status of the download process. It first wishes the user, show the download progress when any file is downloaded and show "**FINISH DOWNLOAD**" when the download is complete.

Tkinter provides three options to place the widgets in the window. These are called layout managers or geometry managers in python tkinter:

- pack
- grid
- place

The three layout managers pack, grid, and place should never be mixed in the same master window! Geometry managers serve various functions. They:

- arrange widgets on the screen
- register widgets with the underlying windowing system
- manage the display of widgets on the screen

Arranging widgets on the screen includes determining the size and position of components. Widgets can provide size and alignment information to geometry managers, but the geometry managers has always the final say on the positioning and sizing. 

I used Place geometry manager for placing the buttons in relative positions with frame. Each widget is placed with coordinates of its origin and an exact size. Place is used when the user has the ability to drag and move widgets around. 
The Place geometry manager allows you explicitly set the position and size of a window, either in absolute terms, or relative to another window. The place manager can be accessed through the place method. It can be applied to all standard widgets.

You can see the position of different frames in the window as shown below pictures. 

&nbsp;

![Panther_Youtube_Downloader_Layout1](https://user-images.githubusercontent.com/35782113/63886221-01005b00-c9a8-11e9-90bd-713b118de738.png)

&nbsp;

&nbsp;

### Functions used in the Panther Youtube Downloader

I created the layout of the Panther Youtube Downloader with all the different widgets of tkinter and ttk.  But this is half work done. The main task of performing downloads and showing it to user in an explorer is done by the function and to make this Downloader useful and functional, we need to define functions. The main function used in the program with their purpose are given below:

```python
def go(self):
    """
    Called on the click of "START DOWNLOAD" button. This function check whether video link and file name is provided or not, whether downloader type and file type selected or not. It then called the particular download function based on the the downloader type ("AUDIO DOWNLOAD", "VIDEO DOWNLOAD"). Update status in status-bar accordingly.
    :param: None
    :return: None
    """
```

```python
    def _resize_image(self, event):
            """
            Resize the image according to size of window.
            :param event: event occured when window is resized.
            :return: None
            """
    
```

```python
    def download_audio(self):
        """
        Define the command used to download the audio for a particular video link, then download the audio and move it to download folder under the path of Panther youtube downloader.
        :param: None
        :return: None
        """
```

```python
    def download_video(self):
        """
        Define the command used to download the video for a particular video link, then move it to download folder under the path of Panther youtube downloader.
        :param: None
        :return: None
        """
```

```python
    def populate_explorer(self):
        """
        Populate the listbox (called explorer) with all the audio and video downloaded using Panther youtube downloader in a sorted manner.
        :param: None
        :return: None
        """
        
```

```python
    def clear(self):
        """
        Clear the file_name, youtube_link textbox and update the status bar to wish the user.
        :param: None
        :return: None
        """
```

```python
    def delete(self):
        """
        Delete the selected audio/ video file from the listbox (explorer) and update the status-bar.
        :param: None
        :return: None
        """
```

```python
    def stop(self):
        """
        Stop the playing audio file and update the status-bar.
        :param: None
        :return: None
        """
```

```python
def play(self):
    """
    Play the selected audio file from the explorer and update the status-bar.
    :param: None
    :return: None
    """
```

```python
def set_status_label(self, incoming_message1):
    """
    Set the status-bar according to the argument passed.
    :param incoming_message1: Message to display on the status-bar.
    :return: None
    """
```

```python
   def set_explorer_status_label(self, incoming_message2):
        """
        Set the explorer label equal to the number of files in the list-box.
        :param incoming_message2: Variable to set the value of label
        :return: None
        """
```

```python
    def themeset(self, event):
        """
        Set the different theme as chosen by the user using Combo-box.
        :param event: event to get the selected theme name from the Combo-box.None
        :return: None
        """
```

```python
    def downloaderset(self, event):
        """
        Change the values in the file-type Combo-box based on the selection of downloader type i.e. update the file-type format according to "AUDIO DOWNLOADER" and "VIDEO DOWNLOADER" selection.
        :param event: variable to get the value of the selected downloader type.
        :return: None
        """
```

```python
    def get_filetype(self):
        """
        Get the file-type format (.mp3, .mp4, .flv, .ogg etc.) to download.
        :param: None
        :return: None
        """
```

```python
    def finished(self):
        """
        Update the status bar with "FINISHED DOWNLOAD" when download is complete.
        :param: None
        :return: None
        """
```



## Tests

This program is successfully tested on Window 10, Mac, and Ubuntu 16.04.

------

## Contributing

If interested, you can contribute by following the given step:

1. Fork it using `https://github.com/rajenderk18/Panther_Youtube_Downloader.git`
2. Create your feature branch (git checkout -b my-new-feature) 🔨🔨🔨
3. Commit your changes (git commit -am 'Added <xyz> feature')
4. Push to the branch (git push origin my-new-feature)
5. Create new Pull Request 🔃

------

## FAQ

**How to install the Panther Youtube Downloader?**

- See Installation.

**There is something wrong with my download, what can I do?**

- If something is wrong with your download the first thing you should try is to check that you select the right downloader (Audio or Video) and correct file-type format for the download. Try again by refreshing the youtube and copying the new link. 
  If that does not work contact us here and make sure to exactly describe your problem. 

**Why can't I download certain videos?**

- Certain YouTube videos can't be downloaded because we have either received a complaint from copyright holders or because YouTube has blocked our servers from accessing the video. Please check to make sure the YouTube video you want to download isn't private and is accessible worldwide.

**Where are the downloaded files stored?**

- All the downloaded files (Audio and Video) are stored in the "downloads" folder under the path  where you install Panther Youtube Downloader. 

**How to watch *.FLV, *.OGG, *.WEBM or other video formats?**

- To play video files, go to the download folder under the path of Panther Youtube Downloader and play with any supported media player like "VLC Media Player", "Media Player Classic", "5KPlayer", "GOM Media Player", "KMPlayer", "PotPlayer", "5KPlayer" etc.

**How to convert FLV video in AVI, MPEG and WMV?**

- We think that the most simple freeware video-converter is "Frezz FLV to AVI/MPEG/WMV Converter". It allows you to convert Flash FLV video in AVI/MPEG/WMV and also to change options of quality of video and audio, as well as converting several video reels at once.

**Is this app free?**

- Yes. This app is and always will be free and there's no limit to the number of files you can convert, so feel free to use "Panther Youtube Downloader" as much as you want.
  Donations and all other kinds of support are greatly appreciated though.

**How can I support "Panther Youtube Downloader"?**

- You can help me by donating so that I can improve the Panther Youtube Downloader and make other useful software. cover the server costs. More here
  You can show "Panther Youtube Downloader" your friends and family and make sure everybody knows about it :) .

**How long does it take to convert a video?**

- While we offer one of the fastest conversion rates, the actual duration may vary based on the length of the original video and the time of the day. The speed and stability of your internet connection may also affect the time it takes to complete the conversion process. To give you an idea, a five-minute video usually takes roughly a minute or less to convert.

**What video formats do you support?**

- We support conversions to most of the available video formats out there, which include ".3gp", ".flv", ".mp4", ".ogg", ".webm".

**What audio formats do you support?**

- We support conversions to most of the available audio formats out there, which include ".mp3", ".wav", ".mp4a", ".flac", ".opus", ".vorbis".

**Why did you create a new youtube downloader, when there are already many exiting youtube downloader available?**

- I start this program just for learning purpose. Now, It become a very good youtube downloader program.

**Why did you create a new youtube downloader in *tkinter*?**

- Tkinter provide a great GUI for python based program. I enjoy the process of creating the GUI for this youtube downloader in tkinter.

**Is download youtube video legal?**

- You should only download videos if you have permission from the copyright holder. Unauthorized downloading is against YouTube's terms of service. It is risky to download copyright-protected videos without the author's permission. Panther Youtube Downloader suggest you to respect owner's rights.

**To right holders?**

- Dear right holders, "Panther Youtube Downloader" does not host files on its servers and does not publish any links. If your copyright has been violated please contact the administration of websites, where your files are stored: youtube.com.

**I have a questions that is not answered here!**

- In case you have a question that this F.A.Q. does not cover, please contact us here with your question!

------

## Support

Reach out to me at one of the following places!

- Website at <a href="http://KumarRajender.com" target="_blank">`KumarRajender.com`</a>
- Email me: [rajenderk18@gmail.com](mailto:rajenderk18@gmail.com)

&nbsp;

------

## Donations

- If you think this little youtube downloader is useful to you, then it's a good reason to do a donation.
- Your gratitude and financial help will motivate me to continue improving this and work on many other open-source project.
- I dedicated a lot of free time to this project and do not intend to show any ads because ads kind of suck.
- If you like my little downloader, please consider donating so I can continue working on it.

&nbsp;**How you can donate**
You can donate via:



| Payment Method  |                         Payment Link                         |        If image link not working, click on these link        |
| :-------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|     PayPal      | <a href="https://www.paypal.com/webapps/shoppingcart?flowlogging_id=71de0a21b6cb7&mfid=1568207919162_71de0a21b6cb7#/checkout/openButton" target="_blank"><img src="https://user-images.githubusercontent.com/35782113/63217312-24a6e400-c112-11e9-9eef-cc1a0bf69747.jpg" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a> | https://www.paypal.com/webapps/shoppingcart?flowlogging_id=71de0a21b6cb7&mfid=1568207919162_71de0a21b6cb7#/checkout/openButton |
|     Patreon     | <a href="https://www.patreon.com/bePatron?u=23393229" target="_blank"><img src="https://user-images.githubusercontent.com/35782113/63217315-253f7a80-c112-11e9-8aed-aa70e001c3d9.png"></a> |         https://www.patreon.com/bePatron?u=23393229          |
| Buy Me a Coffee | <a href="https://www.buymeacoffee.com/rajenderk18" target="_blank"><img src="https://user-images.githubusercontent.com/35782113/63219307-f8548d00-c13c-11e9-809d-0c531dc1f0d2.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a> |           https://www.buymeacoffee.com/rajenderk18           |
|     Bitcoin     | <img src="https://user-images.githubusercontent.com/35782113/63689899-360a8300-c7d9-11e9-858a-2a014c73e87b.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" > 1Hfu2yC7LH1nqQTdZxcRcgpYBjn6b5fD5j | <img src="https://user-images.githubusercontent.com/35782113/63795081-34bc8180-c8d1-11e9-8c4d-8a709c33a83f.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" >1Hfu2yC7LH1nqQTdZxcRcgpYBjn6b5fD5j |
|  Bitcoin Cash   | <img src="https://user-images.githubusercontent.com/35782113/63795072-3423eb00-c8d1-11e9-9313-272ef36735d6.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" > qq2nhtkytapezz9px0xh9vegyjutpka5asavxf0s8n | <img src="https://user-images.githubusercontent.com/35782113/63795080-34bc8180-c8d1-11e9-9d66-c8c300b601e7.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" >qq2nhtkytapezz9px0xh9vegyjutpka5asavxf0s8n |
|    Ethereum     | <img src="https://user-images.githubusercontent.com/35782113/63689897-360a8300-c7d9-11e9-9640-d2493b872f9f.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" >0x727C0AC1f216Cc2b83680E4FD37A9A0f14c62Dd5 | <img src="https://user-images.githubusercontent.com/35782113/63795079-34bc8180-c8d1-11e9-9ff2-17fce1c74fc5.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" >0x727C0AC1f216Cc2b83680E4FD37A9A0f14c62Dd5 |
|    LiteCoin     | <img src="https://user-images.githubusercontent.com/35782113/63795074-34bc8180-c8d1-11e9-880d-d76c1955c2a9.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" > MA32LZ7Gr3C7Ccp7R1NhB63QogvCf5yePR | <img src="https://user-images.githubusercontent.com/35782113/63795076-34bc8180-c8d1-11e9-9a1a-700333b800b4.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" >MA32LZ7Gr3C7Ccp7R1NhB63QogvCf5yePR |

&nbsp;

&nbsp;

<p align="center">
  <a href="https://www.paypal.com/webapps/shoppingcart?flowlogging_id=71de0a21b6cb7&mfid=1568207919162_71de0a21b6cb7#/checkout/openButton" target="_blank">
  <img width="300" height="125" src="https://user-images.githubusercontent.com/35782113/63217310-24a6e400-c112-11e9-9fb6-2d7f6ec2f143.jpg">
    </a>
</p>

**Other ways you can help me**

- Do you have a Youtube Channel? a Blog? anything similar? Promote Panther Youtube Downloader!
- Thank you for considering to donate



------

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](https://github.com/rajenderk18/Panther-Calculator/blob/master/LICENSE)**
- Copyright 2019 © <a href="http://KumarRajender.com" target="_blank">Rajender Kumar</a>.
