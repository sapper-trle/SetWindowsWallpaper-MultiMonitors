# python 3.10.11

### Where Windows 11 stores wallpapers
# BingWallpaperFolder = %LOCALAPPDATA%\Microsoft\BingWallpaperApp\WPImages\
# WindowsWallpaperSpotlightFolder = %LOCALAPPDATA%\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets\
# WindowsLockScreenSpotlightFolder = C:\WINDOWS\SystemApps\MicrosoftWindows.Client.CBS_cw5n1h2txyewy\DesktopSpotlight\Assets\Images\
###

import IDesktopWallpaper as idw
import bing_wallpaper_downloader as bwdl
import os


def main(whichMonitor, override=False, index=None):
    monitor_count = idw.ListCurrentWallpapers()
    if monitor_count == 0:
        return
    monitor_ids = idw.GetMonitorIDs()
    idx = whichMonitor - 1
    if (whichMonitor > monitor_count) or (idx < 0):
        print(f"Your choice of monitor number {whichMonitor} is invalid.")
        plural = " is"
        if monitor_count > 1:
            plural = "s are"
        l = [i+1 for i in range(monitor_count)]
        msg = f"Valid monitor number{plural}: {l}"            
        print(f"{msg}")
        print("Exiting.")
        return
    image_path = bwdl.main(override, index)
    if not image_path:
        print("No new image downloaded. Exiting")
        return
    desktop_wallpaper = idw.IDesktopWallpaper.CoCreateInstance()
    monitor_id = monitor_ids[idx]
    image_path = os.path.abspath(image_path)
    if image_path == desktop_wallpaper.GetWallpaper(monitor_id):
        print(f"Monitor {whichMonitor} wallpaper already set to {image_path}.")
        print("Exiting")
        return
    desktop_wallpaper.SetWallpaper(monitor_id, image_path)
    idw.ListCurrentWallpapers()

if __name__ == "__main__":
    monitor_num = 2     # 1 = first monitor, 2 = second monitor, etc
    override = False    # True -> Bing Wallpaper downloaded even if already downloaded.
                        # Note wallpaper is changed only if an image is downloaded
    index = 0           # which Bing Wallpaper, 0 = today's, 1 = yesterday's, 2 = 2 days ago, etc
    main(monitor_num, override, index) 
