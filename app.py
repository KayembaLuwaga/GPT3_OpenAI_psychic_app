from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Dummy function for interacting with OpenAI API
def get_openai_quotes(api_key, age_group, gender):
    # Set the OpenAI API key dynamically based on user input
    openai.api_key = api_key

    # Define the prompt for the OpenAI API
    prompt = f"Write excellent positive-well being vibes, motivation quotes for me, a person in age range {age_group}, my gender is {gender}"

    # Make a request to the OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-002",  # Use an appropriate engine
        prompt=prompt,
        max_tokens=100  # Adjust based on your needs
    )

    # Extract the generated quote from the API response
    generated_quote = response['choices'][0]['text']

    return generated_quote

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_quotes', methods=['POST'])
def get_quotes():
    # Get input from the form
    api_key = request.form.get('api_key')
    age_group = request.form.get('age_group')
    gender = request.form.get('gender')

    # Validate API key
    # if api_key != 'your_api_key':  # Replace 'your_api_key' with your actual API key
    #     return render_template('index.html', error='Invalid API key')

    # Include age group and gender in the request to OpenAI
    openai_response = get_openai_quotes(api_key, age_group, gender)

    return render_template('index.html', quotes=openai_response)

if __name__ == '__main__':
    app.run(debug=True)
