# Standard Library
from dataclasses import field
from datetime import date
from enum import Enum
from typing import TYPE_CHECKING

# VerdanTech Source
from src.domain.attributes import AttributeCluster, AttributeProfile
from src.domain.common import DomainModel, Value, value_dataclass
from src.domain.cultivars.entities import Cultivar
from src.utils.sanitizers import SpecError

if TYPE_CHECKING:
    # VerdanTech Source
    from src.domain.garden.garden import Garden
    from src.domain.workspace.workspace import Workspace


type EnvironmentAttributeProfileParentType = Garden | Workspace


class EnvironmentAttributeProfilesEnum(Enum):
    FROST_DATES = "frost_date_profile"
    GEO_COORDINATES = "geo_coordinate_profile"


class EnvironmentAttributeProfile(
    AttributeProfile[EnvironmentAttributeProfileParentType]
):
    """Base class for attribute profiles which pertain to environmental characteristics."""

    id: EnvironmentAttributeProfilesEnum


@value_dataclass
class FrostDateProfile(EnvironmentAttributeProfile):
    """
    Defines the dates of the first and last frost.

    Attributes:
        last_frost_date (date): the date of the last frost.
        first_frost_date (date): the date of the first frost.
    """

    id = EnvironmentAttributeProfilesEnum.FROST_DATES

    last_frost_date: date
    first_frost_date: date

    def sanitize(self) -> None:
        if self.last_frost_date > self.first_frost_date:
            raise SpecError(
                message={
                    "MultiFieldError": "The last frost date cannot be later than the first frost date."
                }
            )


@value_dataclass
class GeoCoordinateProfile(EnvironmentAttributeProfile):
    """
    Defines the geospatial location of the environment.

    Attributes:
        long (float): the longitude of the environment.
        lat (float): the latitude of the environment.
    """

    id = EnvironmentAttributeProfilesEnum.GEO_COORDINATES

    long: float
    lat: float


@value_dataclass
class EnvironmentAttributeCluster(AttributeCluster[EnvironmentAttributeProfile]):
    """Acts as a container for a set of EnvironmentAttributeProfile."""

    frost_date_profile: FrostDateProfile | None = None
    geo_coordinate_profile: GeoCoordinateProfile | None = None
