# YouTube-Transcript-Summarizer
Generate a summary of a youtube video transcript

# Objective

In this project, you will be a creating a Chrome Extension which will make a request to a backend REST API where it will perform NLP and respond with a summarized version of a YouTube transcript.

# Project Context

Enormous number of video recordings are being created and shared on the Internet through out the day. It has become really difficult to spend time in watching such videos which may have a longer duration than expected and sometimes our efforts may become futile if we couldn't find relevant information out of it. Summarizing transcripts of such videos automatically allows us to quickly look out for the important patterns in the video and helps us to save time and efforts to go through the whole content of the video.

This project will give us an opportunity to have hands on experience with state of the art NLP technique for abstractive text summarization and implement an interesting idea suitable for intermediates and a refreshing hobby project for professionals.

# Approach
1. Get transcripts/subtitles for a given YouTube video Id using a Python API.
2. Perform text summarization on obtained transcripts using HuggingFace transformers.
3. Build a Flask backend REST API to expose the summarization service to the client.
4. Develop a chrome extension which will utilize the backend API to display summarized text to the user.

# Applications
1. Meetings and video-conferencing - A system that could turn voice to text and generate summaries from your team meetings.
2. Patent research - A summarizer to extract the most salient claims across patents.

# Getting Started with the back-end
APIs changed the way we build applications, there are countless examples of APIs in the world, and many ways to structure or set up your APIs. In this milestone, we are going to see how to create a back-end application directory and structure it to work with the required files. We are going to isolate the back-end of the application to avoid the conflicting dependencies from other parts of the project.
# Requirements
* Create a back-end application directory containing files named as app.py and requirements.txt.
* Initialize app.py file with basic Flask RESTful BoilerPlate with the tutorial link as mentioned in the Reference Section below.
* Create a new virtual environment with pip installed which will act as an isolated location (a directory) where everything resides.
* Activate the newly formed virtual environment and install the following dependencies using pip:-
  * Flask
  * youtube_transcript_api
  * transformers[torch]
* Execute pip freeze and redirect the output to the requirements.txt file. This requirements.txt file is used for specifying what python packages are required to run the project.

# Get transcript for a given video
Ever wondered how to get your YouTube video's transcripts? In this milestone, we are going to utilize a python API which allows you to get the transcripts/subtitles for a given YouTube video. It also works for automatically generated subtitles, supports translating subtitles and it does not require a headless browser, like other selenium based solutions do!
# Requirements
In app.py,
* Create a function which will accept YouTube video id as an input parameter and return parsed full transcript as output.
* The response from the Transcript API will return a list of dictionaries looking somewhat like this:
  [
    {
        'text': 'Hey there',
        'start': 7.58,
        'duration': 6.13
    },
    {
        'text': 'how are you',
        'start': 14.08,
        'duration': 7.58
    },
     ...
] 
* Parse the data from the response to return the transcript in whole string format looking somewhat like this:
  Hey there how are you ... 

# Perform text summarization
Text summarization is the task of shortening long pieces of text into a concise summary that preserves key information content and overall meaning.
There are two different approaches that are widely used for text summarization:

* Extractive Summarization: This is where the model identifies the important sentences and phrases from the original text and only outputs those.
* Abstractive Summarization: The model produces a completely different text that is shorter than the original, it generates new sentences in a new form, just like humans do. In this project, we will use transformers for this approach.

In this milestone, we will use HuggingFace's transformers library in Python to perform abstractive text summarization on the transcript obtained from previous milestone.
