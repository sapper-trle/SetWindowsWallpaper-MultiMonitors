
# Set Windows Wallpaper Multi Monitor

## Introduction

I have a dual monitor setup and wished to use the Bing Wallpaper App to change the wallpaper on my PC daily.

However, the Bing Wallpaper App sets both monitors to the new wallpaper whereas I only wished to change the wallpaper on monitor 2.

So I had to keep going into the Personalize setting in Windows 11 and right-click on the background image I wanted for monitor 1 and re-set it.

Doing this disables the daily refresh setting in the Bing Wallpaper App.

So I wrote a python script to download the daily Bing Wallpaper and set it as wallpaper for monitor 2.

## Instructions

Install the required python packages listed in "requirements.txt"

Copy the three files, "set\_desktop\_wallpaper.py", "bing\_wallpaper\_downloader.py" and "IDesktopWallpaper.py" into the same directory.

Run "set\_desktop\_wallpaper.py" to download the daily wallpaper image from Bing and set it as wallpaper on monitor 2.

The downloaded Bing Wallpaper images will be stored in the "BingWallpapers" directory created in the same directory as the three python scripts.

A database file, "download\_history.db", storing the download history will also be created in the same directory.

Images that are recorded in the database will not be downloaded again.

The script will only set the wallpaper on monitor 2 if it downloads a new image.

## Notes

"bing\_wallpaper\_downloader.py" copied from here.
https://github.com/xTayEx/BingWallpaperDownloader

Main modifications:

* hardcoded to always use argument "--use-api"
* default resolution "1920 x 1080"
* default mkt is "en-AU"
* uses negative cleanup-days argument for deleting history

Run "bing\_wallpaper\_downloader.py" standalone to download Bing wallpapers only.

"IDesktopWallpaper.py" code copied from here.
https://stackoverflow.com/questions/66375014/is-it-possible-to-use-idesktopwallpaper-in-python

Run "IDesktopWallpaper.py" standalone to list the current wallpaper images for all monitors.


I was able to run this script on a PC without admin rights using portable version of Thonny Python IDE.
The PC disallowed installing packages into Thonny using "Manage Packages" feature.
So I needed to install all required packages into portable version of Thonny on PC which I had admin rights and then re-zip, copy and extract on target PC.



I also had to install pip-system-certs package into Thonny to fix SSL certificate errors on target PC for "https://bing.biturl.top"

