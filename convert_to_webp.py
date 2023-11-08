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
import shutil
import subprocess
import time


def get_images(directory=pathlib.Path(os.curdir), extensions=('.png', '.jpg', '.jpeg')):
    try:
        images = directory.rglob('*')
        return [_ for _ in images if _.suffix.lower() in extensions]

    except:
        pass


def convert_to_webp(root_path: pathlib.Path, file: pathlib.Path, quality: int = 80) -> bool:
    command = f'cwebp -q {quality} "{file.absolute()}" -o "{file.parent}\\{file.stem}.webp"'
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

    except:
        pass

    if pathlib.WindowsPath(f'{file.parent}\\{file.stem}.webp').exists():

        relative_path = file.relative_to(root_path)

        if not pathlib.Path(f'{root_path.parent}\\pngs\\{relative_path.parent}').exists():
            os.mkdir(f'{root_path.parent}\\pngs\\{relative_path.parent}')

        print(f'{root_path.parent}\\pngs\\{relative_path.parent}')
        shutil.move(file.absolute(), f'{root_path.parent}\\pngs\\{relative_path}')
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

dir_path = pathlib.Path(dir_name)

list_of_images = get_images(dir_path, default_extensions)

for image in list_of_images:
    result = convert_to_webp(dir_path, image, global_quality)
    if result:
        print(f'{image.name} converted successfully.')
    else:
        print(f'{image.name} failed to convert.')
