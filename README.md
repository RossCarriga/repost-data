# repost-data
Project to track the most common repost on different subreddits. 

# Documentation (initial planning)
    1. Database
        - SQL database will be created to store useful information that we parse out of jsons from different subreddits.
    
    2. Gathering Posts
        - We will create a script to access json files containing information about different posts from subreddits.
        - This will find the fields we need and send their information to the SQL database.

    3. Processing
        - Data recieved from the gathering process will then be processed and given information that makes it useful to us.
        - This process ideally will expose information about how often the information is posted to reddit so that we can display that information.

    4. Displaying
        - We will be creating a frontend to this that will give a good idea about the information about groups of posts and individual posts themselves.
        