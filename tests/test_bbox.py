import pytest

from tuw_raster_geometry.projected import BBox


@pytest.mark.parametrize("a, b, expected", [
    (BBox(min_x=2999980.0, min_y=599980.0, max_x=3600020.0, max_y=1200020.0),
     BBox(min_x=2700000.0, min_y=1200000.0, max_x=3000000.0, max_y=1500000.0),
     BBox(min_x=2999980.0, min_y=1200000.0, max_x=3000000.0, max_y=1200020.0)),
])
def test_bbox_intersection(a, b, expected):
    assert a.intersect(b) == expected
