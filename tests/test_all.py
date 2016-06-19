# -*- coding: utf-8 -*-
from pynger.pynger import Pynger


if __name__ == '__main__':
    pynger = Pynger('http://www.haikson.com/sitemap.xml')
    results = pynger.ping_all()
    for k in results.keys():
        print('%s: %s' % (k, results[k]))
