from pydantic import BaseModel

class PredictionRequest(BaseModel):
    content: str
    model: str
    lang: str



class PredictionResponse(BaseModel):
    worldwide_gross: float