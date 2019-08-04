from __future__ import unicode_literals
import youtube_dl


def main(url):
    ydl_opts = {}

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(url, download=False)
        return meta
    