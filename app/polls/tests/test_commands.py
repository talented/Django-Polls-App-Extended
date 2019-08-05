from django.test import TestCase
from io import StringIO
from django.core.management import call_command


class CommandTests(TestCase):

    def test_import_from_csv(self):
        out = StringIO()
        path = '/pgdata/polls.csv'
        call_command('import_from_csv', path, stdout=out)
        print("testing...")
        self.assertIn('Saving to the database...', out.getvalue())
