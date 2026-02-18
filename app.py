from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Coding Q&A Database
qa_data = {
    "what is python": "🐍 **Python** is a high-level programming language. It's easy to learn and great for beginners! Created by Guido van Rossum in 1991.",
    
    "how to print in python": "📝 Use `print()` function:\n```python\nprint('Hello World!')\nname = 'John'\nprint(f'Hello, {name}')\n```",
    
    "what are variables": "📦 **Variables** store data:\n```python\nname = 'John'        # string\nage = 25            # integer\nprice = 19.99       # float\nis_student = True   # boolean\n```",
    
    "how to make a list": "📋 **Lists** store multiple items:\n```python\nfruits = ['apple', 'banana', 'orange']\nnumbers = [1, 2, 3, 4, 5]\nmixed = [1, 'hello', 3.14, True]\n\n# Access items\nprint(fruits[0])  # apple\n```",
    
    "what is a loop": "🔄 **Loops** repeat code:\n```python\n# For loop\nfor i in range(5):\n    print(i)  # 0,1,2,3,4\n\n# While loop\ncount = 0\nwhile count < 5:\n    print(count)\n    count += 1\n```",
    
    "how to define a function": "⚙️ **Functions** use 'def':\n```python\ndef greet(name):\n    return f'Hello, {name}!'\n\n# Call function\nresult = greet('John')\nprint(result)  # Hello, John!\n```",
    
    "what is if else": "🔀 **Conditionals**:\n```python\nage = 18\nif age >= 18:\n    print('Adult')\nelif age >= 13:\n    print('Teenager')\nelse:\n    print('Child')\n```",
    
    "what is coding": "💻 **Coding** is writing instructions for computers. It's like giving commands to a robot!",
    
    "how to start coding": "🚀 Start with Python! It's beginner-friendly. Practice daily, build small projects, and never give up!",
    
    "best language for beginners": "🐍 **Python** is the best for beginners! Simple syntax, huge community, and many job opportunities."
}

random_responses = [
    "❓ I'm still learning! Try asking about Python basics.",
    "💡 Ask me 'what is python' or 'how to print in python'",
    "📚 I know about variables, loops, lists, and functions!",
    "🔍 Try: 'how to make a list' or 'what is a loop'",
    "🎯 Ask me anything about Python programming!"
]

def find_answer(message):
    message = message.lower().strip()
    
    # Check exact matches
    if message in qa_data:
        return qa_data[message]
    
    # Check keywords
    if "print" in message:
        return qa_data["how to print in python"]
    if "list" in message or "array" in message:
        return qa_data["how to make a list"]
    if "loop" in message or "for" in message or "while" in message:
        return qa_data["what is a loop"]
    if "function" in message or "def" in message:
        return qa_data["how to define a function"]
    if "variable" in message:
        return qa_data["what are variables"]
    if "if" in message or "else" in message or "condition" in message:
        return qa_data["what is if else"]
    if "python" in message:
        return qa_data["what is python"]
    if "start" in message or "begin" in message:
        return qa_data["how to start coding"]
    if "best" in message or "language" in message:
        return qa_data["best language for beginners"]
    
    return random.choice(random_responses)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    response = find_answer(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)