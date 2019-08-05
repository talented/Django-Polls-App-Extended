from django.test import TestCase
from polls.models import Author


class InetIPLookupTestCase(TestCase):
    """Test that custom lookup field for IsContainedByOrEqual 
    using PostgreSQL inet operators working"""

    def test_net_contained_or_equals(self):
        ip1 = '10.0.1.1/32'
        ip2 = '10.0.0.1/32'
        ip3 = '10.0.0.10/32'

        author1 = Author(name="author1", inet=ip1)
        author2 = Author(name="author2", inet=ip2)
        author3 = Author(name="author3", inet=ip3)
        author1.save()
        author2.save()
        author3.save()

        query = Author.objects.filter(
            inet__net_contains_or_equals='10.0.0.1/32')

        self.assertEqual(query.first().name,  author2.name)
