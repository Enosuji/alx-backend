from flask import Flask

# Step 1: Create Flask app
app = Flask(__name__)

# Step 5: Define a simple route
@app.route('/')
def index():
    return "Hello, World!"

# Step 6: Run the app
if __name__ == '__main__':
    app.run(debug=True)

