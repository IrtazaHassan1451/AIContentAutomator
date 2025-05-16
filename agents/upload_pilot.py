import logging
import time
import random
from datetime import datetime, timedelta

# Configure logging
logger = logging.getLogger(__name__)

def log_upload(topic_data, script_data, video_data, thumbnail_data):
    """
    Simulates logging the upload details for the YouTube short
    
    Args:
        topic_data (dict): The topic information
        script_data (dict): The script information
        video_data (dict): The video information
        thumbnail_data (dict): The thumbnail information
    
    Returns:
        dict: Information about the simulated upload
    """
    logger.info("Generating upload log")
    
    # Simulate processing time
    time.sleep(0.75)
    
    # Extract title from topic
    video_title = topic_data.get("title", "Financial Insights with Warren Black")
    
    # Generate random tags
    tags = ["finance", "investing", "money", "warren black"]
    
    # Add keyword from topic as tag
    keyword = topic_data.get("keyword", "")
    if keyword:
        tags.append(keyword)
    
    # Add category from topic as tag
    category = topic_data.get("category", "")
    if category:
        tags.append(category)
    
    # Generate random additional tags
    additional_tags = ["financial advice", "stocks", "money tips", "wealth", 
                      "economic news", "financial freedom", "personal finance",
                      "investment strategy", "market update"]
    tags.extend(random.sample(additional_tags, 3))
    
    # Generate scheduled upload time (random time in next 24 hours)
    current_time = datetime.now()
    hours_ahead = random.randint(1, 24)
    scheduled_time = current_time + timedelta(hours=hours_ahead)
    scheduled_time_str = scheduled_time.strftime("%Y-%m-%d %H:%M:%S")
    
    # Create upload data
    upload_data = {
        "title": video_title,
        "description": f"{script_data.get('text', '')[:100]}... Warren Black brings you daily financial insights to help you build wealth and secure your future. Follow for more!",
        "tags": tags,
        "category": "Finance",
        "visibility": "Public",
        "scheduled_time": scheduled_time_str,
        "estimated_duration": video_data.get("duration", "1:00"),
        "thumbnail": thumbnail_data.get("filename", ""),
        "status": "Scheduled for upload",
        "channel": "Warren Black Finance",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "projected_metrics": {
            "estimated_views_24h": random.randint(500, 5000),
            "estimated_engagement_rate": f"{random.uniform(2.5, 8.5):.1f}%",
            "target_audience": "Finance enthusiasts, 25-45 years old"
        }
    }
    
    logger.info(f"Upload log created for: {video_title}, scheduled for: {scheduled_time_str}")
    
    return upload_data
