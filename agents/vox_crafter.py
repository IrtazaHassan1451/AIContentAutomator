import logging
import time
import random
import os
from datetime import datetime

# Configure logging
logger = logging.getLogger(__name__)

def create_voiceover(script_data):
    """
    Simulates creating a voiceover from the script
    
    Args:
        script_data (dict): The script information
    
    Returns:
        dict: Information about the simulated voiceover
    """
    logger.info("Generating simulated voiceover")
    
    # Simulate processing time
    time.sleep(1.5)
    
    # Create a unique filename for the voiceover
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"warren_black_voiceover_{timestamp}.mp3"
    filepath = os.path.join("static", "output", filename)
    
    # Calculate simulated file size based on script length
    word_count = script_data.get("word_count", 150)
    file_size_kb = round(word_count * 1.5)  # Roughly 1.5KB per word
    
    # Simulate audio duration (about 3 words per second for natural speech)
    duration_seconds = word_count // 3
    duration_formatted = f"{duration_seconds // 60}:{duration_seconds % 60:02d}"
    
    # Create mock audio metadata
    voice_settings = {
        "voice": "Warren Black (Male)",
        "speed": random.uniform(0.95, 1.05),
        "pitch": 1.0,
        "emphasis": random.choice(["moderate", "strong", "natural"]),
        "clarity": random.uniform(0.9, 1.0)
    }
    
    # Create voiceover data
    voiceover_data = {
        "filename": filename,
        "filepath": filepath,
        "file_size": f"{file_size_kb} KB",
        "duration": duration_formatted,
        "voice_settings": voice_settings,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "script_sample": script_data["text"][:100] + "...",
        "status": "Successfully generated (simulated)"
    }
    
    logger.info(f"Voiceover simulated: {filename}, duration: {duration_formatted}")
    
    return voiceover_data
