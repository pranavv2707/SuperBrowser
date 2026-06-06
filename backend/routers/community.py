from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse

from services.community_summarizer import get_community_insights
from utils.cache import cache_key, get_cached, set_cached

router = APIRouter()


@router.get("/community")
async def get_community(q: str = Query(default=None)):
    if not q:
        return JSONResponse(
            status_code=400,
            content={"error": "query param q is required"}
        )
    
    key = cache_key(q, "all", "community")
    cached = get_cached(key)
    if cached is not None:
        return JSONResponse(content=cached, headers={"X-Cache": "HIT"})

    results = await get_community_insights(q)
    set_cached(key, results)
    return JSONResponse(content=results, headers={"X-Cache": "MISS"})
