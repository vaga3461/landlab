#! /usr/bin/env python
"""The Landlab.

:Package name: TheLandlab
:Release date: 2018-09-18
:Authors: Greg Tucker, Nicole Gasparini, Erkan Istanbulluoglu, Daniel Hobley,
    Sai Nudurupati, Jordan Adams, Eric Hutton, Katherine Barnhart, Margaux
    Mouchene, Nathon Lyons
:URL: https://landlab.readthedocs.io/en/release/
:License: MIT
"""

from numpy import set_printoptions

from ._registry import registry
from ._version import get_versions
from .core.errors import MissingKeyError, ParameterValueError
from .core.model_component import Component
from .core.model_parameter_loader import load_params
from .field.scalar_data_fields import FieldError
from .grid import (
    ACTIVE_LINK,
    BAD_INDEX_VALUE,
    CORE_NODE,
    FIXED_GRADIENT_BOUNDARY,
    FIXED_LINK,
    FIXED_VALUE_BOUNDARY,
    INACTIVE_LINK,
    LOOPED_BOUNDARY,
    HexModelGrid,
    ModelGrid,
    NetworkModelGrid,
    RadialModelGrid,
    RasterModelGrid,
    VoronoiDelaunayGrid,
    create_grid,
)
from .plot import imshow_grid, imshow_grid_at_node

try:
    set_printoptions(legacy="1.13")
except TypeError:
    pass
finally:
    del set_printoptions

cite_as = registry.format_citations

__all__ = [
    "registry",
    "MissingKeyError",
    "ParameterValueError",
    "Component",
    "FieldError",
    "load_params",
    "ModelGrid",
    "HexModelGrid",
    "RadialModelGrid",
    "RasterModelGrid",
    "VoronoiDelaunayGrid",
    "NetworkModelGrid",
    "BAD_INDEX_VALUE",
    "CORE_NODE",
    "FIXED_VALUE_BOUNDARY",
    "FIXED_GRADIENT_BOUNDARY",
    "LOOPED_BOUNDARY",
    "ACTIVE_LINK",
    "FIXED_LINK",
    "INACTIVE_LINK",
    "create_grid",
    "imshow_grid",
    "imshow_grid_at_node",
]

__version__ = get_versions()["version"]
del get_versions
