# import os
import requests 
from flask import Flask, flash, jsonify, redirect, render_template, request, session, redirect, url_for

# setting up flast was from lecture 9
app = Flask(__name__)

# see vid above
s = 'https://www.googleapis.com/civicinfo/v2/representatives?address='
k = '&key=YOUR_API_KEY_HERE'

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def display():
    #validate submission
    zipcode = request.form.get("zipcode")
    # provice errors in case of empty form or invalid completion
    if not zipcode:
        return render_template("error.html", message="Please enter a zip code")
    if not (len(zipcode) == 5):
        return render_template("error.html", message="Zip codes must be five digits")
    if not zipcode.isdecimal():
        return render_template("error.html", message="Zip codes must be only numbers")

    # format url with boilerplate that's always the same  and the zipcode which changes from query to query
    url = s + zipcode + k
    
    r = requests.get(url)
    d_dict = r.json()
    
    # creating dictionaries from just the data I want
    officials = d_dict['officials']
    offices = d_dict['offices']
    # this one's a list technically
    normal = d_dict['normalizedInput']
    # did a lot of work on this on Office Hours Sunday with a TA, I think named Austin?
    for official in officials:
        # if no address, set value of query I'll use to get address to empty, so there's at least something there
        if not ('geocodingSummaries' in official):
            empty = dict()
            empty['queryString'] = "NA"
            official['geocodingSummaries'] = [empty]
        # if there's no phone number, set the value of phone number to none on file
        if not('phones' in official):
            official['phones'] = ["No phone number on file :("]
        # same 
        if not('emails' in official):
            official['emails'] = ["No email on file :("]
    # pair office and officials on officialIndices, worked on this with Ally
    for i in range(len(officials)):
        for office in offices:
           if i in office["officialIndices"]:
               officials[i]["office"] = office["name"]
    if normal['state'] == "AL":
        normal['state'] = 'Alabama'
    if normal['state'] == "AK":
        normal['state'] = 'Alaska'
    if normal['state'] == "AZ":
        normal['state'] = 'Arizona'
    if normal['state'] == "AR":
        normal['state'] = 'Arkansas'
    if normal['state'] == "CA":
        normal['state'] = 'California'
    if normal['state'] == "CO":
        normal['state'] = 'Colorado'
    if normal['state'] == "CT":
        normal['state'] = 'Connecticut'
    if normal['state'] == "DE":
        normal['state'] = 'Delaware'
    if normal['state'] == "DC":
        normal['state'] = 'District-Of-Columbia'
    if normal['state'] == "FL":
        normal['state'] = 'Florida'
    if normal['state'] == "GA":
        normal['state'] = 'Georgia'
    if normal['state'] == "HI":
        normal['state'] = 'Hawaii'
    if normal['state'] == "ID":
        normal['state'] = 'Indiana'
    if normal['state'] == "IL":
        normal['state'] = 'Illinois'
    if normal['state'] == "IN":
        normal['state'] = 'Indiana'
    if normal['state'] == "IA":
        normal['state'] = 'Iowa'
    if normal['state'] == "KS":
        normal['state'] = 'Kansas'
    if normal['state'] == "KY":
        normal['state'] = 'Kentucky'
    if normal['state'] == "LA":
        normal['state'] = 'Louisiana'
    if normal['state'] == "ME":
        normal['state'] = 'Maine'
    if normal['state'] == "MD":
        normal['state'] = 'Maryland'
    if normal['state'] == "MA":
        normal['state'] = 'Massachusetts'
    if normal['state'] == "MI":
        normal['state'] = 'Michigan'
    if normal['state'] == "MN":
        normal['state'] = 'Minnesota'
    if normal['state'] == "MS":
        normal['state'] = 'Mississippi'
    if normal['state'] == "MO":
        normal['state'] = 'Missouri'
    if normal['state'] == "MT":
        normal['state'] = 'Montana'
    if normal['state'] == "NE":
        normal['state'] = 'Nebraska'
    if normal['state'] == "NV":
        normal['state'] = 'Nevada'
    if normal['state'] == "NH":
        normal['state'] = 'New-Hampshire'
    if normal['state'] == "NJ":
        normal['state'] = 'New-Jersey'
    if normal['state'] == "NM":
        normal['state'] = 'New-Mexico'
    if normal['state'] == "NY":
        normal['state'] = 'New-York'
    if normal['state'] == "NC":
        normal['state'] = 'North-Carolina'
    if normal['state'] == "ND":
        normal['state'] = 'North-Dakota'
    if normal['state'] == "OH":
        normal['state'] = 'Ohio'
    if normal['state'] == "OK":
        normal['state'] = 'Oklahoma'
    if normal['state'] == "OR":
        normal['state'] = 'Oregon'
    if normal['state'] == "PA":
        normal['state'] = 'pennsylvania'
    if normal['state'] == "RI":
        normal['state'] = 'Rhode-Island'
    if normal['state'] == "SC":
        normal['state'] = 'South-Carolina'
    if normal['state'] == "SD":
        normal['state'] = 'South-Dakota'
    if normal['state'] == "TN":
        normal['state'] = 'Tennessee'
    if normal['state'] == "TX":
        normal['state'] = 'Texas'
    if normal['state'] == "UT":
        normal['state'] = 'Utah'
    if normal['state'] == "VT":
        normal['state'] = 'Vermont'
    if normal['state'] == "VA":
        normal['state'] = 'Virginia'
    if normal['state'] == "WA":
        normal['state'] = 'Washington'
    if normal['state'] == "WV":
        normal['state'] = 'West-Virginia'
    if normal['state'] == "WI":
        normal['state'] = 'Wisconsin'
    if normal['state'] == "WY":
        normal['state'] = 'Wyoming'
    # right side of equals is name of variable in app.py; left is name in template
    return render_template("results.html", offices=offices, officials=officials, normal=normal)
