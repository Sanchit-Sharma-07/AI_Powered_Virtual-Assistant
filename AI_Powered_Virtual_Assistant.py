from google import genai

client = genai.Client(api_key="")

def ask_ai(query):
    response = client.models.generate_content(
        model="gemini-2.5-flash",  
        contents=query
    )
    return response.text

print("🤖AI Assistant Ready! (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("AI: Goodbye! 👋")
        break
    reply = ask_ai(user_input)
    print(f"AI: {reply}")
