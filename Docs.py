# Replace with your API credentials and document ID
# ...

import json

# Authenticate with the Google Docs API
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

# Replace 'your-credentials.json' with the path to your service account key file
credentials = Credentials.from_service_account_file('your-credentials.json', scopes=['https://www.googleapis.com/auth/documents'])
service = build('docs', 'v1', credentials=credentials)

# Get the document content as JSON
document_content = service.documents().get(documentId="1HV8spdLUXbw5Pkffyy0yFnBERN7-ec-6dsgA0EHCy0I").execute()

# Save the JSON data to a file
with open('document.json', 'w') as f:
    json.dump(document_content, f, indent=4) 