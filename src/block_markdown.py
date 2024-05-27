from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    markdown_list = markdown.split("\n\n")
    new_list = []
    for block in markdown_list:
        if block == "":
            continue
        else:
            new_list.append(block.strip())
    return new_list

def block_to_block_type(blocks):
    block_list = blocks.split("\n")
    if blocks.startswith("# ") or blocks.startswith("## ") or blocks.startswith("### ") or blocks.startswith("#### ") or blocks.startswith("##### ") or blocks.startswith("###### "):
        return block_type_heading
    if len(block_list) > 1 and block_list[0].startswith("```") and block_list[-1].startswith("```"):
        return block_type_code
    if blocks.startswith(">"):
        for block in block_list:
            if not block.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if blocks.startswith("* "):
        for block in block_list:
            if not block.startswith("* "):
                return block_type_paragraph
        return block_type_unordered_list
    if blocks.startswith("- "):
        for block in block_list:
            if not block.startswith("- "):
                return block_type_paragraph
        return block_type_unordered_list
    if blocks.startswith("1. "):
        ordered_list_number = 1
        for block in block_list:
            if not block.startswith(f"{ordered_list_number}. "):
                return block_type_paragraph
            ordered_list_number += 1
        return block_type_ordered_list
    return block_type_paragraph

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)
