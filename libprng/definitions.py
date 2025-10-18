from dataclasses import dataclass
from typing import Tuple


@dataclass(slots=True)
class Seed:
    value: int


__all__: Tuple[str, ...] = ("Seed",)
