from dataclasses import dataclass
from typing import Tuple

import numpy as np
from numpy.typing import NDArray

from tuw_raster_geometry.common_types import ArrayData
from tuw_raster_geometry.optional_modules import Window, da, DaskArray, da_core


@dataclass
class RectPixel:
    x_min: int
    y_min: int
    x_max: int
    y_max: int

    def __eq__(self, other: "RectPixel") -> bool:
        return self.x_min == other.x_min and self.y_min == other.y_min and self.x_max == other.x_max and self.y_max == other.y_max

    @property
    def shape(self) -> Tuple[int, int]:
        return self.x_max - self.x_min, self.y_max - self.y_min

    def intersect(self, other: "RectPixel") -> "RectPixel":
        return RectPixel(max(self.x_min, other.x_min), max(self.y_min, other.y_min),
                         min(self.x_max, other.x_max), min(self.y_max, other.y_max))

    def to_rasterio_window(self) -> Window:
        return Window(self.x_min, self.y_min, self.x_max - self.x_min, self.y_max - self.y_min)

    def slice_array(self, array: ArrayData) -> ArrayData:
        if not is_structured_array(array):
            return array[self.x_min:self.x_max, self.y_min:self.y_max]
        return slice_structured_array(array, self.x_min, self.x_max, self.y_min, self.y_max)

    def transpose(self) -> "RectPixel":
        return RectPixel(self.y_min, self.x_min, self.y_max, self.x_max)


def is_structured_array(array: ArrayData) -> bool:
    return getattr(array, 'dtype') is not None and array.dtype.names is not None


def slice_structured_array(array: ArrayData, x_min, x_max, y_min, y_max) -> ArrayData:
    new_shape = x_max - x_min, y_max - y_min
    new_dt = np.dtype([(n, array.dtype[n].subdtype[0], new_shape) for n in array.dtype.names])

    def _slice_array(a: NDArray) -> NDArray:
        return np.array(tuple(a[n][x_min:x_max, y_min:y_max] for n in new_dt.names), dtype=new_dt)

    if isinstance(array, DaskArray):
        return da.from_delayed(da_core.delayed(_slice_array)(array), shape=tuple(), dtype=new_dt)
    return _slice_array(array)
