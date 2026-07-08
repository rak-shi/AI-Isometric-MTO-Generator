from pydantic import BaseModel
from typing import List, Optional


class DrawingMeta(BaseModel):
    drawing_no: Optional[str] = ""
    revision: Optional[str] = ""
    line_number: Optional[str] = ""
    nps: Optional[str] = ""
    material_class: Optional[str] = ""
    service: Optional[str] = ""


class MTOItem(BaseModel):
    item_no: int
    category: str
    description: str
    size_nps: str
    schedule_rating: Optional[str] = ""
    material_spec: Optional[str] = ""
    end_type: Optional[str] = ""
    quantity: float
    unit: str
    length_m: Optional[float] = None
    confidence: Optional[float] = None
    remarks: Optional[str] = ""


class Summary(BaseModel):
    total_pipe_length_m: float = 0
    fittings: int = 0
    flanges: int = 0
    valves: int = 0
    gaskets: int = 0
    bolt_sets: int = 0


class MTOResponse(BaseModel):
    drawing_meta: DrawingMeta
    items: List[MTOItem]
    summary: Summary