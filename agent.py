import google.generativeai as genai
from config import get_genai_model  # Import API configuration

class CustomerSupportBot:
    def __init__(self):
        self.model = get_genai_model()  # Use the model from config.py

        self.knowledge_base = {
    "greeting": [
        "Hello! I'm your AI customer support assistant. How can I help you today?",
        " Hi there! I'm here to assist you. What can I do for you today?"
    ],
    
    # 🛍️ ORDER STATUS & TRACKING
    "order status": [
        " I'd be happy to check your order status! Can you provide your order number?",
        " Tracking your order is easy! Please share your **order number**, and I'll find the details for you."
    ],
    "track order": [
        " Sure! To track your order, visit [Tracking Link] or share your order number, and I'll check for you.",
        " Let me pull up your tracking details. What’s your **order number?"
    ],

    # SHIPPING & DELIVERY
    "shipping time": [
        " Standard shipping takes 5–7 business days for domestic orders.",
        " International shipping usually takes 10–15 business days, depending on customs clearance."
    ],
    "international shipping": [
        " We ship worldwide! Can you tell me which country you’re in so I can check the estimated delivery time?",
        " International orders take 10–15 business days. Let me know if you need express shipping options!"
    ],
    "express shipping": [
        " Need it faster? We offer express shipping (2–3 business days) for an extra fee.",
        " Express delivery takes 2–3 business days. Would you like to upgrade?"
    ],
    "delayed delivery": [
        " Sorry for the delay! Let me check your tracking details. Could you share your order number?",
        " Sometimes delays happen due to customs or weather conditions. Let me check your tracking info."
    ],

    #  REFUNDS & RETURNS
    "refund policy": [
        " You can request a refund within **30 days of delivery** if the item is unused and in its original packaging.",
        " Refunds take **5–7 business days** to process. Let me check your order details!"
    ],
    "return item": [
        " To return an item, please provide your **order number** and reason for return. I’ll guide you through the process!",
        " Returns are accepted within **30 days**. Do you need a prepaid return label?"
    ],
    "exchange policy": [
        " Need an exchange? We accept exchanges within **30 days** for unused items. What’s your order number?",
        " We can exchange your item if it's in original condition. Let me get that started for you!"
    ],

    # 🔧 PRODUCT ISSUES & WARRANTY
    "warranty claim": [
        " Your product comes with a **1-year warranty**. If you’re experiencing an issue, I can start a claim.",
        " Warranty covers **manufacturing defects**. Can you describe the issue or upload a picture?"
    ],
    "product not working": [
        " Sorry to hear that! Let’s troubleshoot. Is the device turning on? Have you tried resetting it?",
        " If the issue persists, I can arrange a replacement or repair. Want me to check your warranty status?"
    ],
    "damaged item": [
        " Oh no! If your item arrived damaged, we’ll replace it. Please send a **photo** and your **order number**.",
        " We’re sorry about this! I can assist with a replacement or refund. Let me check your order details."
    ],
    
    #  DISCOUNTS & PROMOTIONS
    "discount code": [
        " New customer? Use **WELCOME10** for 10% off your first order!",
        " We have a special **flash sale** this week! Would you like to see the best deals?"
    ],
    "loyalty program": [
        " Join our loyalty program to earn **points on every purchase**! Would you like to sign up?",
        " Earn rewards and exclusive discounts as a loyalty member! Want me to sign you up?"
    ],

    #  HUMAN ESCALATION
    "speak to human": [
        " I’d be happy to transfer you! Can you share your **order number** or issue so I can direct you to the right team?",
        " I understand this needs a personal touch. Let me gather some details so our agent can assist you better."
    ],
    "contact support": [
        " You can contact our support team via **support@example.com** or call **+1234567890** (Mon-Fri, 9 AM-6 PM).",
        " Need urgent help? Live agents are available **Monday-Friday, 9 AM - 6 PM (UTC)**."
    ],
    
    #  GENERAL FAQs
    "business hours": [
        " Our support team is available **Monday-Friday, 9 AM-6 PM (UTC)**.",
        " Our working hours are **9 AM - 6 PM, Monday to Friday**."
    ],
    "payment methods": [
        " We accept **Visa, Mastercard, PayPal, and Apple Pay**.",
        " Your payment is secure! We accept **major credit/debit cards and PayPal**."
    ],
    "cancellation policy": [
        " You can cancel your order within **24 hours of purchase** for a full refund.",
        " Need to cancel? If your order hasn’t shipped yet, I can process a cancellation."
    ],
    
    # 🤖 AI CONFIRMATION
    "ai assistant": [
        " Just so you know, I'm an AI assistant! I'm here to help, but I can transfer you to a human if needed.",
        " I’m an AI customer support assistant, trained to assist with your queries. Let me know how I can help!"
    ]
        }

    def call_llm(self, user_input):
        """Call Google Gemini AI to generate a response"""
        try:
            response = self.model.generate_content(user_input)
            return response.text.strip()
        except Exception as e:
            return f"❌ Error: {str(e)}"

    def get_response(self, user_input):
        """Get response from the knowledge base or call AI"""
        user_input = user_input.lower()
        for key in self.knowledge_base:
            if key in user_input:
                return self.knowledge_base[key][0]  # Return a predefined response

        # If no predefined response, use AI model
        return self.call_llm(user_input)
