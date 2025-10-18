from fastapi import APIRouter, HTTPException
from app.services.cat_facts import get_cat_fact
from app.schemas.profile import ProfileResponse
from app.config import settings
from datetime import datetime, timezone

router = APIRouter()

@router.get("/me", response_model=ProfileResponse)
async def get_profile():
    """
    Get profile information with a random cat fact.
    
    Returns:
        ProfileResponse: Profile data with timestamp and cat fact
    """
    try:
        # Generate current UTC timestamp in ISO 8601 format
        timestamp = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
        
        # Fetch cat fact from external API
        cat_fact = await get_cat_fact()
        
        # Build response
        response = {
            "status": "success",
            "user": {
                "email": settings.USER_EMAIL,
                "name": settings.USER_NAME,
                "stack": settings.USER_STACK
            },
            "timestamp": timestamp,
            "fact": cat_fact
        }
        
        return response
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while processing the request: {str(e)}"
        )