from fastapi import APIRouter
from app.api_v1.endpoints import items, player, team


api_router = APIRouter(prefix='/api')
api_router.include_router(items.router, prefix='/items')
api_router.include_router(player.router, prefix='/player')
# api_router.include_router(team.router, prefix='/team')
