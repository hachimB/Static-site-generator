import unittest
from extract_markdown_link import extract_markdown_link

class TestMarkdownLink(unittest.TestCase):

    def test_link1(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_link(text), [('to boot dev', 'https://www.boot.dev'), ('to youtube','https://www.youtube.com/@bootdotdev')])

    def test_link2(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev"
        self.assertEqual(extract_markdown_link(text), [('to boot dev', 'https://www.boot.dev')])

    def test_link3(self):
        text = "This is text with a link [to boot dev]https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev"
        self.assertEqual(extract_markdown_link(text), [])