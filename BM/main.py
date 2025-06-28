from util import Nibble as nb
from util import Byte as by

HELP = """

"""

def read(data: bytes):
    header_nibbles = nb.unmerge_pair(data[0])
    palette_size_power, color_mode = nb.unmerge_int3_bool(header_nibbles[0])
    image_width_power, image_alpha = nb.unmerge_int3_bool(header_nibbles[1])

    palette_size = 2 ** (palette_size_power+1)
    image_width = 2 ** (image_width_power+1)

    palette_colors = []
    image_pixels = []

    if color_mode == 0:
        palette_data = data[1:1+int(palette_size*1.5)]
        palette_data = [palette_data[i:i+3] for i in range(0, len(palette_data), 3)] 

        data = data[1+int(palette_size*1.5):]

        for pal_clr in palette_data:
            color_12_1 = nb.unmerge_pair(pal_clr[0])
            color_12_inbetween = nb.unmerge_pair(pal_clr[1])
            color_12_2 = nb.unmerge_pair(pal_clr[2])

            r = color_12_1[0]
            g = color_12_1[1]
            b = color_12_inbetween[0]

            palette_colors.append((nb.spread(r), nb.spread(g), nb.spread(b)))

            r = color_12_inbetween[1]
            g = color_12_2[0]
            b = color_12_2[1]

            palette_colors.append((nb.spread(r), nb.spread(g), nb.spread(b)))
    else:
        color_width = 4 if image_alpha else 3

        palette_data = data[1:1+(palette_size*color_width)]
        palette_data = [palette_data[i:i+color_width] for i in range(0, len(palette_data), color_width)]
        
        data = data[1+(palette_size*color_width):]

        for pal_clr in palette_data:
            color = (pal_clr[0], pal_clr[1], pal_clr[2], pal_clr[3]) if image_alpha else (pal_clr[0], pal_clr[1], pal_clr[2])
            palette_colors.append(color)

    chunk_sizes = [
        1, 2, 4, 4, 8, 8, 8, 8
    ]
    chunk_size = chunk_sizes[palette_size_power]

    for pixels in data:
        image_pixels.extend(by.split(chunk_size, pixels, int(8 / chunk_size)))

    if image_alpha and color_mode == 0:
        trans_color = palette_colors[0]
        palette_colors[0] = (trans_color[0], trans_color[1], trans_color[2], 0)

    return [
        {
            "ps": palette_size,
            "cm": color_mode,
            "iw": image_width,
            "ia": image_alpha
        },
        palette_colors,
        image_pixels
    ]

def head(ps: int, cm: bool, iw: int, ia: bool):
    return nb.merge_pair(nb.merge_int3_bool(ps, cm), nb.merge_int3_bool(iw, ia))