import random
import logging
import time
from datetime import datetime

# Configure logging
logger = logging.getLogger(__name__)

# List of trending finance topics
TRENDING_TOPICS = [
    {
        "title": "3 Reasons Inflation Might Crash in 2024",
        "keyword": "inflation",
        "sentiment": "bearish",
        "category": "macroeconomics"
    },
    {
        "title": "High-Yield Dividend Stocks Warren Buffett Loves",
        "keyword": "dividends",
        "sentiment": "bullish",
        "category": "investing"
    },
    {
        "title": "Why the Fed Will Cut Rates Before Summer",
        "keyword": "interest rates",
        "sentiment": "neutral",
        "category": "monetary policy"
    },
    {
        "title": "5 Signs We're Heading Into a Recession",
        "keyword": "recession",
        "sentiment": "bearish",
        "category": "economy"
    },
    {
        "title": "NFT Market Making a Comeback?",
        "keyword": "NFTs",
        "sentiment": "bullish",
        "category": "crypto"
    },
    {
        "title": "Is Bitcoin Going to $100K in 2024?",
        "keyword": "bitcoin",
        "sentiment": "bullish",
        "category": "crypto"
    },
    {
        "title": "Emergency Fund: How Much Is Really Enough?",
        "keyword": "emergency fund",
        "sentiment": "neutral",
        "category": "personal finance"
    },
    {
        "title": "Housing Market Crash Coming? 3 Warning Signs",
        "keyword": "real estate",
        "sentiment": "bearish",
        "category": "housing"
    }
]

def get_trending_topic():
    """
    Simulates finding a trending finance topic
    
    Returns:
        dict: Information about the trending topic
    """
    logger.info("Searching for trending finance topics")
    
    # Simulate processing time
    time.sleep(0.5)
    
    # Select a random trending topic
    topic = random.choice(TRENDING_TOPICS)
    
    # Add additional metadata
    topic["created_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    topic["trending_score"] = random.randint(70, 99)
    topic["search_volume"] = f"{random.randint(5, 50)}K monthly searches"
    
    logger.info(f"Found trending topic: {topic['title']}")
    
    return topic
