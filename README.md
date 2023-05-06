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

categories: Clothes, Beards, Hair, Eyewear, Cig
list of images per category: 5, 5, 5, 5, 2
```

or if you want to generate NFTs with hat and mask run

```console
python3 layering.py

categories: Clothes, Beards, Hat, Eyewear, Cig
list of images per category: 5, 5, 5, 5, 2
```

or if you want to generate NFTs with all assets

```console
python3 layering.py

categories: Back, Clothes, Beards, Hat, Eyewear, Cig
list of images per category: 5, 5, 5, 5, 2
```

in which `categories` are the category names that you want to put them on top of each other and `list of images per category` are the numbers of all images inside each category.

> Noitce that the ordering of the assets is the matter, for example in above `Eyewear` will be on top of the `Hat` or `Hair`.

> Notice that the name of each category must be the base name of each asset inside the `samples` folder. 

> The base image of the human body is named with `Human.png` inside the `samples` folder.

> Final results will be generated inside the `output` folder.
