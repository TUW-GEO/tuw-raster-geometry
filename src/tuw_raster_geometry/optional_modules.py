class ModuleStub:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        raise NotImplementedError(f"Error trying to invoke {item}, library is {self.name} not installed!")


class ClassStub:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError


try:
    import dask.array as da
    import dask.array.core as da_core

    DaskArray = da.Array
    has_dask = True
except ImportError:
    has_dask = False
    da = ModuleStub("dask.array")
    da_core = ModuleStub("dask.array.core")


    class DaskArray(ClassStub):
        ...

try:
    from rasterio.windows import Window

    has_rasterio = True
except ImportError:
    has_rasterio = False


    class Window(ClassStub):
        ...

try:
    from pytileproj import RasterTile

    has_pytileproj = True
except ImportError:
    has_pytileproj = False


    class RasterTile(ClassStub):
        ...
