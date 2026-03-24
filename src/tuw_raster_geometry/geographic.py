from typing import Tuple

from pydantic import BaseModel


class GeogExtent(BaseModel):
    lat_south: float
    lat_north: float
    lon_west: float
    lon_east: float

    @classmethod
    def make_global(cls):
        return cls(lat_south=-90, lat_north=90, lon_west=-180, lon_east=180)

    @classmethod
    def make_from_west_south_east_north(cls, west, south, east, north) -> "GeogExtent":
        return cls(lat_south=south, lat_north=north, lon_west=west, lon_east=east)

    @property
    def is_empty(self) -> bool:
        return (self.lon_east - self.lon_west) == 0 or (self.lat_north - self.lat_south) == 0

    @property
    def is_global(self) -> bool:
        return self.lat_south == -90 and self.lat_north == 90 and self.lon_west == -180 and self.lon_east == 180

    @property
    def covers_antimeridian(self) -> bool:
        return self.lon_west > self.lon_east

    def to_west_south_east_north(self) -> Tuple[float, float, float, float]:
        return self.lon_west, self.lat_south, self.lon_east, self.lat_north

    def expand(self, amount: float) -> "GeogExtent":
        return GeogExtent(
            lat_south=(self.lat_south - amount + 90) % 180 - 90,
            lat_north=(self.lat_north + amount + 90) % 180 - 90,
            lon_west=(self.lon_west - amount + 180) % 360 - 180,
            lon_east=(self.lon_east + amount + 180) % 360 - 180,
        )
