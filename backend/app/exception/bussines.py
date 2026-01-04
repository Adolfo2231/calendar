from fastapi import HTTPException

class EmailExistError(HTTPException):
    def __init__(self, detail: str = "Email already registered"):
        super().__init__(status_code=400, detail=detail)

class UsernameExistError(HTTPException):
    def __init__(self, detail: str = "Username already registered"):
        super().__init__(status_code=400, detail=detail)