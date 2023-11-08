'''
    Script to convert all the images from
    common formats like jpg, png to
    next gen WebP format.

    Make sure to have the following utility added
    to your system path.

    WebP Libraries:
    https://developers.google.com/speed/webp/docs/precompiled

    Refer:
    https://web.dev/codelab-serve-images-webp

    @author thekman
    @version 1.0
'''

import os  # For OS level commands
import pathlib
import subprocess
import time

def get_images(working_dir=os.curdir, extensions=('.png', '.jpg', '.jpeg')):
    try:
        directory = pathlib.Path(working_dir)
        images = directory.rglob('*')
        return [_ for _ in images if _.suffix.lower() in extensions]

    except:
        pass


def convert_to_webp(file: pathlib.Path, quality: int = 80) -> bool:
    command = f'cwebp -q {quality} "{file.absolute()}" -o "{file.parent}\\{file.stem}.webp"'
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

    except:
        pass

    if pathlib.WindowsPath(f'{file.parent}\\{file.stem}.webp').exists():
        return True

    return False


def if_images_exist():
    if len(get_images()) == 0:
        return 'No images'


if if_images_exist() == 'No images':
    print('There are no images in the current directory.')
    input('\nPress any key to exit ')
    exit()

dir_name = r'C:\Users\jelly\Documents\Programming\Python\batch-conversion-to-webp\demo'  # Path to folder which contains images (recursive)
default_extensions = ('.png', '.jpg', '.jpeg')  # Image Extensions
global_quality = 100  # Image quality

list_of_images = get_images(dir_name, default_extensions)

for image in list_of_images:
    result = convert_to_webp(image, global_quality)
    if result:
        print(f'{image.name} converted successfully.')
    else:
        print(f'{image.name} failed to convert.')
