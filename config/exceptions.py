from fastapi import HTTPException, status

class PublicationNotFoundError(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Publication not found"
        )

class DuplicatePublicationError(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Duplicate publication entry detected"
        )