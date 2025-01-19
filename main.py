from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# OpenAI client setup
token = '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'
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

@app.route('/')
def home():
    return render_template('index.html')  # Serves the HTML page

@app.route('/generate_kundali', methods=['POST'])
def generate_kundali():
    data = request.form
    name = data.get('name')
    dob = data.get('dob')
    time = data.get('time')
    city = data.get('city')
    state = data.get('state')

    # Compose the user input
    user_input = (
        f"Name: {name}, DOB: {dob}, Time: {time}, City: {city}, State: {state}"
    )

    try:
        # OpenAI API call
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Act like an astrologer. Based on the user inputs generate a horoscopic data. "
                        "Containing below mentioned data: 1. Basic Birth Information 2. Ascendant (Lagna) "
                        "3. Moon Sign (Rashi) 4. Sun Sign 5. Planetary Positions 6. Houses (Bhavas) "
                        "7. Dashas (Planetary Periods) 8. Navamsa Chart 9. Yogas 10. Aspects (Drishti) "
                        "11. Strength of Planets 12. Nakshatras 13. Divisional Charts (Vargas) 14. Shadbala "
                        "15. Transits (Gochara) 16. Ashta Vargas, The system will provide insights, recommendations, and rituals based on user birth details, along with an interactive chatbot for spiritual advice."
                    ),
                },
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            temperature=1.0,
            top_p=1.0,
            max_tokens=6000,
            model=model_name
        )

        # Extract and return the response content
        result = response.choices[0].message.content
        print(response.choices[0].message.content)
        print(jsonify({"success": True, "kundali": result}))
        return jsonify({"success": True, "kundali": result})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
