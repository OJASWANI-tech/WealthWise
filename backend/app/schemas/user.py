from pydantic import BaseModel, EmailStr
from datetime import datetime
from enum import Enum


class RiskProfile(str, Enum):
    conservative = "conservative"
    moderate = "moderate"
    aggressive = "aggressive"


class KYCStatus(str, Enum):
    unverified = "unverified"
    verified = "verified"


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    risk_profile: RiskProfile
    kyc_status: KYCStatus
    created_at: datetime

    class Config:
        from_attributes = True
