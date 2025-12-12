# WARNING: This code is intentionally vulnerable to RCE.
# DO NOT run this on any production system or exposed server.
# Use only in isolated, educational environments (e.g., local VM, Docker container).

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute():
    code = request.form.get('code', '')  # User-controlled input
    
    # DANGEROUS: Executing user-supplied code directly
    try:
        result = eval(code)  # Extremely vulnerable to RCE!
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
