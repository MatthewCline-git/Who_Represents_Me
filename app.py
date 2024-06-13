import requests 
from flask import Flask, render_template, request

app = Flask(__name__)

# Constants for API URL and key
API_URL = 'https://www.googleapis.com/civicinfo/v2/representatives'
API_KEY = 'YOUR_API_KEY_HERE'

# Mapping of state abbreviations to full names
STATE_ABBREV_TO_NAME = {
    "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas", "CA": "California",
    "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware", "DC": "District of Columbia",
    "FL": "Florida", "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho", "IL": "Illinois",
    "IN": "Indiana", "IA": "Iowa", "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana",
    "ME": "Maine", "MD": "Maryland", "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota",
    "MS": "Mississippi", "MO": "Missouri", "MT": "Montana", "NE": "Nebraska", "NV": "Nevada",
    "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico", "NY": "New York",
    "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma",
    "OR": "Oregon", "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina",
    "SD": "South Dakota", "TN": "Tennessee", "TX": "Texas", "UT": "Utah", "VT": "Vermont",
    "VA": "Virginia", "WA": "Washington", "WV": "West Virginia", "WI": "Wisconsin", "WY": "Wyoming"
}

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def display():
    zipcode = request.form.get("zipcode")

    if not zipcode or not zipcode.isdigit() or len(zipcode) != 5:
        return render_template("error.html", message="Please enter a valid 5-digit zip code.")

    url = f"{API_URL}?address={zipcode}&key={API_KEY}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        officials = data.get('officials', [])
        offices = data.get('offices', [])
        normalized_input = data.get('normalizedInput', {})

        # Add 'office' information to each official based on officialIndices
        for official in officials:
            official['office'] = next(office['name'] for office in offices if official['officeIndices'][0] in office['officialIndices'])

        # Normalize state name
        if normalized_input.get('state'):
            normalized_input['state'] = STATE_ABBREV_TO_NAME.get(normalized_input['state'], normalized_input['state'])

        return render_template("results.html", offices=offices, officials=officials, normal=normalized_input)

    except requests.exceptions.RequestException as e:
        return render_template("error.html", message=f"Error fetching data: {str(e)}")

    except (KeyError, IndexError) as e:
        return render_template("error.html", message="Error parsing data from API response.")
