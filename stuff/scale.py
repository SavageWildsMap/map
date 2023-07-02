import json

# subtract OLD MAP border width from coordinate
# scale the coordinate
# add the NEW MAP border width to the coordinate

#  Coordinate origin is bottom-left of image, not top left, as it's graph map axes, and Y, X
old_map_border_offset = (108, 159)
new_map_border_offset = (369, 484)

# the new map is bigger than the old map
scale_up_factor = 2.33


def offset_and_scale(v:int, old_offset:int, new_offset:int, scale_factor:float):
    # remove border offset, scale, and add new border offset
    return int(((v - old_offset) * scale_factor) + new_offset)


if __name__ == '__main__':
    with open('old_markers.json', 'r') as f:
        markers:list = json.load(f)

    for marker in markers:
        x = offset_and_scale(marker['pos'][0], old_map_border_offset[0], new_map_border_offset[0], scale_up_factor)
        y = offset_and_scale(marker['pos'][1], old_map_border_offset[1], new_map_border_offset[1], scale_up_factor)
        print(f'Old: {marker["pos"]}  New: {[x, y]}')
        marker['pos'] = [x, y]

    with open('markers.json', 'w') as f:
        json.dump(markers, f)
