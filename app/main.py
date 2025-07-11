from .cafe import Cafe
from .errors import (
    NotWearingMaskError,
    VaccineError,
)

from typing import List, Dict, Any


def go_to_cafe(friends: List[Dict[str, Any]], cafe: Cafe) -> str:
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
