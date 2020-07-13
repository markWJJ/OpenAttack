from OpenAttack.utils import make_zip_downloader
import os

NAME = "SCPN"

URL = "https://thunlp.oss-cn-qingdao.aliyuncs.com/TAADToolbox/scpn.zip"
DOWNLOAD = make_zip_downloader(URL)


def LOAD(path):
    flist = ["scpn.pt", "parse_generator.pt", "parse_vocab.pkl", "bpe.codes", "vocab.txt", "ptb_tagset.pkl"]
    return {
        it: os.path.join(path, it) for it in flist
    }