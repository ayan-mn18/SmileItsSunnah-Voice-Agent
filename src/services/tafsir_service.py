import asyncio
import aiohttp
import json
from typing import Dict, List, Optional
import logging
from ..config.settings import AgentConfig
from .surah_mapping import SURAH_MAPPING, TOPIC_VERSES

logger = logging.getLogger(__name__)

class TafsirService:
    """Service for accessing Tafsir Ibn Kathir commentary"""
    
    def __init__(self):
        self.base_url = AgentConfig.QURAN_API_BASE_URL
        self.tafsir_edition = AgentConfig.TAFSIR_EDITION
        self.surah_mapping = SURAH_MAPPING

    def _get_surah_number(self, surah: str) -> Optional[int]:
        """Convert surah name or number to surah number"""
        if surah.isdigit():
            return int(surah)
        
        surah_clean = surah.lower().strip().replace(' ', '-')
        return self.surah_mapping.get(surah_clean)

    async def get_tafsir(self, surah: str, ayah: int, language: str = "english") -> Optional[str]:
        """
        Get Tafsir Ibn Kathir for a specific verse
        
        Args:
            surah: The Surah name or number
            ayah: The verse number
            language: Language preference (currently only English supported)
            
        Returns:
            The Tafsir commentary text or None if not found
        """
        try:
            surah_number = self._get_surah_number(surah)
            if not surah_number:
                logger.warning(f"Invalid surah reference: {surah}")
                return None

            url = f"{self.base_url}/ayah/{surah_number}:{ayah}/{self.tafsir_edition}"
            
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()
                        if data.get('code') == 200:
                            return data['data']['text']
                    
                    logger.warning(f"API request failed: {response.status} for {url}")
                    return None
                    
        except Exception as e:
            logger.error(f"Error fetching tafsir for {surah}:{ayah}: {e}")
            return None

    async def search_by_topic(self, topic: str, limit: int = 5) -> List[Dict]:
        """
        Search for verses related to a topic
        
        Args:
            topic: The topic or keyword to search for
            limit: Maximum number of results
            
        Returns:
            List of dictionaries containing surah, ayah, and commentary
        """
        try:
            topic_lower = topic.lower()
            verses_to_fetch = []
            
            # Find relevant verses for the topic
            for key, verses in TOPIC_VERSES.items():
                if key in topic_lower or topic_lower in key:
                    verses_to_fetch.extend(verses[:limit])
                    
            if not verses_to_fetch:
                logger.info(f"No verses found for topic: {topic}")
                return []
                
            # Fetch tafsir for found verses
            results = []
            for surah, ayah in verses_to_fetch[:limit]:
                tafsir = await self.get_tafsir(str(surah), ayah)
                if tafsir:
                    results.append({
                        'surah': surah,
                        'ayah': ayah,
                        'commentary': tafsir
                    })
                    
            return results
                
        except Exception as e:
            logger.error(f"Error searching by topic '{topic}': {e}")
            return []

    def get_surah_name(self, surah_number: int) -> Optional[str]:
        """Get surah name from number"""
        for name, number in self.surah_mapping.items():
            if number == surah_number:
                return name.title().replace('-', ' ')
        return None