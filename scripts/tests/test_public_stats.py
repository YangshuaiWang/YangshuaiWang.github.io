import copy
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('fetch', Path(__file__).parents[1] / 'fetch_public_stats.py')
fetch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fetch)

class SummaryTests(unittest.TestCase):
    def setUp(self):
        self.data = {'version':1, 'status':'ok', 'metric':'sessions', 'since':'2026-10-19',
                     'date':'2026-10-19', 'generated_at':'2026-10-19T05:00:00Z',
                     'timezone':'Asia/Singapore', 'sites':{}}
        for key, host in fetch.HOSTS.items():
            self.data['sites'][key] = {'host':host, 'today_sessions':2, 'total_sessions':4,
                'country_count':1, 'top_countries':[{'name':'Singapore','sessions':4}]}

    def test_strips_unapproved_fields(self):
        self.data['private'] = 'secret'
        self.data['sites']['github']['private'] = 'secret'
        result = fetch.validate(self.data)
        self.assertNotIn('private', str(result))
        self.assertEqual(result['sites']['github']['today_sessions'], 2)

    def test_rejects_wrong_site_or_metric(self):
        for field, value in [('host','other.example'), ('today_sessions',-1), ('total_sessions',True), ('country_count',999)]:
            with self.subTest(field=field):
                data = copy.deepcopy(self.data)
                data['sites']['github'][field] = value
                with self.assertRaises(ValueError): fetch.validate(data)

    def test_does_not_turn_failure_into_zeroes(self):
        with self.assertRaises(ValueError): fetch.validate({'status':'unavailable'})

    def test_snapshot_date_matches_property_timezone(self):
        self.data['date'] = '2026-10-20'
        with self.assertRaises(ValueError): fetch.validate(self.data)

if __name__ == '__main__':
    unittest.main()
