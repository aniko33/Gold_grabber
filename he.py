from hentai import Hentai
def loli(count):
    i=0
    count=int(count)
    while i<count:
        doujin = Hentai(i)
        for tag in doujin.tag:
            if tag == "lolicon":
                doujin.download(progressbar=False)
        i=+i