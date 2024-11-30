# Blackboard-Vision
Blackboard-Vision is a Python project that filters images by identifying their content, specifically separating blackboard images from others. It utilizes machine learning and metadata to categorize images based on the class in which they were captured.

![explorer_mlfqvj4B2h](https://github.com/user-attachments/assets/024d61d6-3172-4262-a3e2-b4ff52c0bfe2)

For my personal use case, I use [Syncthing](https://syncthing.net/) to synchronize the pictures folder between devices (desktop and smartphone) and set Blackboard-Vision to run automatically when I'm not using my desktop. This has significantly improved my productivity in studying by eliminating the need to search for blackboard images among other pictures.
 

## How to Install
This app has been tested on Windows 10 using Python 3.12.7. Compatibility with other operating systems is not guaranteed.

1. Clone repository:

    ```git clone https://github.com/Vilefilipe1/Whiteboard-Vision.git```

2. Install the required dependencies:

    ```pip install -i requirements.txt```

3. Customize your schedule by modifying the read.py file (An interface for adjusting the schedule within the app is planned for future).

Example: For three classes on Monday and Wednesday:

    13:30/15:00 - PI
    15:10/17:20 - LP
    17:30/18:30 - C-B

Use conditional statements to filter by day (1 for Monday, 3 for Wednesday) and time:

```
 if (day_of_week == 1) or (day_of_week == 3): 
        # Monday ou Wednesday
        if (hour < 15) or ((hour == 15) and (min <= 10)):
            return "PI"  
        if (hour < 17) or ((hour <= 17) and (min <= 15)):
            return "LP"           
        else:
            return "C-B"
```

For time, be precise with time conditions (as for exemple in the first if, using one to assing to any hour before 15 and another one to hour 15 with any minutes before 10)

 
## How to Use
IMPORTANT: ENSURE YOU HAVE A BACKUP OF YOUR FOLDER BEFORE EXECUTING

Start the script:

```python ./read.py```

Follow the prompts to set up the source directory for filtering and the destination directory for sorted images. (Note: Cloud directories have not been tested, use at your own risk)

## To do

Implement an in-app interface for customizing schedules
 
