import unittest
from  blocktype import BlockType, block_to_block_type

class TestBlocktype(unittest.TestCase):
    def test_headings(self):
        markdown = """# Welcome
        ## Hello everyone
        ### You are welcome"""
        result = block_to_block_type(markdown)
        self.assertEqual(result, BlockType.HEADING)
    
    def test_Code(self):
        markdown = """```printf("20 * 2 = %d", 40);```"""
        result = block_to_block_type(markdown)
        self.assertEqual(result, BlockType.CODE)
    
    def test_quotes(self):
        markdown = """>Successful people are not gifted; they just work hard, then succeed on purpose.
        >Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, love of what you are doing or learning to do.
        >Success is the sum of small efforts, repeated day in and day out."""
        result = block_to_block_type(markdown)
        self.assertEqual(result, BlockType.QUOTE)
    
    def test_unorderedList(self):
        markdown = """- Successful people are not gifted; they just work hard, then succeed on purpose.
        - Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, love of what you are doing or learning to do.
        - Success is the sum of small efforts, repeated day in and day out."""
        result = block_to_block_type(markdown)
        self.assertEqual(result, BlockType.UNORDERED_LIST)
    
    def test_orderedList(self):
        markdown = """1. Successful people are not gifted; they just work hard, then succeed on purpose.
        2. Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, love of what you are doing or learning to do.
        3. Success is the sum of small efforts, repeated day in and day out."""
        result = block_to_block_type(markdown)
        self.assertEqual(result, BlockType.ORDERED_LIST)

    def test_paragraph(self):
        markdown = """1. Successful people are not gifted; they just work hard, then succeed on purpose.

        > Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, love of what you are doing or learning to do.
        
        - Success is the sum of small efforts, repeated day in and day out."""
        result = block_to_block_type(markdown)
        self.assertEqual(result, BlockType.PARAGRAPH)