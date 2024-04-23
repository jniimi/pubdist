import os, sys, requests, dropbox
from random import randint

local_dir = os.environ['HOME']
filename  = 'sample.png'
if len(sys.argv) > 1:
    file_path = sys.argv[1]
    if os.path.isfile(file_path):
        local_dir, filename = os.path.split(file_path)
local_abs = os.path.join(local_dir, filename)

def upload(dbx, filename):
    dest = f'/{randint(0, 999999999)}/{filename}'
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
            else:
                print(err)

def get_sharable_link(dbx, file_path):
    try:
        pub_link = dbx.sharing_create_shared_link_with_settings(file_path)
        return pub_link.url
    except dropbox.exceptions.ApiError as err:
        print(err)

def shorten_url(public_url, desired_url=None):
    BL_TOKEN = os.environ.get('PUBDIST_BITLY_TOKEN', '')
    if len(BL_TOKEN)==0:
        raise ValueError('Dropbox token is not set')
    POST_URL = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {"Authorization": f"Bearer {BL_TOKEN}", "Content-Type": "application/json"}
    body    = {"domain": "bit.ly", "long_url": public_url}
    res = requests.post(POST_URL, headers=headers, json=body).json()
    return res["link"]

def upload_dropbox():
    DB_TOKEN = os.environ.get('PUBDIST_DROPBOX_TOKEN', '')
    if len(DB_TOKEN)==0:
        raise ValueError('Dropbox token is not set')
    with dropbox.Dropbox(DB_TOKEN) as dbx:
        dbx.users_get_current_account()
        newfile = upload(dbx, filename)
        public_url = get_sharable_link(dbx, newfile)
    return public_url

if __name__ == '__main__':
    public_url = upload_dropbox()
    print(public_url)
    short_link = shorten_url(public_url=public_url)
    print(short_link)
