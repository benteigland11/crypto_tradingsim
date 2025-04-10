# -----------------------------
# Main Flask application file for the backend API.

from flask import Flask, request, jsonify
import json

# Create the Flask application instance
app = Flask(__name__)

# --- API Endpoints ---

@app.route('/')
def index():
    """ A simple index route to check if the server is running. """
    return "Crypto Simulator API is running!"

@app.route('/simulate', methods=['POST'])
def handle_simulation_request():
    """
    Handles the simulation request from the frontend GUI.
    Receives configuration data via POST request (expects FormData).
    Initially, just logs the received data and returns a dummy response.
    """
    print("Received /simulate request...")

    if not request.form:
        print("Error: No form data received.")
        return jsonify({"error": "No form data received in the request."}), 400

    try:
        # Access form data sent from the frontend
        # FormData is typically accessed via request.form
        # File data (like the CSV) is accessed via request.files
        config_data = request.form.to_dict()
        print("\nReceived Configuration Data:")
        print(json.dumps(config_data, indent=2)) # Pretty print the received config

        # Access uploaded file (if any)
        if 'data_file' in request.files:
            data_file = request.files['data_file']
            if data_file.filename == '':
                print("Error: No data file selected.")
                return jsonify({"error": "No data file selected."}), 400

            print(f"\nReceived Data File:")
            print(f" - Filename: {data_file.filename}")
            print(f" - Content Type: {data_file.content_type}")
            # TODO: Process the file here (e.g., save it temporarily, read with pandas)
            # For now, just acknowledge receipt.
            # Example: data_df = pd.read_csv(data_file.stream)

        else:
            print("Warning: No data file found in the request.")
            # Depending on requirements, you might return an error here
            # return jsonify({"error": "Data file is required."}), 400


        # --- Placeholder for Actual Simulation Logic ---
        # TODO:
        # 1. Parse and validate config_data more thoroughly.
        # 2. Load data using data_manager (using the uploaded file).
        # 3. Instantiate the selected strategy from strategies module.
        # 4. Run the simulation using the engine module.
        # 5. Calculate results using the analysis module.
        # 6. Format the results to be sent back to the frontend.
        print("\n--- Simulation logic placeholder ---")
        # ---------------------------------------------

        # Simulate a successful result (replace with actual results later)
        dummy_results = {
            "message": "Simulation request received successfully (placeholder).",
            "config_received": config_data,
            "file_received": data_file.filename if 'data_file' in request.files and data_file else None,
            # --- Actual results structure would go here ---
            "totalReturn": "10.5%",
            "annualizedReturn": "18.2%",
            "maxDrawdown": "-8.1%",
            "sharpeRatio": "1.1",
            "profitFactor": "1.6",
            "winRate": "52.0%",
            "numTrades": 38,
            "tradeLog": [
                 {'timestamp': '2023-03-01 12:00', 'action': 'BUY', 'price': 22000, 'quantity': 0.05, 'cost': -1100, 'commission': -1.10},
                 {'timestamp': '2023-03-05 15:00', 'action': 'SELL', 'price': 22500, 'quantity': 0.05, 'cost': 1125, 'commission': -1.13},
            ],
            "equityCurve": {} # Placeholder for chart data
        }
        print("--- Sending dummy success response ---")
        return jsonify(dummy_results), 200

    except Exception as e:
        # Log the exception for debugging on the server side
        print(f"\n!!! Error processing simulation request: {e}")
        import traceback
        traceback.print_exc()
        # Return a generic error response to the client
        return jsonify({"error": f"An internal server error occurred: {e}"}), 500
