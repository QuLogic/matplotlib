from collections.abc import Sequence

from .transforms import BboxBase

def count_bboxes_overlapping_bbox(bbox: BboxBase, bboxes: Sequence[BboxBase]) -> int: ...
def update_path_extents(path, trans, rect, minpos, ignore): ...
