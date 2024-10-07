import InfoBlock as bl
import InfoBlocks as bls
import pandas as pd

file_path = "AnimalRightsOrgsUSA.csv"

encodings = ['utf-8', 'latin1', 'ISO-8859-1', 'cp1252', 'utf-16le']

for encoding in encodings:
    try:
        df = pd.read_csv(file_path, encoding=encoding)
        print(f"Successfully read the file with encoding: {encoding}")
        break
    except UnicodeDecodeError:
        print(f"Failed to decode with encoding: {encoding}")
else:
    print("All specified encodings failed. Check the file format or content.")
    
states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
    "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
    "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
    "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
    "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", 
    "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island",
    "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
    "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{state}</title>
    <link rel="stylesheet" href="../styles.css">
    <style>
        .desktop {{
            display: none;
        }}

        .mobile {{
            display: none;
        }}
    </style>
</head>
<body>
<div class="desktop">
<h1><b>{state}</b></h1>
<p>
    <a href="../Other%20HTML/General%20Vegan%20Information.html">General Vegan Information</a>&emsp;&emsp;
    <a href="../index.html">Vegan Information By US State</a>
</p>
<p>
    <img src="../Pics/Factory Farm Animals.png" width="1273" height="168">
</p>
    <div class="flex-container">
        <div class="column">
            <h4>{state} Animal Rights Organizations</h4>
            <ul>
            <li><a href="https://aldf.org/state/{state}/">Animal Legal Defense Fund</a></li>
            </ul>
        </div>
        <div class="column">
            <h4>{state} Animal Agriculture Videos</h4>
            <ul>
            </ul>
        </div>
        <div class="column">
            <h4>{state} Animal Sanctuaries</h4>
            <ul>
            </ul>
        </div>
        <div class="column">
    <h4>{state} Vegan Restaurant Guides</h4>
    <ul>
        <li><a href="https://www.happycow.net/north_america/usa/{lowerState}/">HappyCow - {state} Vegan Guide</a></li>
    </ul>
</div>
        <div class="column">
            <h4>{state} Vegan Facebook Groups</h4>
            <ul>
                <li><a href="https://facebook.com/search/top?q=Vegan{FBstate}">{state} Vegan Facebook Groups</a></li>
            </ul>
        </div>
    </div>
    <p>This website was created by Sean McKnelly. To reach me, send an email to veganinfo33@gmail.com.</p>
</div>
<div class="mobile">
    <h1><b>{state}</b></h1>
    <div class="vertical-container">
        <div class="child">
            &emsp;<a href="../Other%20HTML/General%20Vegan%20Information.html">General Vegan Information</a>
        </div>
        <div class="child">
            &emsp;<a href="../index.html">Vegan Information By US State</a>
        </div>
    </div>
</p>
    <div class="flex-container">
        <div class="column2">
            <h4>{state} Animal Rights Organizations</h4>
            <ul>
            <li><a href="https://aldf.org/state/{state}/">Animal Legal Defense Fund</a></li>
            </ul>
        </div>
        <div class="column2">
            <h4>{state} Animal Agriculture Videos</h4>
            <ul>
            </ul>
        </div>
    </div>
    <div class="flex-container">
        <div class="column2">
            <h4>{state} Animal Sanctuaries</h4>
            <ul>
            </ul>
        </div>
        <div class="column2">
    <h4>{state} Vegan Restaurant Guides</h4>
    <ul>
        <li><a href="https://www.happycow.net/north_america/usa/{lowerState}/">HappyCow - {state} Vegan Guide</a></li>
    </ul>
</div>
</div>
    <div class="flex-container">
        <div class="column2">
            <h4>{state} Vegan Facebook Groups</h4>
            <ul>
                <li><a href="https://facebook.com/search/top?q=Vegan{FBstate}">{state} Vegan Facebook Groups</a></li>
            </ul>
        </div>
    </div>
    <p>This website was created by Sean McKnelly. To reach me, send an email to veganinfo33@gmail.com.</p>
