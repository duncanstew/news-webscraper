Files to Add:
    - client_secret.json
    - .ppk file

Files to edit:
    - info.txt {Search Criteria}
    - requirements.txt {Install}
    - scrape.py {PAGES_TO_SCRAPE var}
    - gcintegration.py {COLOR var}

Step 0: {client_secret.json}
    - In order for this to work, you will need to enable the google calendar API. 
    - https://dev.to/megazear7/google-calendar-api-integration-made-easy-2a68
    - This article has the basic steps for retrieving the json file, and you don't need to follow the rest of the steps, only up until 
    securing your json file. Name it: client_secret.json

Step 0.5: (.ppk file)
    - To make this file run autonomously, you have multiple options but I went with hosting an ec-2 instance on AWS. If you use Putty for 
    accessing servers, you will need to create a .ppk file, which originates from the .pem file you download when you generate your instance. 
    Just upload the .pem file into PuttyGen and it will generate the .ppk file. 

Step 1: {Search Criteria}
    a. In the info.txt file, add all search terms that you would be interested in viewing articles of. Any terms listed will be
    used for searching article titles. Any matching titles with matching words will be saved and outputted to calendar.
    b. case sensitivity does not matter

Step 2: {Install}
    - setup a venv
    - run command: pip install --upgrade requirements.txt

Step 3: {PAGES_TO_SCRAPE}
    - In scrape.py file, edit variable: PAGES_TO_SCRAPE. Each page contains around 30 entries. 4 pages = 120 entries to draw from. 
    - As hacker news is updated daily, don't increment the number of pages too much or you will have article overlap in consecutive days

Step 4: {COLOR}
    - Minor detail but to change the color of your google calendar event, change the integer for COLOR var. 
    - Table below demonstrates all the potential options for customization.
        Replace COLOR with Color ID

        Color ID	Color Name	    Hex Code
        undefined	Who knows	    #039be5
        1	        Lavender	    #7986cb
        2	        Sage	        #33b679
        3	        Grape	        #8e24aa
        4	        Flamingo	    #e67c73
        5	        Banana	        #f6c026
        6	        Tangerine	    #f5511d
        7	        Peacock	        #039be5
        8	        Graphite	    #616161
        9	        Blueberry	    #3f51b5
        10	        Basil	        #0b8043
        11	        Tomato	        #d60000

