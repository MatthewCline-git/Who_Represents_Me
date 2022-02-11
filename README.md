## Who Represents Me?

## By Matthew Cline

## Project Documentation

Who Represents Me is a web application that empowers users with information about the elected 
officials who represent them at all levels of government, from the Commander-in-Chief to the
local dog catcher. The project sources its information from the Google Civic API.

When you open the homepage (index.html), you'll find a text box prompting for a standard,
5-digit U.S. zip code. Entering any other sort of input, whether one with more than five 
digits or containing non-numeric characters, will yield an error. 

Once you submit the form with the five-digit zip code, you will see a table that displays
multiple civic engagement resources. At the top of the table is a clickable header, which
will navigate the user to the League of Women Voter's Vote411 page for the state
that corresponds to the user-provided zip code. This page displays nonpartisan election
and voter registration information. 

The remaining rows of the table display the names and essential information about all
elected officials who represent residents of the entered zip code. This information 
includes the name, office, party, address, phone number, and email of those elected
officials. The table also contains links to a voter guide for writing elected officials.
It also contains buttons that activate the native telephone and email clients of the users
device to call or draft an email, respectively, to the corresponding legislator. 

For a small minority of cases, the Google Civic API will not have complete information
for an elected official. In these cases, error messages display within the table. 

On the technical side, the meat and potatoes of this project is in app.py and 
results.html. I'll explain briefly here and elaborate in DESIGN.md. app.py initiates flask 
and defines three functions. The most important is def display(). This function retrieves
the user-provided zipcode, uses that info to make a request of the Google Civic API. Then,
that data is parsed into two three dictionaries that I use to create the table. I do some
extensive data cleaning to make it usable and return it to results.html. 

In results.html, I make extensive use of jinja templating and original css formatting to 
present the data. All of the information is presented via table entries that retrieve 
information passed in by the display() function. 