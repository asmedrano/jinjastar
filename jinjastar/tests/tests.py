"""
Run tests like so:
    python -m unittest discover
Make sure its from the main module directory!
SEE: http://docs.python.org/library/unittest.html#test-discovery
"""
from unittest import TestCase, main
from jinjastar.core import *
import os

class TestRender(TestCase):

    def setUp(self):
        self.template_path= os.path.join(os.path.dirname(__file__),'templates')

    def test_dir_render(self):
        main(self.template_path)


    def tearDown(self):
        pass

if __name__ == '__main__':
    main()

