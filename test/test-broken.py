import sys
import logging
import html2jira

if sys.version_info[:2] < (2, 7):
    import unittest2 as unittest
else:
    import unittest


logging.basicConfig(format='%(levelname)s:%(funcName)s:%(message)s',
                    level=logging.DEBUG)


class TestHtmlToJira(unittest.TestCase):

        def test_broken(self):
            parser = html2jira.HTML2Jira(bodywidth=0)
            self.assertEqual(parser.handle("<h1>BlaBla</h1>"), "h1. BlaBla\n")

if __name__ == "__main__":
    unittest.main()
