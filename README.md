# [pubdist] Instant Uploader
the Easiest way to Upload the file, Share it, and Shorten the public link to share

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
```bash
git clone https://github.com/jniimi/pubdist.git
```
### 2. Install required packages
The required packages for the least function are os, sys, random, requests, and dropbox. Dropbox SDK can be installed with pip.
```bash
pip install dropbox
```
If you want to use it with GUI, PyQt6 is also needed.
```bash
pip install pyqt6
```

### 3. Install required packages
At this stage, to securely connect with the service, we need to register tokens as environment variables. We'd like to show the way to register them in macOS:
```bash
export PUBDIST_DROPBOX_TOKEN="abc123"
export PUBDIST_BITLY_TOKEN="abc123"
```
In the future, we'll surely create OAuth login. 

### 4. Run the script with the absolute filepath
At this stage, we need to specify the filepath to upload. In the future, we'll set up GUI to drop the file.
```bash
python main.py [path_to_file]
```

## License
[MIT](https://choosealicense.com/licenses/mit/)