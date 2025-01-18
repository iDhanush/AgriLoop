from fastapi import APIRouter

admin_router = APIRouter(
    prefix="/user",
    tags=["admin"],
    responses={404: {"description": "Not found"}},
)
