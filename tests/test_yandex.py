# -*- coding: utf-8 -*-
from pynger.pynger import Pynger


if __name__ == '__main__':
    pynger = Pynger('http://www.haikson.com/sitemap.xml')
    res = pynger.ping('yandex')
    print(res)
