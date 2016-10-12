from django.test import TestCase
import datetime

from core.models import TemperatureLog
class TemperatureLogTestCase(TestCase):
    def setup(self):
        TemperatureLog.objects.create(timestamp=datetime.datetime.now().strftime ("%Y%m%d"),temperature=27)
        TemperatureLog.objects.create(timestamp=datetime.datetime.now().strftime ("%Y%m%d"),temperature=28)


    def test_created_templogs_exist_in_db(self):
        create1 = TemperatureLog.objects.create(timestamp=datetime.datetime.now(),temperature=30)
        create2 = TemperatureLog.objects.create(timestamp=datetime.datetime.now(),temperature=29)
        self.assertEqual(TemperatureLog.objects.get(temperature=30) in TemperatureLog.objects.all(),True)
        
