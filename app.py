import os
import logging
import json
import time
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session, flash

# Import all agents
from agents.trend_seeker import get_trending_topic
from agents.script_smith import generate_script
from agents.vox_crafter import create_voiceover
from agents.clip_maker import create_video
from agents.thumb_wizard import create_thumbnail
from agents.upload_pilot import log_upload

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "warren-black-finance-app-secret")

# Ensure output directory exists
os.makedirs("static/output", exist_ok=True)

def run_content_pipeline():
    """
    Run the full content creation pipeline with all agents
    
    Returns:
        dict: Results from all pipeline stages
    """
    logger.info("Starting content creation pipeline")
    results = {}
    
    # Step 1: Get trending finance topic
    logger.info("Running Trend Seeker agent")
    topic_data = get_trending_topic()
    results["topic"] = topic_data
    
    # Step 2: Generate script based on topic
    logger.info("Running Script Smith agent")
    script_data = generate_script(topic_data)
    results["script"] = script_data
    
    # Step 3: Create voiceover from script
    logger.info("Running Vox Crafter agent")
    voiceover_data = create_voiceover(script_data)
    results["voiceover"] = voiceover_data
    
    # Step 4: Create video with voiceover
    logger.info("Running Clip Maker agent")
    video_data = create_video(script_data, voiceover_data)
    results["video"] = video_data
    
    # Step 5: Create thumbnail for video
    logger.info("Running Thumb Wizard agent")
    thumbnail_data = create_thumbnail(topic_data, script_data)
    results["thumbnail"] = thumbnail_data
    
    # Step 6: Log the upload details
    logger.info("Running Upload Pilot agent")
    upload_data = log_upload(
        topic_data, 
        script_data, 
        video_data, 
        thumbnail_data
    )
    results["upload"] = upload_data
    
    # Save results to data.json
    save_results(results)
    
    logger.info("Content pipeline completed successfully")
    return results

def save_results(results):
    """Save pipeline results to data.json"""
    try:
        # Add timestamp to results
        results["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Save to file
        with open("data.json", "w") as f:
            json.dump(results, f, indent=4)
        
        logger.info("Results saved to data.json")
    except Exception as e:
        logger.error(f"Error saving results: {str(e)}")

@app.route('/', methods=['GET', 'POST'])
def index():
    """Main route handling form submission and displaying the form"""
    if request.method == 'POST':
        # Run the content pipeline when form is submitted
        pipeline_results = run_content_pipeline()
        
        # Store results in session
        session['pipeline_results'] = pipeline_results
        
        # Redirect to results page
        return redirect(url_for('results'))
    
    # Display form page on GET request
    return render_template('index.html')

@app.route('/results')
def results():
    """Display results from the content pipeline"""
    # Get results from session
    pipeline_results = session.get('pipeline_results', None)
    
    # If no results, redirect to index
    if not pipeline_results:
        flash('No content has been generated yet. Please create a finance short first.', 'warning')
        return redirect(url_for('index'))
    
    # Display results
    return render_template('results.html', results=pipeline_results)

@app.route('/new')
def new_content():
    """Clear session and start new content creation"""
    session.pop('pipeline_results', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
