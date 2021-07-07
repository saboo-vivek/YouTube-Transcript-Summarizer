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
# Requirements
In app.py,

* Create a function which will accept YouTube transcript as an input parameter and return summarized transcript as output.
* Instantiate a tokenizer and a model from the checkpoint name. Summarization is usually done using an encoder-decoder model, such as Bart or T5.
* Define the transcript that should be summarized.
* Add the T5 specific prefix “summarize: “.
* Use the PreTrainedModel.generate() method to generate the summary.
# Create REST API endpoint
The next step is to define the resources that will be exposed by this backend service. This is an extremely simple application, we only have a single endpoint, so our only resource will be the summarized text.

# Requirements
In app.py,

* Create a Flask API Route with GET HTTP Request method with a URI http://[hostname]/api/summarize?youtube_url=<url>.
* Extract the YouTube video id from the YouTube URL which is obtained from the query params.
* Generate the summarized transcript by executing the transcript generation function following the execution of transcript summarizer function.
* Return the summarized transcript with HTTP Status OK and handle HTTP exceptions if applicable.
* Run the Flask Application and test the endpoint in Postman to verify the appropriate results.

# Getting Started with Chrome Extension
Extensions are small software programs that customize the browsing experience. They enable users to tailor Chrome functionality and behavior to individual preferences. They are built on web technologies such as HTML, CSS and JavaScript. In this milestone, we are going to see how to create a recommended Chrome extension application directory and structure it to work with the required files.

# Requirements
* Create a chrome extension application directory containing essential files required as mentioned below.
  * images
  * background.js
  * contentScript.js
  * manifest.json
  * popus.css
  * popup.html
  * popup.js
 

* Paste the following code snippet in the manifest.json.
{ 
    "manifest_version": 2,
    "name": "YSummarize",
    "description": "An extension to provide summarized transcript of a YouTube Subtitle eligible     Video.",
    "version": "1.0",
    "permissions": ["activeTab"],


}

* And guess what? We already have enough to load our extension in the browser:
  * Just go to chrome://extensions and turn on developer mode from the top right-hand corner.
  * Then click on Load unpacked and select the folder containing the manifest file that we just created.
  * There you have it, our extension is up and running.
 
# Build a User Interface for Extension Popup
We need a user interface so that the user can interact with the popups which are one of several types of user interface that a Chrome extension can provide. They usually appear upon clicking the extension icon in the browser toolbar.

# Requirements
* Add the line below to page_action in the manifest file which enable the User Interface for a Popup.
{
 .
 .
 .
 "page_action": {
        "default_popup": "popup.html",
 }
 .
 .
}

* In the popup.html file,
   * Include the popup.css file to make the styles available to the HTML elements.
   * Include the popup.js file to enable user interaction and behavior with the HTML elements.
   * Add a button element named Summarize which when clicked will emit a click event which will be detected by an event listener to respond to it.
   * Add a div element where summarized text will be displayed when received from backend REST API Call.
* In popup.css file,
   * Provide appropriate CSS styling to the HTML elements 'button' and 'div' to have a better user experience.
 
 # Display Summarized transcript
We have provided a basic UI to enable users to interact and display the summarized text but there are some missing links which must be addressed. In this milestone, we will add a functionality to allow the extension to interact with the backend server using HTTP REST API Calls.

# Requirements
* In popup.js,

   * When DOM is ready, attach event listener with event type as "click" to the Summarize button and pass second parameter as an anonymous callback function.
   * In anonymous function, send an action message generate using chrome.runtime.sendMessage method to notify contentScript.js to execute summary generation.
   * Add event listener chrome.runtime.onMessage to listen message result from contentScript.js which will execute the outputSummary callback function.
   * In callback function, display the summary in the div element programmatically using Javascript.
* Add the line below to content_scripts in the manifest file which will inject the content script contentScript.js declaratively and execute the script automatically on a particular page.

{
 .
 .
 .
 "content_scripts":[
    {
      "matches":["https://www.youtube.com/watch?v=*"],
      "js": ["contentScript.js"]
    }
 ],
 .
 .
 .

}
* In contentScript.js,
   * Add event listener chrome.runtime.onMessage to listen message generate which will execute the generateSummary callback function.
   * In call back function, extract the URL of the current tab and make a GET HTTP request using XMLHTTPRequest Web API to the backend to receive summarized text as a response.
   * Send an action message result with summary payload using chrome.runtime.sendMessage to notify popup.js to display the summarized text.
