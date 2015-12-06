#!/usr/bin/env python
# -*- coding: utf-8 -*-
from index_fetcher import IndexFetcher, Status
from threading import Timer


class App(object):
    def __init__(self, url, location, interval):
        self.fetcher = IndexFetcher(url)
        self.interval = interval

    def repeat_refreshing(self):
        self.fetcher.refresh()
        Timer(self.interval, self.repeat_refreshing).start()

    def display(self):
        if self.fetcher.status == Status.success:
            indices = self.fetcher.get_indices(my_location)
            return indices

    def run(self):
        self.repeat_refreshing()


if __name__ == "__main__":
    url = "http://cleanair.seoul.go.kr/air_city.htm?method=measure"
    my_location = "강남구"
    interval = 3
    App(url, my_location, interval).run()
