


# note that this script assumes that all the images 
# have the same dimensions and transparency (alpha channel) 
# for proper layering.

import os
import itertools
from PIL import Image

def load_image_files(directory, category, images_per_cat):
    image_paths = []
    for i in range(1, int(images_per_cat) + 1):
        filename = f"{category}{i}.png"
        image_paths.append(os.path.join(directory, filename))
    return image_paths

def layer_images(image_paths):
    human = 'samples/Human.jpg'
    # convert Human.jpg it to RGBA like other images 
    base_image = Image.open(human).convert('RGBA')
    base_image_size = base_image.size
    for path in image_paths:
        img = Image.open(path).resize(base_image_size, Image.LANCZOS)
        if img.mode == "RGB":
            img = img.convert('RGBA')
        base_image = Image.alpha_composite(base_image, img)
        # base_img.paste(overlay_img, position, overlay_img) 
    return base_image 

def save_image(image, filename):
    image.save(filename, 'PNG')

def gen(cat, images_per_cat):
    images_directory = 'samples'
    output_directory = 'output'

    categories = cat
    image_combinations = []

    # Load image paths from each category
    for category, count in zip(categories, images_per_cat):
        image_combinations.append(load_image_files(images_directory, category, count))
        
    # Combine all images considering all possibilities
    for combo in itertools.product(*image_combinations):
        # Skip combinations with both hair and hat images
        hair_image = any(img_path.startswith(os.path.join(images_directory, 'Hair')) for img_path in combo)
        hat_image = any(img_path.startswith(os.path.join(images_directory, 'Hat')) for img_path in combo)
        if hair_image and hat_image:
            print("only hair or hat")
            continue
        layered_image = layer_images(combo)
        output_filename = "_".join([os.path.basename(img_path).split('.')[0] for img_path in combo]) + ".png"
        save_image(layered_image, os.path.join(output_directory, output_filename))


if __name__ == '__main__':

    cats = input('categories: ').split(", ") # Beards, Clothes, Eyewear, Hair, Hat, Mask => ['Beards', 'Clothes', 'Eyewear', 'Hair', 'Hat', 'Mask'] 
    image_per_cat = input('list of images per category: ').split(", ") # 5, 5, 5, 5, 2
    
    gen(cats, image_per_cat)
    
    