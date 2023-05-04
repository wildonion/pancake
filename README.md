

# 🥞 NFT layering script 

## ⚗️ Setup 

Install python then 

```console
pip install pillow
```

## 🥙 Usage

To generate the NFTs run:

```
python3 layering.py

categories: Beards, Clothes, Eyewear, Hair, Cig
list of images per category: 5, 5, 5, 5, 2, 5
```

or if you want to generate NFTs with hat and mask run

```console
python3 layering.py

categories: Beards, Clothes, Eyewear, Hat, Cig, Mask
list of images per category: 5, 5, 5, 5, 2, 5
```

in which `categories` are the category names that you want to put them on top of each other and `list of images per category` are the numbers of all images inside each category.

> Notice that the name of each category must be the base name of each asset inside the `samples` folder. 

> The base image of the human body is named with `Human.png` inside the `samples` folder.

> Final results will be generated inside the `output` folder.

To add the backgrounds to each generated NFT run:

```console
python3 add_back.py
```

> Make sure that you have the backgrounds already inside the `backs` foldr.
