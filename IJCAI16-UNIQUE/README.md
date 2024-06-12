# MIND-UNIQUE

## Data Website

[IJCAI-16 Brick-and-Mortar Store Recommendation Dataset](https://msnews.github.io/index.html#getting-start)

## START

You should download the data first:

```bash
# You should get your own link on the above website url
# Then you will get 'IJCAI16_data.zip'
wget $YOUR_DOWNLOAD_LINK

# UNZIP
unzip IJCAI16_data.zip -d ./large_train
```

Then Start data cleaning and analysis:

```bash
python clean.py
python calc.py
```