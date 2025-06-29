class Pixel:
    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        avg = (self._red + self._green + self._blue) // 3
        self._red = avg
        self._green = avg
        self._blue = avg

    def print_pixel_info(self):
        color_format = f"Color: ({self._red}, {self._green}, {self._blue}) "
        if self._red + self._green + self._blue > 50:
            if self._red == 0 and self._green == 0 and self._blue > 50:
                color_format += "Blue"
            elif self._red == 0 and self._blue == 0 and self._green > 50:
                color_format += "Green"
            elif self._green == 0 and self._blue == 0 and self._red > 50:
                color_format += "Red"
        print(f"X: {self._x}, Y: {self._y}, {color_format}")


def main():
    pixel = Pixel(5, 6, 250, 0, 0)
    pixel.print_pixel_info()
    pixel.set_grayscale()
    pixel.print_pixel_info()


if __name__ == '__main__':
    main()
