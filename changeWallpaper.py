"""
Scripts responsible for wallpaper change
"""
import os
import subprocess
import random
import time


def changeWallpaper(image_path: str) -> None:
    """Change wallpaper to given image"""
    if not os.path.isabs(image_path):
        image_path = os.path.abspath(image_path)
    subprocess.run([
        'gsettings',
        'set',
        'org.gnome.desktop.background',
        'picture-uri-dark',
        f'file://{image_path}'
    ])

def pickRandomWallpaper(dir_path: str) -> str:
    "Pick random file from directory"
    _listdir = os.listdir(dir_path)
    rand_image = random.choice(_listdir)
    rand_image_path = os.path.join(os.path.abspath(dir_path), rand_image)
    # work on abspaths, dir_path by default
    return rand_image_path
    
def changeSeriesOfWallpapers(
        dir_path: str,
        rand: bool = True, 
        times: int = 1, 
        speed: int = 1) -> None:
    """
    Change Series of Wallpapers
    
    If given:
    dir_path - is directory from which image would be taken
    rand - whether images should be taken in random order
    times - how many times wallpaper should be changed
            default = 1: once
            eternity: -1
    speed - seconds per one wallpaper change
            default = 1: once every second
    """
    for i in range(times):
        print(f'{i+1}-wallpaper')
        if rand == True:
            image = pickRandomWallpaper(dir_path)
        # implement rand == False for sequential wallpaper change
        else:
            ...
        changeWallpaper(image)
        time.sleep(speed)
    

if __name__ == '__main__':
    changeWallpaper(pickRandomWallpaper('wallpaperStock'))
    # changeSeriesOfWallpapers('wallpaperStock', times=10)
