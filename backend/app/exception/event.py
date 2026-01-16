from fastapi import HTTPException, status

class EventNotFoundError(HTTPException):
    def __init__(self, detail: str = "Event not found"):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)

class EventPermissionError(HTTPException):
    def __init__(self, detail: str = "You don't have permission to access this event"):
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, detail=detail)