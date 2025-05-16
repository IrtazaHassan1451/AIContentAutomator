import logging
import time
import random
import os
from datetime import datetime

# Configure logging
logger = logging.getLogger(__name__)

# List of possible thumbnail styles
THUMBNAIL_STYLES = [
    "Dramatic finance chart with arrow",
    "Warren Black professional headshot with title",
    "Money/wealth visualization with text overlay",
    "Split-image comparison with strong text",
    "Minimalist icon with bold claim"
]

# List of color schemes
COLOR_SCHEMES = [
    {"primary": "#0A2463", "secondary": "#E2E2E2", "accent": "#FB3640"},  # Blue/Red
    {"primary": "#2A9D8F", "secondary": "#E9C46A", "accent": "#E76F51"},  # Teal/Orange
    {"primary": "#003049", "secondary": "#FCBF49", "accent": "#D62828"},  # Navy/Gold
    {"primary": "#1A535C", "secondary": "#4ECDC4", "accent": "#FF6B6B"},  # Teal/Coral
    {"primary": "#5F0F40", "secondary": "#9A031E", "accent": "#FB8B24"}   # Purple/Orange
]

# List of font combinations
FONT_COMBINATIONS = [
    {"title": "Montserrat Bold", "subtitle": "Open Sans"},
    {"title": "Oswald", "subtitle": "Roboto"},
    {"title": "Playfair Display", "subtitle": "Source Sans Pro"},
    {"title": "Raleway Black", "subtitle": "Lato"}
]

def create_thumbnail(topic_data, script_data):
    """
    Simulates creating a thumbnail for the video
    
    Args:
        topic_data (dict): The topic information
        script_data (dict): The script information
    
    Returns:
        dict: Information about the simulated thumbnail
    """
    logger.info("Generating simulated thumbnail")
    
    # Simulate processing time
    time.sleep(1)
    
    # Create a unique filename for the thumbnail
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"warren_black_thumb_{timestamp}.jpg"
    filepath = os.path.join("static", "output", filename)
    
    # Select thumbnail style and design elements
    style = random.choice(THUMBNAIL_STYLES)
    colors = random.choice(COLOR_SCHEMES)
    fonts = random.choice(FONT_COMBINATIONS)
    
    # Extract title from topic
    title = topic_data.get("title", "Financial Insights")
    
    # Create shortened title for thumbnail (max 30 chars)
    if len(title) > 30:
        thumbnail_title = title[:27] + "..."
    else:
        thumbnail_title = title
    
    # Create thumbnail data
    thumbnail_data = {
        "filename": filename,
        "filepath": filepath,
        "title_text": thumbnail_title,
        "style": style,
        "colors": colors,
        "fonts": fonts,
        "dimensions": "1280x720",
        "file_size": f"{random.randint(200, 500)} KB",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "Successfully generated (simulated)"
    }
    
    logger.info(f"Thumbnail simulated: {filename}, style: {style}")
    
    return thumbnail_data
