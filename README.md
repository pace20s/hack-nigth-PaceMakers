### About the project.
This project was built on HackNight (hackathon) organized by Sahyadri College of Engineering Mangalore

#### problem statement of choice. (Problem Statement 4)

*As part of typical business workflows, some organizations may need to send an adverse action letter to a customer / prospective customer. Examples of adverse action letters can be: a notice of foreclosure, a denial of application for a loan, etc. Organizations may want to send such a letter as a PDF document (through a short URL) and include a summary of the letter within the SMS. Design an algorithm to summarize an adverse action letter within 320 characters (including a sample short URL).*

**problem statement by www.solutionsbytext.com/**

### Our solution
* Our UI is built using Flask Python web framework, this front end will get inputs 1.FILE and 2.MOBILE NUMBER 
* The text will be extracted from the file for processing and summarizing 
* GPT3 is used and the summarization
* the summarised text is sent to the MOBILE NUMBER of the user with Twilio API.

### Run the app on your local machine.
```sh
go to the server folder
and run the server.py file

$ flask --app server run
```
*make sure to add your own Open AI GPT3 API keys in the server.py file*
