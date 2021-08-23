from flask import Flask, request
from flask_restful import Resource,Api
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import T5ForConditionalGeneration, T5Tokenizer
from transformers import pipeline
# define flask app 
app = Flask(__name__)
# creating an API object
#api=Api(app)


@app.route('/api/<string:video_id>')
# video id= _wiBNJyEC8c&list=PLZnxqowr6IKhMv9_rzass-qWavKE7_SHB
#getting transcrit
def get_YTscript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    script=""
    for i in (transcript):
        script += i["text"]+" " 
    return (summarize_t5(script))
        
#summarize via t5 
def summarize_t5(script):
    model = T5ForConditionalGeneration.from_pretrained("t5-base")
    tokenizer = T5Tokenizer.from_pretrained("t5-base")
    # encode the text into tensor of integers using the 
    # appropriate tokenizer
    inputs = tokenizer.encode(
        "summarize: " + script,
        return_tensors="pt",
        max_length=1024,
        truncation=True)
    # generate the summarization output
    outputs = model.generate(
        inputs, 
        max_length=512, 
        min_length=40, 
        length_penalty=2.0, 
        num_beams=4, 
        early_stopping=True)
    # just for debugging
    return (tokenizer.decode(outputs[0]))

# summarise via pipeline api
def summarize_pipe(script):
    summarization=pipeline("summarization")
    summary=summarization(script)[0]['summary']
    return(summary)

    



# server the app when this file is run
if __name__ == '__main__':
    app.run(debug=True)
   
