# ------------------------------------------------------
# Script to start the Flask development server for the API backend.

# Import the Flask app instance created in server.py
# We assume the 'simulator' directory is in the Python path.
# If running from the root, Python should find it.
# You might need to adjust imports based on your exact execution context or use relative imports.
from simulator.api.server import app
import os

if __name__ == '__main__':
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    # Run the Flask development server
    # debug=True enables auto-reloading on code changes and provides detailed error pages.
    # Use host='0.0.0.0' to make the server accessible on your network (useful for testing from other devices)
    # For production, use a proper WSGI server like Gunicorn or Waitress.
    print(f"Starting Flask server on [http://127.0.0.1](http://127.0.0.1):{port}")
    app.run(host='0.0.0.0', port=port, debug=True)
