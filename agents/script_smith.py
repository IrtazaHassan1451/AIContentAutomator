import random
import logging
import time

# Configure logging
logger = logging.getLogger(__name__)

# Script templates organized by sentiment
SCRIPT_TEMPLATES = {
    "bullish": [
        "Hey finance fans, Warren Black here. Let's talk about {keyword}. {intro_hook} "
        "First point - {point_1} This is crucial because {explanation_1} "
        "Second - {point_2} What most people don't realize is {explanation_2} "
        "Finally - {point_3} Remember this: {key_takeaway} "
        "If you found this helpful, tap like and follow for more financial insights.",
        
        "Warren Black here with a quick breakdown on {keyword}. {intro_hook} "
        "Here's what you need to know: {point_1} Why does this matter? {explanation_1} "
        "The data shows {point_2} Industry experts are saying {explanation_2} "
        "My prediction? {point_3} The bottom line: {key_takeaway} "
        "Drop your thoughts below. Warren Black - helping you build wealth."
    ],
    
    "bearish": [
        "Warren Black with an urgent update. {keyword} is showing concerning signals. {intro_hook} "
        "Red flag number one: {point_1} This matters because {explanation_1} "
        "Second warning sign: {point_2} The implications? {explanation_2} "
        "Final indicator: {point_3} My advice right now: {key_takeaway} "
        "Share this with someone who needs to hear it. Follow for more financial warnings.",
        
        "Financial warning from Warren Black. Let's discuss {keyword}. {intro_hook} "
        "First concern: {point_1} The data doesn't lie - {explanation_1} "
        "Second issue: {point_2} Historical patterns suggest {explanation_2} "
        "Third problem: {point_3} What should you do? {key_takeaway} "
        "Stay informed. Stay prepared. Warren Black - protecting your financial future."
    ],
    
    "neutral": [
        "Finance fact check with Warren Black. Today's topic: {keyword}. {intro_hook} "
        "Let's analyze: {point_1} The context matters here - {explanation_1} "
        "Consider this perspective: {point_2} Looking at both sides: {explanation_2} "
        "Balanced approach: {point_3} Key insight: {key_takeaway} "
        "Want more balanced financial analysis? Follow Warren Black.",
        
        "Warren Black here. Let's break down {keyword} objectively. {intro_hook} "
        "First factor to consider: {point_1} The numbers show {explanation_1} "
        "Alternative viewpoint: {point_2} Weighing the evidence: {explanation_2} "
        "Balanced conclusion: {point_3} Remember this principle: {key_takeaway} "
        "For more no-hype financial insights, follow Warren Black."
    ]
}

