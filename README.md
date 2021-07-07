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
1. Patent research - A summarizer to extract the most salient claims across patents.
