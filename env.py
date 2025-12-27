import os

# Read from environment
api_key = os.environ.get('API_KEY')
database = os.environ.get('DATABASE_NAME', 'default.db')

print(f"Using database: {database}")
print(f"Using database: {api_key }")


# example for setting variable
# in terminal run, export API_KEY=sk-1234567890abcdef

# or we can use .env file



from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Now use your variables
api_key = os.environ.get('API_KEY')
debug = os.environ.get('DEBUG')

print(f"API Key: {api_key}")
print(f"Debug mode: {debug}")

# Full example
# app.py
from dotenv import load_dotenv
import os
import requests

# Load environment variables
load_dotenv()
# if .env file are in foldder and not in root use this
#load_dotenv("folder/.env")


# Get API key
API_KEY = os.environ.get('OPENAI_API_KEY')

if not API_KEY:
    print("Please set OPENAI_API_KEY in .env file")
    exit(1)

# Use the API
headers = {"Authorization": f"Bearer {API_KEY}"}
# Make your API calls...

