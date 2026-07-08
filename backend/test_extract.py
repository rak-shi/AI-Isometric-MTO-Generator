from pprint import pprint

from app.pipeline.gemini_pipeline import extract_mto
from app.models.mto import MTOResponse

result = extract_mto("outputs/3. Marked isometric (1).png")

validated = MTOResponse.model_validate(result)

pprint(validated.model_dump())