def mood_response(mood):
    if mood == "happy":
        return "Today is a good day!"
    elif mood == "sad":
        return "I'm sorry to hear that! Have you considered going for a walk or reaching out to a friend?"
    elif mood == "excited":
        return "Woot! I'm hyped for you!"
    elif mood == "angry":
        return "We all get mad from time to time. Take a deep breath and count to four."
    else:
        return "Sorry, I'm a computer and my programmer did not think to include that mood. Blame them or feel free to share a different word for your mood?"