from fastapi import APIRouter

admin_router = APIRouter(
    prefix="/auth",
    tags=["admin"],
    responses={404: {"description": "Not found"}},
)
