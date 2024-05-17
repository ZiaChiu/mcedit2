"""
lightmap
"""
from __future__ import absolute_import, division, print_function, unicode_literals
import logging
import numpy as np

log = logging.getLogger(__name__)


def generate_lightmap(brightness, the_end=False, min_light=0.0, gamma=0.5):
    """
    :type gamma: Brightness setting in the Minecraft Video Options. Usual values are 0.0 to 1.0
    """

    light_brightness_table = np.zeros(16)
    for index in range(16):
        darkness = 1.0 - index / 15.0
        light_brightness_table[index] = (1.0 - darkness) / (darkness * 3.0 + 1.0) * (1.0 - min_light) + min_light

    lightmap_colors = np.zeros((16, 16, 4), dtype=np.uint8)

    torch_flicker_x = 0.0
    log.debug("Generating lightmap. brightness=%s, min_light=%s, the_end=%s, gamma=%s",
              brightness, min_light, the_end, gamma)

    for x, y in np.ndindex(16, 16):
        var4 = brightness * 0.95 + 0.05
        sky_brightness = light_brightness_table[y] * var4
        block_brightness = light_brightness_table[x] * (torch_flicker_x * 0.1 + 1.5)

        sky_red = sky_brightness * (brightness * 0.65 + 0.35)
        sky_green = sky_brightness * (brightness * 0.65 + 0.35)
        block_green = block_brightness * ((block_brightness * 0.6 + 0.4) * 0.6 + 0.4)
        block_blue = block_brightness * (block_brightness ** 2 * 0.6 + 0.4)
        red = sky_red + block_brightness
        green = sky_green + block_green
        blue = sky_brightness + block_blue
        red = red * 0.96 + 0.03
        green = green * 0.96 + 0.03
        blue = blue * 0.96 + 0.03

        if the_end:
            red = 0.22 + block_brightness * 0.75
            green = 0.28 + block_green * 0.75
            blue = 0.25 + block_blue * 0.75

        red = min(max(red, 0.0), 1.0)
        green = min(max(green, 0.0), 1.0)
        blue = min(max(blue, 0.0), 1.0)

        red_g = 1.0 - red
        green_g = 1.0 - green
        blue_g = 1.0 - blue
        red_g = 1.0 - red_g ** 4
        green_g = 1.0 - green_g ** 4
        blue_g = 1.0 - blue_g ** 4
        red = red * (1.0 - gamma) + red_g * gamma
        green = green * (1.0 - gamma) + green_g * gamma
        blue = blue * (1.0 - gamma) + blue_g * gamma
        red = red * 0.96 + 0.03
        green = green * 0.96 + 0.03
        blue = blue * 0.96 + 0.03

        red = min(max(red, 0.0), 1.0)
        green = min(max(green, 0.0), 1.0)
        blue = min(max(blue, 0.0), 1.0)

        alpha_b = 255
        red_b = int(red * 255.0)
        green_b = int(green * 255.0)
        blue_b = int(blue * 255.0)
        slot = lightmap_colors[x, y]
        slot[:] = (red_b, green_b, blue_b, alpha_b)

    return lightmap_colors


def main():
    colors = generate_lightmap(0.2)
    np.set_printoptions(edgeitems=100)
    for bl in range(16):
        sl = colors[bl]
        print(f"BlockLight {bl}, SkyLight 0-15")
        print(sl)


if __name__ == "__main__":
    main()
