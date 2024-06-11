# MIND-UNIQUE

## Data Website

[MIND: MIcrosoft News Dataset](https://msnews.github.io/index.html#getting-start)

[Data Description](https://github.com/msnews/msnews.github.io/blob/master/assets/doc/introduction.md)

## START

You should download the data first:

```bash
wget https://mind201910small.blob.core.windows.net/release/MINDlarge_train.zip

# UNZIP
unzip MINDlarge_train.zip -d ./large_train
```

Then Start data cleaning and analysis:

```bash
python clean.py
python calc.py
```
