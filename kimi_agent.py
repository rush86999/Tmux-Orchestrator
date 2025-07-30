import openai
import os
import sys

def get_kimi_response(prompt):
    """
    Sends a prompt to the Kimi K2 model and returns the response.
    """
    try:
        # It's recommended to set the API key as an environment variable
        # for security reasons.
        api_key = os.environ.get("MOONSHOT_API_KEY")
        if not api_key:
            raise ValueError("MOONSHOT_API_KEY environment variable not set.")

        client = openai.OpenAI(
            api_key=api_key,
            base_url="https://api.moonshot.ai/v1",
        )

        completion = client.chat.completions.create(
            model="moonshot-v1-8k",  # Or another suitable Kimi model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.3,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        prompt = " ".join(sys.argv[1:])
        response = get_kimi_response(prompt)
        print(response)
    else:
        print("Usage: python kimi_agent.py <prompt>")
