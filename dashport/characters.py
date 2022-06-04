#! /usr/bin/env python3
import json

with (open('dashport/resources/box_drawing_table.json')) as data:
    box_drawing = json.load(data)
with (open('dashport/resources/block_elements_table.json')) as data:
    block_elements = json.load(data)


class BoxDrawing:
    def data():
        return box_drawing

    def html(character):
        return box_drawing[character][0]

    def unicode(character):
        return box_drawing[character][1]

    def char(character):
        if isinstance(character, str):
            return chr(box_drawing[character][0])
        elif isinstance(character, int):
            if character >= 9472:
                return box_drawing[character][1]
            else:
                return box_drawing[character][0]


class BlockElements:
    def data():
        return block_elements

    def html(character):
        return block_elements[character][0]

    def unicode(character):
        return block_elements[character][1]

    def char(character):
        if isinstance(character, str):
            return chr(block_elements[character][0])
        elif isinstance(character, int):
            if character >= 9472:
                return block_elements[character][1]
            else:
                return block_elements[character][0]
