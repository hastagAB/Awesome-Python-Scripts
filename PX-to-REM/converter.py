class Converter:
    base_px = 16

    def __init__(self):
        self.data = []

    def px_to_rem(self, px):
        return float(px) / self.base_px

    def rem_to_px(self, rem):
        return float(rem) * self.base_px
