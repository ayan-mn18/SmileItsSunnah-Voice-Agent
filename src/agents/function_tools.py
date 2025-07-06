from typing import Annotated
from livekit.agents import function_tool
from ..services.tafsir_service import TafsirService
import logging

logger = logging.getLogger(__name__)

class IslamicFunctionTools:
    """Function tools for Islamic knowledge queries"""
    
    def __init__(self):
        self.tafsir_service = TafsirService()

    @function_tool()
    async def get_tafsir_ibn_kathir(
        self,
        surah: Annotated[str, "The name or number of the Surah (chapter)"],
        ayah: Annotated[int, "The verse number within the Surah"],
        language: Annotated[str, "Language for the response (default: 'english')"] = "english"
    ) -> str:
        """
        Retrieves Tafsir Ibn Kathir commentary for a specific Quranic verse.
        
        Args:
            surah: The Surah name (e.g., "Al-Fatiha", "Al-Baqarah") or number (1, 2, etc.)
            ayah: The verse number within the Surah
            language: Language preference for the commentary
            
        Returns:
            The Tafsir Ibn Kathir commentary for the specified verse
        """
        try:
            commentary = await self.tafsir_service.get_tafsir(surah, ayah, language)
            
            if commentary:
                return f"According to Tafsir Ibn Kathir for Surah {surah}, Ayah {ayah}: {commentary}"
            else:
                return f"I couldn't find the Tafsir for Surah {surah}, Ayah {ayah}. Could you please double-check the verse reference?"
                
        except Exception as e:
            logger.error(f"Error in get_tafsir_ibn_kathir: {e}")
            return f"I encountered an issue while retrieving the Tafsir. Please try again with a valid verse reference, insha'Allah."

    @function_tool()
    async def search_tafsir_by_topic(
        self,
        topic: Annotated[str, "The topic or keyword to search for in Tafsir Ibn Kathir"],
        limit: Annotated[int, "Maximum number of results to return (default: 5)"] = 5
    ) -> str:
        """
        Searches Tafsir Ibn Kathir for commentary related to a specific topic or keyword.
        
        Args:
            topic: The topic, keyword, or theme to search for
            limit: Maximum number of results to return
            
        Returns:
            Relevant Tafsir commentary related to the topic
        """
        try:
            results = await self.tafsir_service.search_by_topic(topic, limit)
            
            if results:
                response = f"Alhamdulillah, I found {len(results)} relevant commentary about {topic} in Tafsir Ibn Kathir. "
                for result in results:
                    surah_name = self.tafsir_service.get_surah_name(result['surah']) or f"Surah {result['surah']}"
                    response += f"In {surah_name}, verse {result['ayah']}, Ibn Kathir explains: {result['commentary'][:200]}... "
                return response
            else:
                return f"I couldn't find specific commentary about {topic} in Tafsir Ibn Kathir. Try asking about a related concept or specific verse, insha'Allah."
                
        except Exception as e:
            logger.error(f"Error in search_tafsir_by_topic: {e}")
            return f"I encountered an issue while searching. Please try again with a different topic, insha'Allah."