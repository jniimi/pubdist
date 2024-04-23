# pubdist
Upload, share, and shorten the link to share.

## Overview
This Python script utilizes the Dropbox and Bitly APIs to automate the process of uploading a specified file to Dropbox, retrieving a shareable link, and acquiring a shortened URL for the link through Bitly.

## Features
- File upload to Dropbox
- Generation of Dropbox shareable links
- URL shortening via Bitly

## Prerequisites
You need to obtain API keys from Dropbox and Bitly.
- Dropbox API key
- Bitly API key

## Installation
### 1. Clone the repository
```
git clone https://github.com/jniimi/pubdist.git
```
### 2. Install required packages
All we need is os, sys, random, requests, dropbox
```
pip install dropbox
```

### 3. Run the script with the absolute filepath
At this stage, we need to specify the filepath to upload. In the future, we'll set up GUI to drop the file.
```
python main.py [path_to_file]
```
