from flask import Flask, send_from_directory, render_template_string
import os

app = Flask(__name__)

# Define the directory where your HTML file is located
# It's assumed Main.html is in the same directory as this Flask script
STATIC_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def serve_main_html():
    """
    Serves the Main.html file when the root URL is accessed.
    """
    # Read the content of Main.html
    html_file_path = os.path.join(STATIC_DIR, 'Main.html')
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        return render_template_string(html_content)
    except FileNotFoundError:
        return "Main.html not found!", 404
    except Exception as e:
        return f"An error occurred: {e}", 500

@app.route('/<path:filename>')
def serve_static_files(filename):
    """
    Serves static files (like images, CSS, JS) from the same directory
    as the Flask script.
    """
    return send_from_directory(STATIC_DIR, filename)

if __name__ == '__main__':
    # Run the Flask app in debug mode.
    # Set debug=False for production environments.
    # The 'host="0.0.0.0"' makes the server accessible from other devices
    # on the same network, using your computer's local IP address.
    app.run(debug=True, host='0.0.0.0')
