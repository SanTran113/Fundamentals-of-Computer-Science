class Pixel:
    '''Represents an RGB pixel'''
    def init(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue

    def str(self) -> str:
        return f'({self.red,self.green,self.blue})'