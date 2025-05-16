import logging
import time
import random
import os
from datetime import datetime

# Configure logging
logger = logging.getLogger(__name__)

# List of finance images to choose from
FINANCE_IMAGES = [
    "https://pixabay.com/get/g61f6baad3cfd0b0cebc5cbde541faa7d67f3e4038223ebbdbaf3ed57eda14bfd2615a165c8629fce26de91aeed9e29dd09150d548a9ba309f2e8694c2f7308e0_1280.jpg",
    "https://pixabay.com/get/g35c15c6cede25afb2d05d79c2b784a8c9c810177fcde32f3c5d2dfeadccf587b725527c0c1352af0181e45a18f52ad8f8f83d470ea0aebab1e0748ab92cbb898_1280.jpg",
    "https://pixabay.com/get/gef857e9a3f6f43f82eca34905cfe3baa190e5e1307f2a367a5919ae423bf06f08ac0eb789f50b719dd1b203e512e89984b16a922dc879e4d10b20956eed3e1ac_1280.jpg",
    "https://pixabay.com/get/g80f86e0223ab1bcedb78d6d75c5ad4e6987f2151fa933442ae0ce495bb102e2cd9b439ada8765116cd5880670c1e1ee5a5b45d5aa508c4a162b7f6ce160f3516_1280.jpg",
    "https://pixabay.com/get/g4779a13f083d0d2286b118e38e724bda49b9e1e274f3903beb1c2f1e6200850235313a1c3b60ee9650ce3188b2c33e5de8dd0dbda1d31c37483ac28089a851ea_1280.jpg",
    "https://pixabay.com/get/g7165a4805f5e3ffd69480cd1ae4f0b7e92ce9fd639c1713ae9662e008d7b827df69c46875e20cc960b3b5992654007933cfe58667bdd2ebea5b1cf0376f6360a_1280.jpg"
]

# List of business person images for Warren Black
WARREN_IMAGES = [
    "https://pixabay.com/get/g6fa2dbb393a5af328fe50ed954a303a7736d8a6b5e071c49e53391f44a792a8f02b08b04f93fdc56970e532604ce07ffad17a165091a6a8ebea6fc5249a89b74_1280.jpg",
    "https://pixabay.com/get/gdcc3d6f20318c8522a6cf728d50831df3cd5b4308f6e2a0945e161e6ccdc2c79de4ad89b4b817917495dcb943d71268bb1a379713d33430aff5876da49ec0a30_1280.jpg"
]

def create_video(script_data, voiceover_data):
    """
    Simulates creating a video with the voiceover and visuals
    
    Args:
        script_data (dict): The script information
        voiceover_data (dict): The voiceover information
    
    Returns:
        dict: Information about the simulated video
    """
    logger.info("Generating simulated video")
    
    # Simulate processing time
    time.sleep(2)
    
    # Create a unique filename for the video
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"warren_black_short_{timestamp}.mp4"
    filepath = os.path.join("static", "output", filename)
    
    # Calculate simulated file size
    duration_str = voiceover_data.get("duration", "1:00")
    try:
        minutes, seconds = map(int, duration_str.split(":"))
        duration_seconds = minutes * 60 + seconds
    except:
        duration_seconds = 60
    
    file_size_mb = round(duration_seconds * 0.5, 1)  # Roughly 0.5MB per second of video
    
    # Select random images for the video
    selected_finance_images = random.sample(FINANCE_IMAGES, min(3, len(FINANCE_IMAGES)))
    selected_warren_image = random.choice(WARREN_IMAGES)
    
    # Create video data
    video_data = {
        "filename": filename,
        "filepath": filepath,
        "file_size": f"{file_size_mb} MB",
        "duration": voiceover_data.get("duration", "1:00"),
        "resolution": "1080x1920",  # Vertical format for shorts
        "fps": 30,
        "background_images": selected_finance_images,
        "warren_black_image": selected_warren_image,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "captions": "Auto-generated",
        "status": "Successfully rendered (simulated)"
    }
    
    logger.info(f"Video simulated: {filename}, duration: {video_data['duration']}")
    
    return video_data
