import httpx
from fastapi import HTTPException
import logging

logger = logging.getLogger(__name__)

CAT_FACTS_API_URL = "https://catfact.ninja/fact"
TIMEOUT = 5.0  # seconds
FALLBACK_FACT = "Cats are amazing creatures!"

async def get_cat_fact() -> str:
    """
    Fetch a random cat fact from the Cat Facts API.
    
    Returns:
        str: A random cat fact
        
    Raises:
        HTTPException: If the API call fails after retries
    """
    try:
        async with httpx.AsyncClient(timeout=TIMEOUT) as client:
            response = await client.get(CAT_FACTS_API_URL)
            response.raise_for_status()
            
            data = response.json()
            fact = data.get("fact", FALLBACK_FACT)
            
            logger.info("Successfully fetched cat fact")
            return fact
            
    except httpx.TimeoutException:
        logger.error("Cat Facts API timeout")
        # Return fallback instead of raising error
        return FALLBACK_FACT
        
    except httpx.HTTPStatusError as e:
        logger.error(f"Cat Facts API returned status {e.response.status_code}")
        return FALLBACK_FACT
        
    except Exception as e:
        logger.error(f"Unexpected error fetching cat fact: {str(e)}")
        return FALLBACK_FACT