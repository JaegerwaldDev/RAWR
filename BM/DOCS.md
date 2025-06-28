# Basic info

This format is very clearly intended for pixel art, as anything more high res would just be a waste of where the format shines. If youre planning to store something like photos, you should probably recosider using this.

## Limitations

| | Minimum | Maximum |
|-| ------- | ------- |
| Image Size | 2x1 | 256x256x |
| Palette Size | 2 | 256 |
| Color depth | 12bit | 24bit |



# Header

## Info

The entire header fits in a single byte, as there isn't really that information thats needed to be stored. This also highlights the limitations of this format though, see [Basic info]().

## Format

|PS|PS|PS|CM|IW|IW|IW|IA|
|--|--|--|--|--|--|--|--|

`PS`: Palette size, stored as a power of two<br>
`CM`: Color mode, see [Color mode]()<br>
`IW`: Image width, stored as a power of two, height is gotten automatically from the amount of pixels in the file divided by width<br>
`IA`: Image alpha, see [Transparency]()

## The rest

Now just fill it up with data, after the palette length is reached you just simple write the pixels (referred to by index on the palette.) Here is a map of index lengths:

| Palette size | Index size |
|-|-|
| 2 | 1 |
| 4 | 2 |
| 8 | 4 |
| 16 | 4 |
| 32 | 8 |
| 64 | 8 |
| 128 | 8 |
| 256 | 8 |

> [!WARNING]
> Yes, this seems wasteful, but keep in mind that this is only the raw version of the data, theres a second layer to be applied once everything is done.

# Color mode

The format supports two types of colors, 12 bit colors and 24 bit colors. 24 bit is what you're used to, and 12 bit is the default.

## 12 bit

Each nibble is one of the RGB values. This means the colors need to be in pairs in order to be formatted properly. This is also the reason why the minimum size is 2x1, smallest power of two, smallest amount of possible pixels.

## 24 bit

This is the classic one byte per color, you know the rest.

# Transparency

## 12 bit

This one's easy. First spot in the palette is reserved for a fully transparent color, regardless of what you put there. The spot in the palette has to be filled though, preferrably with something bright and noticible so you know when something goes wrong.

## 24 bit

The 24 bit alpha mode expands the colors to RGBA, and works how you expect, self-explanatory. Technically this means it's 32 bit now.