# Content elements to fill in the templates
CONTENT_ELEMENTS = {
    "inflation": {
        "intro_hook": "The latest CPI numbers have everyone talking, but here's what they're missing.",
        "point_1": "Core inflation is actually diverging from headline numbers.",
        "explanation_1": "food and energy prices are becoming more volatile.",
        "point_2": "The Fed's approach has fundamentally changed since 2021.",
        "explanation_2": "they're now more concerned with employment than hitting exactly 2%.",
        "point_3": "Historical patterns suggest we're near the turning point.",
        "key_takeaway": "Focus on real yields, not nominal rates, for your investment decisions."
    },
    "dividends": {
        "intro_hook": "With market volatility increasing, dividend aristocrats are looking more attractive than ever.",
        "point_1": "Dividend payers have outperformed growth stocks in 7 of the last 10 recessions.",
        "explanation_1": "they provide income regardless of market conditions.",
        "point_2": "The power of dividend reinvestment compounds significantly over time.",
        "explanation_2": "Einstein called compound interest the eighth wonder of the world for a reason.",
        "point_3": "Tax-advantaged accounts maximize dividend efficiency.",
        "key_takeaway": "A 4% dividend yield can provide nearly 40% of historical stock returns with lower volatility."
    },
    "interest rates": {
        "intro_hook": "The yield curve is telling us something important that mainstream finance news is ignoring.",
        "point_1": "Rate cut cycles historically happen faster than rate hike cycles.",
        "explanation_1": "the Fed tends to be more aggressive when stimulating than when cooling the economy.",
        "point_2": "Employment data is a lagging indicator for monetary policy.",
        "explanation_2": "by the time unemployment rises, the Fed is usually already cutting.",
        "point_3": "Market pricing rarely gets the timing right on the first cut.",
        "key_takeaway": "Position your portfolio now, before the consensus shifts."
    },
    "recession": {
        "intro_hook": "The technical indicators I watch are flashing warning signs we haven't seen since 2007.",
        "point_1": "The Leading Economic Index has fallen for 10 consecutive months.",
        "explanation_1": "this indicator has preceded every recession for the past 60 years.",
        "point_2": "Consumer sentiment and spending patterns are diverging.",
        "explanation_2": "people say one thing in surveys but their credit card data shows something else entirely.",
        "point_3": "Corporate earnings guidance is increasingly cautious for Q3 and Q4.",
        "key_takeaway": "Cash positions and defensive assets deserve your attention right now."
    },
    "NFTs": {
        "intro_hook": "After a 95% collapse, certain segments of the NFT market are showing surprising signs of life.",
        "point_1": "Trading volume for blue-chip collections is up 47% quarter-over-quarter.",
        "explanation_1": "institutional interest is returning to established projects with utility.",
        "point_2": "The integration with real-world assets is creating legitimate use cases.",
        "explanation_2": "we're moving beyond simple jpeg speculation to actual financial applications.",
        "point_3": "Regulatory clarity is finally emerging in key markets.",
        "key_takeaway": "The survivors of this crypto winter will likely lead the next cycle."
    },
    "bitcoin": {
        "intro_hook": "The halving event is approaching, and history suggests a major price catalyst.",
        "point_1": "Supply shock fundamentals are stronger than previous halvings.",
        "explanation_1": "institutional holders are removing more BTC from circulation than ever before.",
        "point_2": "ETF approval has created a new on-ramp for trillions in traditional capital.",
        "explanation_2": "pension funds and endowments can now gain exposure without direct custody concerns.",
        "point_3": "Technical chart patterns are forming a classic cup and handle.",
        "key_takeaway": "Even a small allocation could significantly impact portfolio performance if historical patterns repeat."
    },
    "emergency fund": {
        "intro_hook": "The 3-6 month rule might be outdated in today's economic environment.",
        "point_1": "Income volatility has increased across all career levels.",
        "explanation_1": "even high earners are experiencing more frequent job transitions.",
        "point_2": "High-yield savings accounts have changed the opportunity cost equation.",
        "explanation_2": "you can now earn meaningful returns on emergency cash without sacrificing liquidity.",
        "point_3": "Your emergency fund calculation should include lifestyle flexibility.",
        "key_takeaway": "Personalize your safety net based on income stability, not just generic rules."
    },
    "real estate": {
        "intro_hook": "Housing affordability is at its worst level in 40 years, creating potential market instability.",
        "point_1": "Mortgage payment to income ratios have broken historical records.",
        "explanation_1": "the typical homebuyer is now spending over 30% of their income on housing.",
        "point_2": "Inventory levels are finally increasing in key markets.",
        "explanation_2": "sellers who were waiting for the 'perfect time' are now becoming more realistic.",
        "point_3": "Institutional buyers are quietly reducing their acquisition targets.",
        "key_takeaway": "Regional markets will likely behave very differently - national headlines won't tell the full story."
    }
}

def generate_script(topic):
    """
    Generates a finance script based on the trending topic
    
    Args:
        topic (dict): The trending topic information
    
    Returns:
        dict: The generated script and metadata
    """
    logger.info(f"Generating script for topic: {topic['title']}")
    
    # Simulate processing time
    time.sleep(1)
    
    # Get the appropriate template based on sentiment
    sentiment = topic.get('sentiment', 'neutral')
    template = random.choice(SCRIPT_TEMPLATES[sentiment])
    
    # Get the content elements based on keyword
    keyword = topic.get('keyword', 'finance')
    elements = CONTENT_ELEMENTS.get(keyword, CONTENT_ELEMENTS['inflation'])
    
    # Fill in the template with the content elements
    script_text = template.format(
        keyword=keyword,
        intro_hook=elements['intro_hook'],
        point_1=elements['point_1'],
        explanation_1=elements['explanation_1'],
        point_2=elements['point_2'],
        explanation_2=elements['explanation_2'],
        point_3=elements['point_3'],
        key_takeaway=elements['key_takeaway']
    )
    
    # Create script metadata
    script_data = {
        "text": script_text,
        "word_count": len(script_text.split()),
        "estimated_duration": f"{len(script_text.split()) // 3} seconds",
        "target_audience": "Finance enthusiasts, investors, aged 25-45",
        "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "topic_title": topic['title']
    }
    
    logger.info(f"Script generated: {len(script_text)} characters, {script_data['word_count']} words")
    
    return script_data
