from agent import CustomerSupportBot

def test_chatbot():
    bot = CustomerSupportBot()
    
    test_cases = [
        "Hello",
        "Where is my order?",
        "Can I return an item?",
        "How long does shipping take?",
        "What is the refund policy?",
        "I want to speak to a human"
    ]
    
    for test in test_cases:
        print(f"\nUser: {test}")
        print(f"Support AI: {bot.get_response(test)}")

if __name__ == "__main__":
    test_chatbot()
