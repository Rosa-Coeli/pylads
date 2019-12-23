from PIL import Image
import math
import sys


def unmask_one(white_board, background, width, height, position):
     for w in range(position[0], position[0]+width):
         for h in range(position[1], position[1]+height):
             white_board.putpixel((w, h), background.getpixel((w, h)))


def main():
    WHITE = (255, 255, 255)
    fraction = 4 if len(sys.argv) == 2 else int(sys.argv[2])
    background = Image.open(sys.argv[1]).convert('RGB')
    width, height = background.size
    white_board = Image.new('RGB', (width, height), WHITE)
    tile_width = width//fraction
    tile_height = height//fraction
    white_board.save('partially_unmasked.jpg')
    while True:
        white_board = Image.open('partially_unmasked.jpg')
        coordinates = input('Insert coordinates: ')
        if coordinates == 'exit':
            break 
        elif coordinates == 'show all':
            background.save('partially_unmasked.jpg')
            break
        elif len(coordinates) != 2:
            print('fak juu')
            continue
        else:
            for i in coordinates:
                if i in [chr(j) for j in range(48, 58)]:
                    right_form = True
                else:
                    right_form = False
                    break
        if not right_form:
            print('fak juu')
            continue
        coordinates = int(coordinates[0]), int(coordinates[1])
        if coordinates[0] >= fraction or coordinates[1] >= fraction:
            print('fak juu')
            continue
        position = width * coordinates[0] // fraction, height * coordinates[1] // fraction  # position of the tile to be revealed
        if coordinates[0] == fraction - 1 and coordinates[1] == fraction - 1: 
            unmask_one(white_board, background, tile_width, tile_height, position)
        elif coordinates[0] == fraction - 1: 
            unmask_one(white_board, background, tile_width, tile_height+1, position)
        elif coordinates[1] == fraction - 1: 
            unmask_one(white_board, background, tile_width+1, tile_height, position)
        else:
            unmask_one(white_board, background, tile_width+1, tile_height+1, position)
        white_board.save('partially_unmasked.jpg')


main()
