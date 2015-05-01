from __future__ import print_function

import json
from pyquery import PyQuery as pq


class PRS:

    _page = None

    def fetch_page(self, url='http://www.prsindia.org/mptrack/16loksabha/list?query=%'):
        print("Fetching...")
        if self._page is None:
            self._page = pq(url)
        return self._page

    def get_column(self, data_title='Name', child=''):
        page_html = self.fetch_page()
        table_html = page_html('#no-more-tables')
        data_html = table_html("[data-title='{}'] {}".format(data_title, child))
        return [data.text for data in data_html]


prs_client = PRS()
names = prs_client.get_column('Name', 'a')
constituencys = prs_client.get_column('Constituency')

data = zip(names, constituencys)

print(json.dumps(data))
