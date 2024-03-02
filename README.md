# Project Setup Instructions

Follow these step-by-step instructions to successfully run and test our FastAPI project.

## Step 1: Unzip the Project

Begin by unzipping the project file and extracting the folder.

## Step 2: Open in VS Code

Launch Visual Studio Code and open the extracted folder to facilitate a smooth development experience.

## Step 3: Install Dependencies and Run the Server

Open a terminal in VS Code and execute the following commands to install the required packages and start the FastAPI server:

```bash
# Install the packages listed in the requirements.txt file
pip install -r requirements.txt

# Run the FastAPI server
python main.py
```

The server will be accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Step 4: Explore Interactive Documentation

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your web browser to access the interactive documentation. Here, you can conveniently test and send HTTP requests directly from the documentation, thanks to FastAPI's special features.

## Step 5: Postman Integration

For additional testing capabilities, open Postman and import the provided file. This file contains all 15 API links for the tasks, allowing you to send HTTP requests and observe responses using Postman.

## Step 6: Dynamic Parameters

Certain HTTP links include dynamic parameters such as `student_id` and `course_id`. Adjust these parameters as needed to explore different functionalities. Refer to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for schema details and guidance on what to include in POST methods.
