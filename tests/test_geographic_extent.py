from tuw_raster_geometry.geographic import GeogExtent


def test_empty():
    assert GeogExtent(lat_south=0, lat_north=0, lon_west=0, lon_east=0).is_empty
    assert GeogExtent(lat_south=10, lat_north=10, lon_west=0, lon_east=5).is_empty
    assert GeogExtent(lat_south=10, lat_north=15, lon_west=-5, lon_east=-5).is_empty
    assert GeogExtent(lat_south=10, lat_north=15, lon_west=5, lon_east=5).is_empty
    assert not GeogExtent(lat_south=10, lat_north=15, lon_west=0, lon_east=5).is_empty
    assert not GeogExtent(lat_south=-10, lat_north=15, lon_west=0, lon_east=5).is_empty
    assert not GeogExtent(lat_south=10, lat_north=15, lon_west=-5, lon_east=5).is_empty
    assert not GeogExtent(lat_south=10, lat_north=15, lon_west=5, lon_east=-5).is_empty


def test_global_extent():
    assert GeogExtent.make_global().is_global
    assert not GeogExtent(lat_south=20, lat_north=30, lon_west=20, lon_east=30).is_global


def test_extent_to_west_south_east_north():
    assert (GeogExtent(lat_south=20, lat_north=30, lon_west=20, lon_east=30).to_west_south_east_north() ==
            (20, 20, 30, 30))


def test_extent_has_minus180_plus180_longitude_range():
    assert GeogExtent.make_global().to_west_south_east_north() == (-180, -90, 180, 90)


def test_covers_antimeridian():
    assert GeogExtent(lat_south=20, lat_north=30, lon_west=179, lon_east=-179).covers_antimeridian
    assert not GeogExtent(lat_south=20, lat_north=30, lon_west=-179, lon_east=179).covers_antimeridian


def test_expand():
    expanded = GeogExtent(lat_south=20, lat_north=30, lon_west=20, lon_east=30).expand(0.2)
    assert expanded == GeogExtent(lat_south=19.8, lat_north=30.2, lon_west=19.8, lon_east=30.2)


def test_expand_over_antimeridian():
    expanded = GeogExtent(lat_south=20, lat_north=30, lon_west=179, lon_east=-179).expand(0.2)
    assert expanded == GeogExtent(lat_south=19.8, lat_north=30.2, lon_west=178.8, lon_east=-178.8)


def test_make_from_west_south_east_north():
    assert GeogExtent.make_from_west_south_east_north(1, 2, 3, 4).to_west_south_east_north() == (1, 2, 3, 4)
