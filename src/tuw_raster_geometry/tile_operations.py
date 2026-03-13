from tuw_raster_geometry.optional_modules import RasterTile
from tuw_raster_geometry.pixel import RectPixel
from tuw_raster_geometry.projected import BBox


class RasterTilePixelSelector:
    def __init__(self, tile: RasterTile):
        self.tile = tile

    def covered_by(self, area: BBox) -> RectPixel:
        intersected = BBox(*self.tile.outer_boundary_extent).intersect(area)
        top, left = self.tile.xy2rc(intersected.min_x, intersected.min_y)
        bottom, right = self.tile.xy2rc(intersected.max_x, intersected.max_y)
        return RectPixel(x_min=left, y_min=bottom, x_max=right, y_max=top)


def select_pixels_within(tile: RasterTile) -> RasterTilePixelSelector:
    return RasterTilePixelSelector(tile)