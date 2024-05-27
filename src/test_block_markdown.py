import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, block_type_paragraph ,block_type_heading, block_type_code, block_type_ordered_list, block_type_unordered_list, block_type_quote

class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        block_function = markdown_to_blocks("# This is a heading\n\nThis is a paragraph of text. \n\n              It has some **bold** and *italic* words inside of it.\n\n* This is a list item\n* This is another list item")
        block_list = [
            "# This is a heading",
            "This is a paragraph of text.",
            "It has some **bold** and *italic* words inside of it.",
            "* This is a list item\n* This is another list item"
        ]
        self.assertListEqual(block_function, block_list)

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

if __name__ == "__main__":
    unittest.main()
