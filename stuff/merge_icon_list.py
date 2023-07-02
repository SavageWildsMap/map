import json

def main():
    layers:list = json.load(open('markerdump.json'))
    icons:dict = json.load(open('icons.json'))

    # make an icon index by filename
    iconidx = {}
    for key, icon in icons.items():
        iconidx[icon['iconUrl']] = key

    for layer in layers:
        for marker in layer['markers']:
            marker['icon_url'] = marker['icon']
            marker['icon'] = iconidx[marker['icon_url']]


    json.dump(layers, open('old_markers.json', 'w'), indent=4)


main()