</div>
</div>
<script src="../scripts.js"></script> 
</body>
</html>
"""
blocks = bls.InfoBlocks()
df2 = df.reset_index(drop=True)

for i in range(len(df2) - 1):
    if df2.at[i, "Active"] == "Y":
        a = bl.InfoBlock(df2.at[i, 'description'],
                         df2.at[i, 'name'],
                         "Animal Rights Organization",
                         df2.at[i, 'State'])
        blocks.add(a)

a = bl.InfoBlock("https://www.youtube.com/watch?v=nk36rifq38w",
              "Drone Footage Exposes Real California Dairy Farm",
              "Animal Agriculture",
              "California")
blocks.add(a)
a = bl.InfoBlock("https://www.instagram.com/lovealwayssanctuary/",
                 "Love Always Sanctuary",
                 "Animal Sanctuary",
                 "California")
blocks.add(a)
a = bl.InfoBlock("https://www.instagram.com/farmanimalrefuge/",
                "Farm Animal Refuge",
                 "Animal Sanctuary",
                 "California")
blocks.add(a)
a = bl.InfoBlock("https://luvinarms.org/",
                 "Luvin Arms",
                 "Animal Sanctuary",
                 "Colorado")
blocks.add(a)
a = bl.InfoBlock("https://www.sagemtn.org/",
                 "Sage Mountain",
                 "Animal Sanctuary",
                 "Utah")
blocks.add(a)

a = bl.InfoBlock("https://www.facebook.com/groups/333822847614170",
                 "Glass Walls Experience",
                 "Animal Rights Organization",
                 "Utah")
blocks.add(a)
a = bl.InfoBlock("https://uarc.io/join/",
                 "Utah Animal Rights Coalition",
                 "Animal Rights Organization",
                 "Utah")
blocks.add(a)
a = bl.InfoBlock("https://casanctuary.org/",
                 "Catskill Aimal Sanctuary",
                 "Animal Sanctuary",
                 "New York")
blocks.add(a)
a = bl.InfoBlock("https://www.instagram.com/newlifeanimalsanctuary/",
                 "New Life Animal Sanctuary",
                 "Animal Sanctuary",
                 "California")
blocks.add(a)
a = bl.InfoBlock("https://www.rootssanctuary.org/",
                 "Roots Animal Sanctuary",
                 "Animal Sanctuary",
                 "New Mexico")
blocks.add(a)

a = bl.InfoBlock("https://www.facebook.com/alabamaanimalrights/",
                 "Alabama Animal Rights",
                 "Animal Rights Organization",
                 "Alabama")
blocks.add(a)
a = bl.InfoBlock("https://www.lovingfarm.org/",
                 "Loving Farm Animal Sanctuary",
                 "Animal Sanctuary",
                 "California")
blocks.add(a)
a = bl.InfoBlock('https://www.arthursacresanimalsanctuary.org/',
                 "Arthur's Acres Animal Sanctuary",
                 "Animal Sanctuary",
                 "New York")
blocks.add(a)
a = bl.InfoBlock("https://www.instagram.com/sunnyroseanimalsanctuary/",
                 "Sunny Rose Animal Sanctuary",
                 "Animal Sanctuary",
                 "California")
blocks.add(a)
a = bl.InfoBlock('https://skylandssanctuary.org/visit-2/',
                 "Skylands Animal Sanctuary and Rescue",
                 "Animal Sanctuary",
                 "New York")
blocks.add(a)
a = bl.InfoBlock("https://www.facebook.com/speaktucson/?paipv=0&eav=AfYcf6CG_WR4M16xBiVtZdERhLXvKtEXuUyG7GL2UagwJmrvWDG_zgr5IJMm0oZ0alY&_rdr",
                 "SPEAK Tucson",
                 "Animal Rights Organization",
                 "Arizona")
blocks.add(a)
a = bl.InfoBlock("https://www.alliedscholars.org/babson",
                 "Allied Scholars - Babson",
                 "Animal Rights Organization",
                 "Massachusetts")
blocks.add(a)
a = bl.InfoBlock("https://www.alliedscholars.org/berkeley",
                 "Allied Scholars - Berkeley",
                 "Animal Rights Organization",
                 "California")
blocks.add(a)
a = bl.InfoBlock("https://www.alliedscholars.org/brown",
                 "Allied Scholars - Brown",
                 "Animal Rights Organization",
                 "Minnesota")
blocks.add(a)
a = bl.InfoBlock("https://www.alliedscholars.org/columbia",
                 "Allied Scholars - Columbia",
                 "Animal Rights Organization",
                 "New York")
blocks.add(a)
a = bl.InfoBlock("https://www.alliedscholars.org/dartmouth",
                 "Allied Scholars - Dartmouth",
                 "Animal Rights Organization",
                 "New Hampshire")
blocks.add(a)
a = bl.InfoBlock("https://www.alliedscholars.org/harvard",
                 "Allied Scholars - Harvard",
                 "Animal Rights Organization",
                 "Massachusetts")
blocks.add(a)
a = bl.InfoBlock("https://www.alliedscholars.org/mit",
                 "Allied Scholars - MIT",
                 "Animal Rights Organization",
                 "Massachusetts")
blocks.add(a)
a = bl.InfoBlock("https://www.alliedscholars.org/ohiostate",
                 "Allied Scholars - Ohio State University",
                 "Animal Rights Organization",
                 "Massachusetts")
blocks.add(a)
a = bl.InfoBlock("https://www.alliedscholars.org/sam-houston-state",
                 "Allied Scholars - Sam Houston State",
                 "Animal Rights Organization",
                 "Texas")
blocks.add(a)
a = bl.InfoBlock("https://www.alliedscholars.org/tamu",
                 "Allied Scholars - Texas A&M",
                 "Animal Rights Organization",
                 "Texas")
blocks.add(a)
a = bl.InfoBlock("https://www.alliedscholars.org/uarizona",
                 "Allied Scholars - U of Arizona",
                 "Animal Rights Organization",
                 "Arizona")
blocks.add(a)
a = bl.InfoBlock("https://www.alliedscholars.org/uchicago",
                 "Allied Scholars - U of Chicago",
                 "Animal Rights Organization",
                 "Massachusetts")
blocks.add(a)
a = bl.InfoBlock("https://www.alliedscholars.org/university-of-north-texas",
                 "Allied Scholars - U of North Texas",
                 "Animal Rights Organization",
                 "Texas")
blocks.add(a)
a = bl.InfoBlock("https://www.alliedscholars.org/upenn",
                 "Allied Scholars - U of Pennsylvania",
                 "Animal Rights Organization",
                 "Pennsylvania")
blocks.add(a)
a = bl.InfoBlock("https://www.alliedscholars.org/utaustin",
                 "Allied Scholars - UT Austin",
                 "Animal Rights Organization",
                 "Texas")
blocks.add(a)
a = bl.InfoBlock("https://www.alliedscholars.org/uwmadison",
                 "Allied Scholars - UW Madison",
                 "Animal Rights Organization",
                 "Wisconsin")
blocks.add(a)
a = bl.InfoBlock("https://www.alliedscholars.org/yale",
                 "Allied Scholars - Yale",
                 "Animal Rights Organization",
                 "Connecticut")
blocks.add(a)
a = bl.InfoBlock("https://www.clementineranch.org/",
                 "Clementine Ranch",
                 "Animal Sanctuary",
                 "Utah")
blocks.add(a)
a = bl.InfoBlock("https://www.farmsanctuary.org/the-sanctuaries/watkins-glen-ny/",
                 "Farm Sanctuary - NY",
                 "Animal Sanctuary",
                 "New York")
blocks.add(a)
a = bl.InfoBlock("https://www.farmsanctuary.org/the-sanctuaries/los-angeles-ca/",
                 "Farm Sanctuary - CA",
                 "Animal Sanctuary",
                 "California")
blocks.add(a)
a = bl.InfoBlock("https://www.instagram.com/ashevilleanimalsave/",
                 "Animal Save - Asheville",
                 "Animal Rights Organization",
                 "North Carolina")
blocks.add(a)
a = bl.InfoBlock("https://www.instagram.com/chinoanimalsave/",
                 "Animal Save - Chino",
                 "Animal Rights Organization",
                 "California")
blocks.add(a)
a = bl.InfoBlock("https://www.instagram.com/denveranimalsave/",
                 "Animal Save - Denver",
                 "Animal Rights Organization",
                 "Colorado")
blocks.add(a)
a = bl.InfoBlock("https://www.instagram.com/kcanimalsave/",
                 "Animal Save - Kansas City",
                 "Animal Rights Organization",
                 "Missouri")
blocks.add(a)
a = bl.InfoBlock("https://www.instagram.com/lasvegasanimalsave/",
                 "Animal Save - Las Vegas",
                 "Animal Rights Organization",
                 "Nevada")
blocks.add(a)
a = bl.InfoBlock("https://www.instagram.com/animalalliancenetwork/",
                 "Animal Alliance Network - LA",
                 "Animal Rights Organization",
                 "California")
blocks.add(a)
a = bl.InfoBlock("https://www.instagram.com/laanimalsave/",
                 "Animal Save - LA",
                 "Animal Rights Organization",
                 "California")
blocks.add(a)
a = bl.InfoBlock("https://www.instagram.com/lafuranimalsave/",
                 "LA Fur Animal Save",
                 "Animal Rights Organization",
                 "California")
blocks.add(a)
'''
a = bl.InfoBlock("https://www.instagram.com/louisvillepigsave/",
                 "Louisville Pig Save",
                 "Animal Rights Organization",
                 "Kentucky")
blocks.add(a)
'''
a = bl.InfoBlock("https://www.instagram.com/milwaukeeanimalsave/",
                 "Animal Save - Milwaukee",
                 "Animal Rights Organization",
                 "Wisconsin")
blocks.add(a)
a = bl.InfoBlock("https://www.instagram.com/newarkanimalsave/",
                 "Animal Save - Newark",
                 "Animal Rights Organization",
                 "New Jersey")
blocks.add(a)
a = bl.InfoBlock("https://www.instagram.com/smithfieldanimalsrescue/",
                 "Animal Save - Smithfield",
                 "Animal Rights Organization",
                 "Virginia")
blocks.add(a)
a = bl.InfoBlock("https://www.facebook.com/StocktonAnimalSave",
                 "Animal Save - Stockton",
                 "Animal Rights Organization",
                 "California")
blocks.add(a)
a = bl.InfoBlock("https://www.instagram.com/tucsonanimalsave/",
                 "Animal Save - Tuscon",
                 "Animal Rights Organization",
                 "Arizona")
blocks.add(a)
a = bl.InfoBlock("https://www.instagram.com/centralpa_farmed_animal_save/",
                 "Animal Save - Central PA",
                 "Animal Rights Organization",
                 "Pennsylvania")
blocks.add(a)
a = bl.InfoBlock("https://www.facebook.com/groups/2095065820872274",
                 "Animal Save - Des Moines",
                 "Animal Rights Organization",
                 "Iowa")
blocks.add(a)
a = bl.InfoBlock("https://www.instagram.com/njanimalsavemovement/",
                 "NJ Animal Save Movement",
                 "Animal Rights Organization",
                 "New Jersey")
blocks.add(a)
a = bl.InfoBlock("http://instagram.com/nyfasave",
                 "NY Farmed Animal Save",
                 "Animal Rights Organization",
                 "New York")
blocks.add(a)
a = bl.InfoBlock("https://www.instagram.com/orange_county_animal_save/",
                 "Animal Save - Orange County",
                 "Animal Rights Organization",
                 "California")
blocks.add(a)
a = bl.InfoBlock("https://www.facebook.com/profile.php?id=100067538743599",
                 "Animal Save - Western PA",
                 "Animal Rights Organization",
                 "Pennsylvania")
blocks.add(a)
a = bl.InfoBlock("https://www.swoarn.org/",
                 "SWOARN - SW Ohio",
                 "Animal Rights Organization",
                 "Ohio")
blocks.add(a)
a = bl.InfoBlock("https://columbusanimaladvocates.org/",
                 "Columbus Animal Advocates",
                 "Animal Rights Organization",
                 "Ohio")
blocks.add(a)
a = bl.InfoBlock("https://www.foreverlandfarm.org/",
                 "Foreverland Farm",
                 "Animal Sanctuary",
                 "Ohio")
blocks.add(a)
a = bl.InfoBlock("https://redoakanimalrescue.com/",
                 "Red Oak Animal Rescue",
                 "Animal Sanctuary",
                 "Ohio")
blocks.add(a)
a = bl.InfoBlock("https://www.instagram.com/the.salty.sanctuary/",
                 "The Salty Sanctuary",
                 "Animal Sanctuary",
                 "Utah")
blocks.add(a)
a = bl.InfoBlock("https://wasatchwanderers.org/",
                 "Wasatch Wanderers Animal Rescue",
                 "Animal Sanctuary",
                 "Utah")
blocks.add(a)
a = bl.InfoBlock("https://www.ritzyrescueranch.org/",
                 "Ritzy Rescue Ranch",
                 "Animal Sanctuary",
                 "Utah")
blocks.add(a)
                 

for state in states:
    lines = html_template
    # ANIMAL SANCTUARY ADDITIONS     
    # ADD BLOCKS
    for block in blocks.arr:
        if block.category == "Animal Sanctuary" and block.state == state:
            lines = lines.splitlines()
        
            # New line to add
            new_line = """<li><a href=\"""" + block.url + "\">" + block.title + "</a></li>"

            # Insert the new line at the desired position (index 2 for the third line)
            lines.insert(87, new_line)

            # Join the lines back into a single text block
            lines = "\n".join(lines)
    # The Gentle Barn Addition
    if state in ["California", "Tennessee", "Missouri"]:
        # Convert text block to a list of lines
        lines = lines.splitlines()
        
        # New line to add
        new_line = """<li><a href="https://www.gentlebarn.org/visit/">The Gentle Barn</a></li>"""

        # Insert the new line at the desired position (index 2 for the third line)
        lines.insert(87, new_line)

        # Join the lines back into a single text block
        lines = "\n".join(lines)
    # ANIMAL AGRICULTURE ADDITIONS
    # Convert text block to a list of lines
    for block in blocks.arr:
        if block.category == "Animal Agriculture" and block.state == state:
            lines = lines.splitlines()
        
            # New line to add
            new_line = """<li><a href=\"""" + block.url + "\">" + block.title + "</a></li>"

            # Insert the new line at the desired position (index 2 for the third line)
            lines.insert(80, new_line)

            # Join the lines back into a single text block
            lines = "\n".join(lines)
    
    # ANIMAL RIGHTS ORGANIZATIONS ADDITIONS
    for block in blocks.arr:
        if block.category == "Animal Rights Organization" and block.state == state:
            lines = lines.splitlines()
        
            # New line to add
            new_line = """<li><a href=\"""" + block.url + "\">" + block.title + "</a></li>"

            # Insert the new line at the desired position (index 2 for the third line)
            lines.insert(75, new_line)

            # Join the lines back into a single text block
            lines = "\n".join(lines)
            
    if state in ["California", "Colorado", "Connecticut", "Florida", "Georgia",
                    "Illinois", "Maryland", "Massachusetts", "Michigan", "Minnesota",
                    "New Jersey", "New York", "Ohio", "Oregon", "Pennsylvania", "Texas"]:
        # Convert text block to a list of lines
        lines = lines.splitlines()
        
        # New line to add
        new_line = """<li><a href="https://www.anonymousforthevoiceless.org">Anonymous for the Voiceless - General Website</a></li>"""

        # Insert the new line at the desired position (index 2 for the third line)
        lines.insert(75, new_line)

        # Join the lines back into a single text block
        lines = "\n".join(lines)

    if state in states:
        # Convert text block to a list of lines
        lines = lines.splitlines()

        # New line to add
        new_line = """<li><a href="https://www.peta2.com/help-animals/activism-help/">SOS PETA - General Website</a></li>"""

        # Insert the new line at the desired position (index 2 for the third line)
        lines.insert(75, new_line)

        # New line to add
        new_line = """<li><a href="https://www.animalactivismmentorship.com/">Animal Activism Mentorship - General Website</a></li>"""

        # Insert the new line at the desired position (index 2 for the third line)
        lines.insert(75, new_line)

        # Join the lines back into a single text block
        lines = "\n".join(lines)

    # Direct Action Everywhere
    if state in ["California", "New York", "Texas", "Oregon",
                "Washington", "Illinois", "Michigan", "Massachusetts", "Florida"]:

        # Convert text block to a list of lines
        lines = lines.splitlines()

        # New line to add
        new_line = """<li><a href="https://www.directactioneverywhere.com/">Direct Action Everywhere - General Website</a></li>"""

        # Insert the new line at the desired position (index 2 for the third line)
        lines.insert(75, new_line)

        # Join the lines back into a single text block
        lines = "\n".join(lines)

    # Veggie Mijas
    if state in ["California", "New York", "Florida"]:

        # Convert text block to a list of lines
        lines = lines.splitlines()

        # New line to add
        new_line = """<li><a href="https://www.veggiemijas.com/">Veggie Mijas - General Website</a></li>"""

        # Insert the new line at the desired position (index 2 for the third line)
        lines.insert(75, new_line)

        # Join the lines back into a single text block
        lines = "\n".join(lines)

    # ANIMAL SANCTUARY ADDITIONS     
    # ADD BLOCKS
    for block in blocks.arr:
        if block.category == "Animal Sanctuary" and block.state == state:
            lines = lines.splitlines()
        
            # New line to add
            new_line = """<li><a href=\"""" + block.url + "\">" + block.title + "</a></li>"

            # Insert the new line at the desired position (index 2 for the third line)
            lines.insert(42, new_line)

            # Join the lines back into a single text block
            lines = "\n".join(lines)
    # The Gentle Barn Addition
    if state in ["California", "Tennessee", "Missouri"]:
        # Convert text block to a list of lines
        lines = lines.splitlines()
        
        # New line to add
        new_line = """<li><a href="https://www.gentlebarn.org/visit/">The Gentle Barn</a></li>"""

        # Insert the new line at the desired position (index 2 for the third line)
        lines.insert(42, new_line)

        # Join the lines back into a single text block
        lines = "\n".join(lines)

    # ANIMAL AGRICULTURE ADDITIONS
    # Convert text block to a list of lines
    for block in blocks.arr:
        if block.category == "Animal Agriculture" and block.state == state:
            lines = lines.splitlines()
        
            # New line to add
            new_line = """<li><a href=\"""" + block.url + "\">" + block.title + "</a></li>"

            # Insert the new line at the desired position (index 2 for the third line)
            lines.insert(37, new_line)

            # Join the lines back into a single text block
            lines = "\n".join(lines)

               
    # ANIMAL RIGHTS ORGANIZATIONS ADDITIONS
    for block in blocks.arr:
        if block.category == "Animal Rights Organization" and block.state == state:
            lines = lines.splitlines()
        
            # New line to add
            new_line = """<li><a href=\"""" + block.url + "\">" + block.title + "</a></li>"

            # Insert the new line at the desired position (index 2 for the third line)
            lines.insert(32, new_line)

            # Join the lines back into a single text block
            lines = "\n".join(lines)
            
    if state in ["California", "Colorado", "Connecticut", "Florida", "Georgia",
                    "Illinois", "Maryland", "Massachusetts", "Michigan", "Minnesota",
                    "New Jersey", "New York", "Ohio", "Oregon", "Pennsylvania", "Texas"]:
        # Convert text block to a list of lines
        lines = lines.splitlines()
        
        # New line to add
        new_line = """<li><a href="https://www.anonymousforthevoiceless.org">Anonymous for the Voiceless - General Website</a></li>"""

        # Insert the new line at the desired position (index 2 for the third line)
        lines.insert(32, new_line)

        # Join the lines back into a single text block
        lines = "\n".join(lines)
        
    #Veggie Mijas
    if state in ["California", "New York", "Florida"]:

        # Convert text block to a list of lines
        lines = lines.splitlines()

        # New line to add
        new_line = """<li><a href="https://www.veggiemijas.com/">Veggie Mijas - General Website</a></li>"""

        # Insert the new line at the desired position (index 2 for the third line)
        lines.insert(32, new_line)

        # Join the lines back into a single text block
        lines = "\n".join(lines)    
    # Direct Action Everywhere
    if state in ["California", "New York", "Texas", "Oregon",
                "Washington", "Illinois", "Michigan", "Massachusetts", "Florida"]:

        # Convert text block to a list of lines
        lines = lines.splitlines()

        # New line to add
        new_line = """<li><a href="https://www.directactioneverywhere.com/">Direct Action Everywhere - General Website</a></li>"""

        # Insert the new line at the desired position (index 2 for the third line)
        lines.insert(32, new_line)

        # Join the lines back into a single text block
        lines = "\n".join(lines)

    # SOS PETA & Animal Activism Mentorship
    if state in states:
        # Convert text block to a list of lines
        lines = lines.splitlines()

        # New line to add
        new_line = """<li><a href="https://www.peta2.com/help-animals/activism-help/">SOS PETA - General Website</a></li>"""

        # Insert the new line at the desired position (index 2 for the third line)
        lines.insert(32, new_line)

        # New line to add
        new_line = """<li><a href="https://www.animalactivismmentorship.com/">Animal Activism Mentorship - General Website</a></li>"""

        # Insert the new line at the desired position (index 2 for the third line)
        lines.insert(32, new_line)

        # Join the lines back into a single text block
        lines = "\n".join(lines)

    file_name = state.replace(" ", "_") + ".html"
    lowerState = state.replace(" ", "_").lower()
    FBstate = "%20" + state.replace(" ", "%20")
    with open("States//" + file_name, 'w') as file:
        file.write(lines.format(state=state, lowerState=lowerState, FBstate = FBstate))

print("HTML files for all 50 states have been created.")
