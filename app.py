from flask import Flask
from config import API_KEY

app = Flask(__name__)

@app.route("/")
def home():
    return {"status": "test app", "key_configured": bool(API_KEY)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
# Test issue: Debug mode enabled
app.config["DEBUG"] = True

# Test issue: Hardcoded test password
test_password = "TestPassword123!"

# Test issue: Broad exception handling
try:
    result = 10 / 2
except Exception:
    pass

# Test issue: Unsafe function pattern
result = eval("1 + 1")
