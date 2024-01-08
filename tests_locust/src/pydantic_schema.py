from pydantic import BaseModel, validator

from src.enums.global_enums import GlobalErrorMessages as GEM


class QuetionSchema(BaseModel):
    id: int
    quetion: str
    answer1: str
    answer2: str
    answer3: str
    answer4: str
    answer_true: str
