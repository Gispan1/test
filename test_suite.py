import unittest

import e2e
from modules import api as api_module
import e2e

api = api_module.api()
class perimeterx_test(unittest.TestCase):

    def setUp(self):
        print("Start test: " + self._testMethodName, "header")

    def test_01_valid_api_report_request(self):
        api.get_report(api_type="socket_ip",value="81.82.81.82",start_time=1499264350000,end_time=1499869150000,threshold=60)

    def test_02_report_request_invalid_timestamp(self):
        api.get_report(api_type="socket_ip",value="81.82.81.82",start_time='1481718521000',end_time='1481736521000',threshold=60 ,valid_call=False)

    def test_03_report_request_invalid_threshold(self):
        api.get_report(api_type="socket_ip",value="81.82.81.82",start_time='1481718521000',end_time='1481736521000',threshold=101 ,valid_call=False)

    def test_04_purchase_at_amazon(self):
        e2e.purchase_runner()

    def test_05_content_scraping(self):
        e2e.content_scraping_runner()