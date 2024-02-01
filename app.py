from flask import Flask, render_template, request
import openai
import json



# Get API key from environment variable

# openai.api_key=

def get_and_render_colors(msg):
  prompt= f"""
  You are a color pallette generating assistant that responds to text prompts for color palettes. You should generate color 
  palettes which match the mood, theme or instructions in the prompt. The palettes should be between 2 and 8 colors.

  Desired Format: JSON array of hexadecimal color codes. The response should be a JSON array. 

  Q: Generate me a list of random, sligtly generic colors. 
  A: ["#d65d14", "#dc1c0a", "#80e744", "#7b296b"]

  Q: The colors of Wes Andersons film, the grand Budapest hotel. 
  A: ["#ffd8ec", "#ffa8cb", "#e5000c", "#784283", "#ddd690"]

  Q: Convert the following verbal description of a color palette into a list of colors: {msg}
  A:
  """

  response = openai.Completion.create(
      model="gpt-3.5-turbo-instruct",
      prompt=prompt,
      max_tokens=200
  )

  return  json.loads(response['choices'][0]['text'])

app=Flask(__name__, template_folder='templates',static_url_path='', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/palette', methods=['POST'])
def prompt_to_palette():
    query=request.form.get('query')
    colors = get_and_render_colors(query)
    return {"colors": colors}


if __name__ =='__main__':
    app.run(debug=True)