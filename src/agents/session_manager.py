from livekit import agents
from livekit.agents import AgentSession, RoomInputOptions
from livekit.plugins import (
    openai,
    cartesia,
    deepgram,
    noise_cancellation,
    silero,
)
from livekit.plugins.turn_detector.multilingual import MultilingualModel

from ..config.settings import AgentConfig
from ..prompts.islamic_instructions import GREETING_INSTRUCTIONS
from .islamic_agent import IslamicAssistant
import logging

logger = logging.getLogger(__name__)

class VoiceSessionManager:
    """Manages voice agent sessions and configuration"""
    
    def __init__(self):
        self.config = AgentConfig()
        
    async def create_session(self, ctx: agents.JobContext) -> AgentSession:
        """Create and configure a new agent session"""
        try:
            # Validate configuration
            self.config.validate_config()
            
            # Create session with configured models
            session = AgentSession(
                stt=deepgram.STT(
                    model=self.config.STT_MODEL, 
                    language=self.config.STT_LANGUAGE
                ),
                llm=openai.LLM(model=self.config.LLM_MODEL),
                tts=cartesia.TTS(
                    model=self.config.TTS_MODEL, 
                    voice=self.config.TTS_VOICE
                ),
                vad=silero.VAD.load(),
                turn_detection=MultilingualModel(),
            )

            # Start session with Islamic assistant
            await session.start(
                room=ctx.room,
                agent=IslamicAssistant(),
                room_input_options=RoomInputOptions(
                    noise_cancellation=noise_cancellation.BVC(), 
                ),
            )

            # Connect to room
            await ctx.connect()

            # Generate initial greeting
            await session.generate_reply(instructions=GREETING_INSTRUCTIONS)
            
            logger.info("Voice session created successfully")
            return session
            
        except Exception as e:
            logger.error(f"Error creating voice session: {e}")
            raise