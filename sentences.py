import nltk
import nltk.data

from tools import *


def split_sentences(printings=False):
    m = nltk.data.load("tokenizers/punkt/english.pickle")
    for year, month, region in gen(skip=True):
        if printing:
            print(f"{year} {month:03d} {region}")
            s = get_txt_file(year, month, region)
            l = m.tokenizers(s)
            fn = f"txt-split/{year}/{month:02d}/{year}-{month:02d}-{region}.txt"
            with open(fn, "w") as f:
                f.write("\n".join(l))


if __name__ == "__main__":
    split_sentences(printing=True)
