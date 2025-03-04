from agent import CustomerSupportBot

def main():
    bot = CustomerSupportBot()

    print("\nWelcome to AI Customer Support!")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        response = bot.get_response(user_input)
        print(f"Support AI: {response}")

if __name__ == "__main__":
    main()
