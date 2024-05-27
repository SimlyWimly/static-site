import re
from textnode import (TextNode, text_type_text, text_type_bold, text_type_italic, text_type_code, text_type_image, text_type_link)

def text_to_textnodes(text):
    text_node = [TextNode(text, text_type_text)]
    text_node = split_nodes_delimiter(text_node, "**", text_type_bold)
    text_node = split_nodes_delimiter(text_node, "*", text_type_italic)
    text_node = split_nodes_delimiter(text_node, "`", text_type_code)
    text_node = split_nodes_image(text_node)
    text_node = split_nodes_link(text_node)
    return text_node

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    text_nodes_list = []
    for old_node in old_nodes:
        if old_node.text_type!= text_type_text:
            text_nodes_list.append(old_node)
            continue
        old_node_split = old_node.text.split(delimiter)
        if len(old_node_split) % 2 == 0:
            raise ValueError("No matching closing delimiter")
        new_nodes_list = []

        for i, new_node in enumerate(old_node_split):
            if new_node == "":
                continue
            if i % 2 == 0:
                new_nodes_list.append(TextNode(new_node, text_type_text))
            else:
                new_nodes_list.append(TextNode(new_node, text_type))
        text_nodes_list.extend(new_nodes_list)
    return text_nodes_list

def extract_markdown_images(text):
    extracted_text = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return extracted_text

def extract_markdown_links(text):
    extracted_text = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return extracted_text

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        markdown_image_list = extract_markdown_images(old_node.text)
        if len(markdown_image_list) == 0:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        for image in markdown_image_list:
            split_text = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(split_text) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], text_type_text))
            new_nodes.append(TextNode(image[0], text_type_image, image[1]))
            original_text = split_text[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        markdown_link_list = extract_markdown_links(old_node.text)
        if len(markdown_link_list) == 0:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        for link in markdown_link_list:
            split_text = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(split_text) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], text_type_text))
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            original_text = split_text[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes
