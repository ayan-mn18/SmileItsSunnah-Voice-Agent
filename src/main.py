"""
Main entry point for the SmileItsSunnah Voice Agent
"""
import logging
from livekit import agents
from .agents.session_manager import VoiceSessionManager
from .config.settings import AgentConfig

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

async def entrypoint(ctx: agents.JobContext):
    """Main entrypoint for the voice agent"""
    try:
        logger.info(f"Starting {AgentConfig.SERVICE_NAME}")
        
        # Create session manager
        session_manager = VoiceSessionManager()
        
        # Create and start session
        session = await session_manager.create_session(ctx)
        
        logger.info("Agent session started successfully")
        
    except Exception as e:
        logger.error(f"Error in entrypoint: {e}")
        raise

def main():
    """Main function to run the agent"""
    try:
        logger.info(f"Initializing {AgentConfig.SERVICE_NAME}")
        agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
    except Exception as e:
        logger.error(f"Failed to start agent: {e}")
        raise

if __name__ == "__main__":
    main()