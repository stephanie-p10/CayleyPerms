"""Imports all of the strategies."""

from .requirement_insertions import (
    RequirementInsertionStrategy,
    InsertionEncodingRequirementInsertionFactory,
    CellInsertionFactory,
)
from .point_placements import (
    RequirementPlacementStrategy,
    InsertionEncodingPlacementFactory,
    PointPlacementFactory,
    PartialRequirementPlacementStrategy,
    RowInsertionFactory,
    ColInsertionFactory,
)
from .remove_empty_rows_and_cols import RemoveEmptyRowsAndColumnsStrategy
from .factor import FactorStrategy, ShuffleFactorStrategy
from .row_column_separation import (
    LessThanRowColSeparationStrategy,
    LessThanOrEqualRowColSeparationStrategy,
)

from .fusion import FusionFactory, FusionStrategy

__all__ = (
    "RequirementInsertionStrategy",
    "InsertionEncodingRequirementInsertionFactory",
    "CellInsertionFactory",
    "RequirementPlacementStrategy",
    "InsertionEncodingPlacementFactory",
    "PointPlacementFactory",
    "PartialRequirementPlacementStrategy",
    "RowInsertionFactory",
    "CellInsertionFactory",
    "ColInsertionFactory",
    "RemoveEmptyRowsAndColumnsStrategy",
    "FactorStrategy",
    "ShuffleFactorStrategy",
    "LessThanOrEqualRowColSeparationStrategy",
    "LessThanRowColSeparationStrategy",
    "FusionFactory",
    "FusionStrategy",
)
