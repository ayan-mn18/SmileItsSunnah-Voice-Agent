from livekit.agents import Agent
from ..prompts.islamic_instructions import ISLAMIC_AGENT_INSTRUCTIONS
from .function_tools import IslamicFunctionTools

class IslamicAssistant(Agent):
    """Main Islamic AI Assistant - Smile"""
    
    def __init__(self):
        # Initialize function tools
        self.function_tools = IslamicFunctionTools()
        
        # Initialize the agent with Islamic instructions
        super().__init__(
            instructions=ISLAMIC_AGENT_INSTRUCTIONS
        )
        
        # Register function tools
        self._register_function_tools()
    
    def _register_function_tools(self):
        """Register all function tools with the agent"""
        # The function_tool decorator automatically registers the functions
        # when the IslamicFunctionTools class is instantiated
        pass
    
    async def get_tafsir_ibn_kathir(self, surah: str, ayah: int, language: str = "english") -> str:
        """Wrapper for tafsir function tool"""
        return await self.function_tools.get_tafsir_ibn_kathir(surah, ayah, language)
    
    async def search_tafsir_by_topic(self, topic: str, limit: int = 5) -> str:
        """Wrapper for topic search function tool"""
        return await self.function_tools.search_tafsir_by_topic(topic, limit)