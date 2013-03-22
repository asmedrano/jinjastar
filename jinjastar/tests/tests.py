"""
Run tests like so:
    python -m unittest discover
Make sure its from the main module directory!
SEE: http://docs.python.org/library/unittest.html#test-discovery
"""
from unittest import TestCase, main
from jinjastar.core import *
from jinjastar.content import *
import os

class TestRender(TestCase):
    """ Tests the most basic functionalilty of the tool"""

    def setUp(self):
        self.template_path= os.path.join(os.path.dirname(__file__),'templates')

    def test_dir_render(self):
        """ For now im just looking to see that things are in /tmp """
        main(self.template_path)

    def tearDown(self):
        pass

class TestContentRender(TestCase):

    def setUp(self):
        self.template_path=os.path.realpath( os.path.join(os.path.dirname(__file__),'templates'))
        self.content_path= os.path.realpath(os.path.join(os.path.dirname(__file__),'content'))

    def test_collect_items(self):
        items = [{'realpath': self.content_path + '/pages/index.md',
                  'cleaned_path': 'index.md', 'file': 'index.md'},
                  {'realpath': self.content_path + '/pages/subpages/badpage.md',
                      'cleaned_path': 'subpages/badpage.md', 'file': 'badpage.md'},
                 {'realpath': self.content_path + '/pages/subpages/more.md',
                  'cleaned_path': 'subpages/more.md', 'file': 'more.md'}]
        collected = collect_items(self.content_path, 'pages')
        self.assertEqual(collected, items)

    def test_get_meta(self):
        collected = collect_items(self.content_path, 'pages')
        # open the index file
        meta = get_content_item_meta(collected[0]['realpath'])
        self.assertEqual(meta, {'template': 'base.html', 'title': 'Home Page'})

    def test_get_meta_bad(self):
        collected = collect_items(self.content_path, 'pages')
        # open the bad file
        meta = get_content_item_meta(collected[1]['realpath'])
        self.assertEqual(meta,None)

    def test_get_content(self):
        collected = collect_items(self.content_path, 'pages')
        content = get_item_content(collected[0]['realpath'])
        test_content = '\n# Hello World!\nThis is a bunch of text that i have written\nthis is more text writen in markdown\n'
        self.assertEqual(content, test_content)

    def test_generate_content(self):
        generate_items(self.content_path)


if __name__ == '__main__':
    main()

