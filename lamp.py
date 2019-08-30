# https://www.codewars.com/kata/the-lamp-revisited/train/python


class Lamp:
    def __init__(self, color):
        self.color = color
        self.on = False

    def toggle_switch(self):
        self.on = not self.on

    def state(self):
        return f"The lamp is {('off', 'on')[self.on]}."

lamp = Lamp("Blue")

print(lamp.state())
