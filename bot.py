import openai
import requests

# Set up OpenAI API key
openai.api_key = "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"

# Set up Telegram API endpoint
TELEGRAM_API_ENDPOINT = "https://api.telegram.org/bot{}/sendMessage"

def handle_message(message_text):
    # Use the OpenAI API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{message_text}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    )

    # Get the response text
    response_text = response.choices[0].text

    # Send the response text to the user
    requests.post(
        TELEGRAM_API_ENDPOINT.format("5856485177:AAEmMpqh9tMLEQTFPkPYdoczyyN972lUjkY"),
        json={
            "chat_id": "https://t.me/wibe3_bot",
            "text": response_text
        }
    )

# Example usage
handle_message("Hello, how can I help you today?")
