from markdowntransform import processLink
import unittest

class Test(unittest.TestCase):
    def test_transform(self):
        old = ["[Markdown](http://example.com)"]
        processLink(None, None, old)
        self.assertEqual(old[0], "`Markdown <http://example.com>`_")
        

if __name__ == '__main__':
    unittest.main()
