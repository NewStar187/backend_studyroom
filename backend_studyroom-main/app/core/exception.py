from fastapi import HTTPException, status

class InvalidTokenError(HTTPException):
    def __init__(self):
        super().__init__(status_code=401, detail="유효하지 않은 토큰입니다")

class DeactivatedAccountError(HTTPException):
    def __init__(self):
        super().__init__(status_code=403, detail="탈퇴한 계정입니다. /auth/reactivate 로 복구하세요")

class ExpiredRecoveryError(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="복구 기간(30일)이 만료되었습니다")

class PermissionDeniedError(HTTPException):
    def __init__(self):
        super().__init__(status_code=403, detail="권한이 없습니다")