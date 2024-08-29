import InfoBlock as bl
import InfoBlocks as bls

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
</head>
<body>
    <h1><b>{state}</b></h1>
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
</body>
</html>
"""
blocks = bls.InfoBlocks()
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
            lines.insert(25, new_line)

            # Join the lines back into a single text block
            lines = "\n".join(lines)
    # The Gentle Barn Addition
    if state in ["California", "Tennessee", "Missouri"]:
        # Convert text block to a list of lines
        lines = lines.splitlines()
        
        # New line to add
        new_line = """<li><a href="https://www.gentlebarn.org/visit/">The Gentle Barn</a></li>"""

        # Insert the new line at the desired position (index 2 for the third line)
        lines.insert(25, new_line)

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
            lines.insert(20, new_line)

            # Join the lines back into a single text block
            lines = "\n".join(lines)
                 
    # ANIMAL RIGHTS ORGANIZATIONS ADDITIONS
    for block in blocks.arr:
        if block.category == "Animal Rights Organization" and block.state == state:
            lines = lines.splitlines()
        
            # New line to add
            new_line = """<li><a href=\"""" + block.url + "\">" + block.title + "</a></li>"

            # Insert the new line at the desired position (index 2 for the third line)
            lines.insert(15, new_line)

            # Join the lines back into a single text block
            lines = "\n".join(lines)
    if state in ["California", "Colorado", "Connecticut", "Florida", "Georgia",
                    "Illinois", "Maryland", "Massachusetts", "Michigan", "Minnesota",
                    "New Jersey", "New York", "Ohio", "Oregon", "Pennsylvania", "Texas"]:
        # Convert text block to a list of lines
        lines = lines.splitlines()
        
        # New line to add
        new_line = """<li><a href="https://www.anonymousforthevoiceless.org">Anonymous for the Voiceless</a></li>"""

        # Insert the new line at the desired position (index 2 for the third line)
        lines.insert(15, new_line)

        # Join the lines back into a single text block
        lines = "\n".join(lines)

    # Mercy For Animals
    if state in ["California", "New York", "Texas"]:
        
        # Convert text block to a list of lines
        lines = lines.splitlines()

        # New line to add
        new_line = """<li><a href="https://mercyforanimals.org/">Mercy For Animals</a></li>"""

        # Insert the new line at the desired position (index 2 for the third line)
        lines.insert(15, new_line)

        # Join the lines back into a single text block
        lines = "\n".join(lines)
        
    # Animal Save Movement Addition    
    if state in ["California", "Colorado", "Florida", "Georgia", "Illinois",
                    "Maryland", "Massachusetts", "Michigan", "Minnesota", "New Jersey",
                    "New York", "Ohio", "Oregon", "Pennsylvania", "Texas", "Washington"]:
        
        # Convert text block to a list of lines
        lines = lines.splitlines()

        # New line to add
        new_line = """<li><a href="https://thesavemovement.org">Animal Save Movement</a></li>"""

        # Insert the new line at the desired position (index 2 for the third line)
        lines.insert(15, new_line)

        # Join the lines back into a single text block
        lines = "\n".join(lines)

    file_name = state.replace(" ", "_") + ".html"
    lowerState = state.replace(" ", "_").lower()
    FBstate = "%20" + state.replace(" ", "%20")
    with open("States//" + file_name, 'w') as file:
        file.write(lines.format(state=state, lowerState=lowerState, FBstate = FBstate))

print("HTML files for all 50 states have been created.")
