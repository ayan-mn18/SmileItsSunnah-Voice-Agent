import os
from dotenv import load_dotenv

load_dotenv()

class AgentConfig:
    """Configuration settings for the Islamic Voice Agent"""
    
    # API Keys
    DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    CARTESIA_API_KEY = os.getenv("CARTESIA_API_KEY")
    LIVEKIT_API_KEY = os.getenv("LIVEKIT_API_KEY")
    LIVEKIT_API_SECRET = os.getenv("LIVEKIT_API_SECRET")
    LIVEKIT_URL = os.getenv("LIVEKIT_URL")
    
    # Agent Settings
    AGENT_NAME = "Smile"
    SERVICE_NAME = "SmileItsSunnah Voice Agent"
    
    # Model Configurations
    STT_MODEL = "nova-2"
    STT_LANGUAGE = "multi"
    LLM_MODEL = "gpt-4o-mini"
    TTS_MODEL = "sonic-2"
    TTS_VOICE = "f786b574-daa5-4673-aa0c-cbe3e8534c02"
    
    # Tafsir API Configuration
    QURAN_API_BASE_URL = "https://api.alquran.cloud/v1"
    TAFSIR_EDITION = "en.kathir"
    
    @classmethod
    def validate_config(cls):
        """Validate that all required environment variables are set"""
        required_vars = [
            "DEEPGRAM_API_KEY",
            "OPENAI_API_KEY", 
            "CARTESIA_API_KEY",
            "LIVEKIT_API_KEY",
            "LIVEKIT_API_SECRET",
            "LIVEKIT_URL"
        ]
        
        missing_vars = [var for var in required_vars if not getattr(cls, var)]
        
        if missing_vars:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
        
        return True