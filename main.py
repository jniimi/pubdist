import os, sys, requests, dropbox
from random import random

local_dir = os.environ['HOME']
filename  = 'sample.png'
if len(sys.argv) > 1:
    file_path = sys.argv[1]
    if os.path.isfile(file_path):
        local_dir, filename = os.path.split(file_path)
local_abs = os.path.join(local_dir, filename)

dest = '/'+str(int(random()*1000000000))+'/'+filename
DB_TOKEN = os.getenv('PUBDIST_DROPBOX_TOKEN') if 'PUBDIST_DROPBOX_TOKEN' in os.environ.keys() else ''
BL_TOKEN = os.getenv('PUBDIST_BITLY_TOKEN') if 'PUBDIST_BITLY_TOKEN' in os.environ.keys() else ''
POST_URL = 'https://api-ssl.bitly.com/v4/shorten'

def upload():
    with open(local_abs, 'rb') as f:
        try:
            meta = dbx.files_upload(f.read(), dest, mode=dropbox.files.WriteMode('overwrite'))
            #newfile = '/Apps/public_uploader'+dest+filename
            newfile = meta.path_lower
            print(newfile)
            return newfile
        except dropbox.exceptions.ApiError as err:
            if (err.error.is_path() and
                    err.error.get_path().reason.is_insufficient_space()):
                sys.exit("ERROR: Insufficient space.")
            elif err.user_message_text:
                print(err.user_message_text)
                sys.exit()
            else:
                print(err)
                sys.exit()

def check_metadata(file_path):
    try:
        metadata = dbx.files_get_metadata(file_path)
        return True
    except dropbox.exceptions.ApiError as err:
        print(err)

def get_sharable_link(file_path):
    try:
        pub_link = dbx.sharing_create_shared_link_with_settings(newfile)
        print(pub_link.url)
        return pub_link.url
    except dropbox.exceptions.ApiError as err:
        print(err)

def shorten_url(BL_TOKEN, public_url, desired_url=None):
    headers = {"Authorization": f"Bearer {BL_TOKEN}", "Content-Type": "application/json"}
    body    = {"domain": "bit.ly", "long_url": public_url}
    res = requests.post(POST_URL, headers=headers, json=body).json()
    return res["link"]

if __name__ == '__main__':
    if len(DB_TOKEN)==0:
        raise ValueError('Dropbox token is not set')
    with dropbox.Dropbox(DB_TOKEN) as dbx:
        user = dbx.users_get_current_account()
        #print(user)
        newfile = upload()
        #print('Uploaded file:', newfile)
        check_metadata(newfile)
        public_url = get_sharable_link(newfile)

    if len(BL_TOKEN)==0:
        raise ValueError('bitly Token is not set.')
    else:
        short_link = shorten_url(BL_TOKEN=BL_TOKEN, public_url=public_url)
        print(short_link)
