from typing import Any, Dict, List

from pydantic import BaseModel


class CollectionPoint(BaseModel):
    id: str
    embedding: List[float] = []
    metadata: Dict[str, Any] = {}


class CollectionPointResult(BaseModel):
    payload: CollectionPoint
    score: float


def get_highest_score_id(points: List[CollectionPointResult]) -> str:
    highest_point = max(points, key=lambda p: p.score)
    return highest_point.payload.id
