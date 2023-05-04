

import os
import itertools
from PIL import Image

def load_image_files(directory, extension='png'):
    image_paths = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            image_paths.append(os.path.join(directory, filename))
    return image_paths

def layer_images(base_image_path, overlay_image_path):
    base_image = Image.open(base_image_path).convert('RGBA')
    overlay_image = Image.open(overlay_image_path).resize(base_image.size, Image.ANTIALIAS)
    combined_image = Image.alpha_composite(base_image, overlay_image)
    return combined_image

def save_image(image, filename):
    image.save(filename, 'PNG')

def main():
    background_directory = 'backs'
    rgba_directory = 'output'
    output_directory = 'nftwithback'

    background_images = load_image_files(background_directory)
    rgba_images = load_image_files(rgba_directory)

    for bg_img_path, rgba_img_path in itertools.product(background_images, rgba_images):
        combined_image = layer_images(bg_img_path, rgba_img_path)
        output_filename = f"Combined_{os.path.basename(bg_img_path).split('.')[0]}_{os.path.basename(rgba_img_path).split('.')[0]}.png"
        save_image(combined_image, os.path.join(output_directory, output_filename))

if __name__ == '__main__':
    main()
    