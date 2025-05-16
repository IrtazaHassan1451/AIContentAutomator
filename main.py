from app import app

# This file is used as an entry point for gunicorn
# All application logic is now in app.py

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
