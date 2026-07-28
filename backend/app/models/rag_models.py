from pydantic import BaseModel

class AskRequest(BaseModel):
    question: str

class UploadResponse(BaseModel):
    success: bool
    message: str
    file_hash: str

class AskResponse(BaseModel):
    success: bool
    answer: str