import time
import random

def sarcastic_response(question):
    responses = [
        "Oh, absolutely! Because that's the most important question in the world right now.",
        "Wow, what a deep thinker we have here. Let me overthink this for you.",
        "Do you really think *I* have the answer to that? Bold of you to assume!",
        "Sure, let me just consult my crystal ball. Oh wait, it's broken.",
        "Are you sure you want to know the answer? It might change your life... or not.",
        "Ah, yes, the meaning of life is clearly hidden in that question. Definitely."
    ]

    # Random delay for dramatic effect
    print("Let me think...")
    time.sleep(random.randint(1, 3))
    
    return random.choice(responses)

def main():
    print("Welcome to the Sarcastic Assistant! I'm here to answer your questions, but don't expect much.")
    print("Type 'quit' to exit, because I know you'll miss me.")

    while True:
        question = input("What's your question? ")
        
        if question.lower() == 'quit':
            print("Oh, leaving already? Typical. Bye!")
            break

        if not question.strip():
            print("Wow, a blank question. Let me use my psychic powers for this one...")
            continue

        # Generate a sarcastic response
        response = sarcastic_response(question)
        print(response)

if __name__ == "__main__":
    main()

