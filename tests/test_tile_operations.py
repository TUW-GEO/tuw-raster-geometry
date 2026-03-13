import pytest

from tuw_raster_geometry.optional_modules import RasterTile, has_pytileproj
from tuw_raster_geometry.pixel import RectPixel
from tuw_raster_geometry.projected import BBox
from tuw_raster_geometry.tile_operations import select_pixels_within


def make_raster_tile(geotrans):
    if has_pytileproj:
        return RasterTile(crs='EPSG:27704', n_rows=15000, n_cols=15000, geotrans=geotrans)
    return None

@pytest.mark.skipif(not has_pytileproj, reason="pytileproj is not installed")
@pytest.mark.parametrize("tile,expected_selection", [
    (make_raster_tile(geotrans=(2700000, 20, 0, 1500000, 0, -20)),
     RectPixel(x_min=14999, y_min=14999, x_max=15000, y_max=15000)),
    (make_raster_tile(geotrans=(3000000, 20, 0, 1500000, 0, -20)),
     RectPixel(x_min=0, y_min=14999, x_max=15000, y_max=15000)),
    (make_raster_tile(geotrans=(3300000, 20, 0, 1500000, 0, -20)),
     RectPixel(x_min=0, y_min=14999, x_max=15000, y_max=15000)),
    (make_raster_tile(geotrans=(3600000, 20, 0, 1500000, 0, -20)),
     RectPixel(x_min=0, y_min=14999, x_max=1, y_max=15000)),
    (make_raster_tile(geotrans=(2700000, 20, 0, 1200000, 0, -20)),
     RectPixel(x_min=14999, y_min=0, x_max=15000, y_max=15000)),
    (make_raster_tile(geotrans=(3000000, 20, 0, 1200000, 0, -20)),
     RectPixel(x_min=0, y_min=0, x_max=15000, y_max=15000)),
    (make_raster_tile(geotrans=(3300000, 20, 0, 1200000, 0, -20)),
     RectPixel(x_min=0, y_min=0, x_max=15000, y_max=15000)),
    (make_raster_tile(geotrans=(3600000, 20, 0, 1200000, 0, -20)), RectPixel(x_min=0, y_min=0, x_max=1, y_max=15000)),
    (make_raster_tile(geotrans=(2700000, 20, 0, 900000, 0, -20)),
     RectPixel(x_min=14999, y_min=0, x_max=15000, y_max=15000)),
    (make_raster_tile(geotrans=(3000000, 20, 0, 900000, 0, -20)),
     RectPixel(x_min=0, y_min=0, x_max=15000, y_max=15000)),
    (make_raster_tile(geotrans=(3300000, 20, 0, 900000, 0, -20)),
     RectPixel(x_min=0, y_min=0, x_max=15000, y_max=15000)),
    (make_raster_tile(geotrans=(3600000, 20, 0, 900000, 0, -20)), RectPixel(x_min=0, y_min=0, x_max=1, y_max=15000)),
    (make_raster_tile(geotrans=(2700000, 20, 0, 600000, 0, -20)),
     RectPixel(x_min=14999, y_min=0, x_max=15000, y_max=1)),
    (make_raster_tile(geotrans=(3000000, 20, 0, 600000, 0, -20)), RectPixel(x_min=0, y_min=0, x_max=15000, y_max=1)),
    (make_raster_tile(geotrans=(3300000, 20, 0, 600000, 0, -20)), RectPixel(x_min=0, y_min=0, x_max=15000, y_max=1)),
    (make_raster_tile(geotrans=(3600000, 20, 0, 600000, 0, -20)), RectPixel(x_min=0, y_min=0, x_max=1, y_max=1)),
])
def test_select_pixels_of_raster_tile_with_bbox(tile, expected_selection):
    bbox = BBox(min_x=2999980, min_y=599980, max_x=3600020, max_y=1200020)
    selected_pixels = select_pixels_within(tile).covered_by(bbox)
    assert selected_pixels == expected_selection
