import numpy as np
import pytest

from tuw_raster_geometry.optional_modules import Window, has_rasterio, da, has_dask
from tuw_raster_geometry.pixel import RectPixel


@pytest.mark.parametrize("a, b, expected", [
    (RectPixel(0, 0, 100, 100), RectPixel(0, 0, 100, 100), RectPixel(0, 0, 100, 100)),
    (RectPixel(0, 0, 100, 100), RectPixel(50, 50, 100, 100), RectPixel(50, 50, 100, 100)),
    (RectPixel(0, 0, 100, 100), RectPixel(0, 0, 50, 50), RectPixel(0, 0, 50, 50)),
    (RectPixel(0, 0, 100, 100), RectPixel(50, 50, 150, 150), RectPixel(50, 50, 100, 100)),
])
def test_rect_pixel_intersection(a, b, expected):
    assert a.intersect(b) == expected


def test_rect_pixel_transpose():
    assert RectPixel(10, 20, 50, 100).transpose() == RectPixel(20, 10, 100, 50)


def test_rect_shape():
    assert RectPixel(10, 20, 50, 100).shape == (40, 80)


def test_rect_pixel_slice_array():
    assert_arrays_eq(RectPixel(1, 1, 3, 3).slice_array(np.array([[1, 2, 3, 4],
                                                                 [5, 6, 7, 8],
                                                                 [9, 10, 11, 12],
                                                                 [13, 14, 15, 16]])), np.array([[6, 7], [10, 11]]))


def assert_arrays_eq(actual, expected):
    np.testing.assert_equal(actual, expected)


def test_rect_pixel_slice_array_structured_array():
    array = make_structured_array([[1, 2, 3, 4],
                                   [5, 6, 7, 8],
                                   [9, 10, 11, 12],
                                   [13, 14, 15, 16]],
                                  [[-1, -2, -3, -4],
                                   [-5, -6, -7, -8],
                                   [-9, -10, -11, -12],
                                   [-13, -14, -15, -16]])
    assert_arrays_eq(RectPixel(1, 1, 3, 3).slice_array(array),
                     make_structured_array([[6, 7],
                                            [10, 11]],
                                           [[-6, -7],
                                            [-10, -11]]))


def make_structured_array(a, b):
    a = np.array(a, dtype='uint8')
    b = np.array(b, dtype='int8')
    return np.array((a, b), dtype=(np.dtype([('a', 'uint8', a.shape), ('b', 'int8', b.shape)])))


@pytest.mark.skipif(not has_dask, reason="dask is not installed")
def test_rect_pixel_slice_dask_array():
    array = da.from_array(np.array([[1, 2, 3, 4],
                                    [5, 6, 7, 8],
                                    [9, 10, 11, 12],
                                    [13, 14, 15, 16]]))
    assert_arrays_eq(RectPixel(1, 1, 3, 3).slice_array(array).compute(),
                     da.from_array(np.array([[6, 7],
                                             [10, 11]])).compute())


@pytest.mark.skipif(not has_dask, reason="dask is not installed")
def test_rect_pixel_slice_dask_array_structured_array():
    array = da.from_array(make_structured_array([[1, 2, 3, 4],
                                                 [5, 6, 7, 8],
                                                 [9, 10, 11, 12],
                                                 [13, 14, 15, 16]],
                                                [[-1, -2, -3, -4],
                                                 [-5, -6, -7, -8],
                                                 [-9, -10, -11, -12],
                                                 [-13, -14, -15, -16]]))
    assert_arrays_eq(RectPixel(1, 1, 3, 3).slice_array(array).compute(),
                     make_structured_array([[6, 7],
                                            [10, 11]],
                                           [[-6, -7],
                                            [-10, -11]]))


@pytest.mark.skipif(not has_rasterio, reason="rasterio is not installed")
def test_rect_pixel_to_rasterio_window():
    assert RectPixel(10, 20, 50, 100).to_rasterio_window() == Window(10, 20, 40, 80)
