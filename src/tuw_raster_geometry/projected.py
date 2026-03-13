from dataclasses import dataclass


@dataclass
class BBox:
    min_x: float
    min_y: float
    max_x: float
    max_y: float

    def with_border(self, border):
        return BBox(self.min_x - border, self.min_y - border, self.max_x + border, self.max_y + border)

    def to_tuple(self) -> tuple[float, float, float, float]:
        return self.min_x, self.min_y, self.max_x, self.max_y

    def intersect(self, other: "BBox") -> "BBox":
        return BBox(max(self.min_x, other.min_x), max(self.min_y, other.min_y),
                    min(self.max_x, other.max_x), min(self.max_y, other.max_y))