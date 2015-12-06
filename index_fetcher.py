#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from enum import Enum


class Status(Enum):
    failed = 1
    updating = 2
    success = 3


class IndexFetcher(object):
    def __init__(self, url):
        self.url = url
        self.refreshed_at = None
        self.data = {}
        self.index_names = None
        self.status = Status.failed

    def refresh(self):
        self.status = Status.updating
        r = requests.get(self.url)
        
        if r.ok:
            data = self.html_to_data(r.text)
            self.refreshed_at = datetime.now()
            self.status = Status.success
        else:
            self.status = Status.failed

        return self.refreshed_at

    def get_indices(self, district_name):
        return self.data[district_name]

    def get_index_names(self, rows):
        indice_lv1 = [h.text.split("\n")[0] for h in rows[0]("th")][1:]
        indice_lv2 = [d.text.split("\n>")[0] for d in rows[1]("td")][1:]
        flat_indices = indice_lv1[1:-1]
        composite_indices = [indice_lv1[-1] + " " + x for x in indice_lv2[-3:]]
        self.index_names = flat_indices + composite_indices

    def html_to_data(self, html):
        soup = BeautifulSoup(html, "html.parser")
        table = soup("table")[1]
        rows = table("tr")

        if self.index_names is None:
            self.get_index_names(rows)

        self.data = {}
        data_rows = rows[2:]
        for r in data_rows:
            x = [d.text.strip() for d in r("td")]
            self.data[x[0]] = dict(zip(self.index_names, x[1:]))
