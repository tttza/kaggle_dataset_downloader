# Kaggle Dataset Downloader for Google Colaboratory

This is dataset downloader for kaggler who use Google Colaboratory.  
This will download kaggle dataset and extract it to ```../input``` dir with  same directory structure as kaggle notebook do. 

What you have to do is just write dataset name, and you don't have to modify the path in your notebook.

# Quick Usage

```ipynb
dataset_name = "<dataset name or competition dataset name>"

!pip install -q kaggle
!mkdir /root/.kaggle
!cp /content/drive/MyDrive/colab/kaggle.json /root/.kaggle/

!git clone https://github.com/tttza/kaggle_dataset_downloader.git
from kaggle_dataset_downloader import download_dataset
download_dataset.get_dataset(dataset_name)

```


# Prerequirements
Save your kaggle.json to GDrive path, ```/content/drive/MyDrive/colab/kaggle.json```.
Then paste below and run.

```ipynb
!git clone https://github.com/tttza/kaggle_dataset_downloader.git

!pip install -q kaggle
!mkdir /root/.kaggle
!cp /content/drive/MyDrive/colab/kaggle.json /root/.kaggle/

```


# Usage

Each dataset, you have to copy dataset name.

When you click "Copy API command" in the dataset page, you will get above.

```kaggle datasets download -d <username>/<dataset name>```

Or part of dataset url also work.

```https://www.kaggle.com/<username>/<dataset name>```



Then, just copy ```<username>/<dataset name>``` and paste it like above and run.

```ipynb
!git clone https://github.com/tttza/kaggle_dataset_downloader.git
from kaggle_dataset_downloader import download_dataset
download_dataset.get_dataset("<username>/<dataset name>")
```

If the dataset is competition dataset, change last line to below.

```ipynb
download_dataset.get_dataset("<competition name>")
```

# NOTE

I am not sure about the specifics of the kaggle apis, so if you find a case where the downloader does not work properly, please feel free to open an issue.
