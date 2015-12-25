#!/usr/bin/env python
# -*- coding: utf-8 -*-
from index_fetcher import IndexFetcher, Status
from displayer import Displayer
from threading import Timer


class App(object):
    def __init__(self, url, interval):
        self.fetcher = IndexFetcher(url)
        self.displayer = Displayer()
        self.interval = interval

    def repeat_refreshing(self):
        self.fetcher.refresh()
        self.display()
        Timer(self.interval, self.repeat_refreshing).start()

    def display(self):
        if self.fetcher.status == Status.success:
            self.displayer.set_data(self.fetcher.data)

    def run(self):
        self.repeat_refreshing()


if __name__ == "__main__":
    domain = "http://openapi.seoul.go.kr:8088/"
    service_name = "ListAirQualityByDistrictService"
    district_code = "111261"
    method = "json"
    url = domain + "sample/{}/{}/1/5/{}/"
    full_url = url.format(method, service_name, district_code)

    interval = 3
    App(full_url, interval).run()
