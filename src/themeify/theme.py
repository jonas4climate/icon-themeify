from pydantic import BaseModel, Field
from typing import List, Tuple


class Theme(BaseModel):
    name: str
    base_rgb: Tuple[int, int, int]
    edge_rgb: Tuple[int, int, int]
    line_thickness: int = 5
    min_elem_size: int = 50
    edge_free_pad: int = 10


class ThemeConfig(BaseModel):
    themes: List[Theme] = Field(default_factory=lambda: [
        Theme(
            name="dark",
            base_rgb=(30, 30, 30),
            edge_rgb=(200, 200, 200),
        ),
        Theme(
            name="light",
            base_rgb=(220, 220, 220),
            edge_rgb=(50, 50, 50),
        ),
        Theme(
            name="blue",
            base_rgb=(80, 104, 183),
            edge_rgb=(241, 241, 241),
        ),
    ])