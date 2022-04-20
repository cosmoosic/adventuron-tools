#!/usr/bin/python3

import base64
import os
import re
import requests
import sys


png_marker = "png\s+\"(.*)\""
png_token = "\spng\s"


def embed_pngs(code):
    fetch = lambda url: requests.get(url).content
    f = lambda url: base64.b64encode(fetch(url)).decode()
    return re.sub(png_marker, lambda m: ' base64_png "' + f(m.group(1)) + '"', code)


def change_tokens(code):
    return re.sub(png_token, " base64_png ", code)


def get_file_content(file_path):
    return open(file_path).read()


def process_content(content):
    new_content = embed_pngs(content)
    return change_tokens(new_content)


def write_content(content, file_name):
    with open(file_name, "w") as new_file:
        new_file.write(content)


def get_new_name(file_path):
    path, ext = os.path.splitext(file_path)
    return path + "_embedded" + ext


def main(file_path, new_name=None):
    new_name = new_name or get_new_name(file_path)
    content = get_file_content(file_path)
    new_content = process_content(content)
    write_content(new_content, new_name)


def test():
    content = 'dream: png "https://cosmoose.org/adventuron_april_2022/Images/dream.png"'
    return process_content(content)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise Exception("Pass file path as first argument")
    file_path = sys.argv[1]
    new_name = sys.argv[2] if len(sys.argv) > 2 else None
    main(file_path, new_name)
