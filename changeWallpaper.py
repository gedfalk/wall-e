"""
Scripts responsible for wallpaper change
"""
import os
import subprocess
import random


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
    

if __name__ == '__main__':
    image = pickRandomWallpaper('wallpaperStock')
    changeWallpaper(image)
    
