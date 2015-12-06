#!/usr/bin/env python
# -*- coding: utf-8 -*-
from index_fetcher import IndexFetcher


class App(object):
    def __init__(self, url, location, update_freq):
        self.fetcher = IndexFetcher(url)

    def display(self):
        self.fetcher.refresh()
        indices = self.fetcher.get_indices(my_location)
        print(indices)
        return indices

    def run(self):
        self.display()


if __name__ == "__main__":
    url = "http://cleanair.seoul.go.kr/air_city.htm?method=measure"
    my_location = "강남구"
    update_freq = 3
    App(url, my_location, update_freq).run()
