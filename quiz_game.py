playing = input('Do you want to play the game? (yes/no): ')
if playing.lower() != 'yes':
    print('Goodbye!')
    quit()
print("Ok! Let's play")
# questions
questions = [
    {"question": "What is my name? ", "answer": "Han"},
    {"question": "What is 1 + 1? ", "answer": "2"},
    {"question": "What is the capital of Vietnam? ", "answer": "Hanoi"},
    {"question": "What is the color of the sky? ", "answer": "blue"},
    {"question": "What programming language is this quiz written in? ", "answer": "Python"},
    {"question": "What does CPU stand for? ", "answer": "Central Processing Unit"},
    {"question": "What is the smallest prime number? ", "answer": "2"},
    {"question": "What is the chemical symbol for gold? ", "answer": "Au"},
    {"question": "Who developed the theory of relativity? ", "answer": "Albert Einstein"},
    {"question": "Does your family knows you're gay? ", "answer": ["Yes", "No"]}
]
# function to ask questions
def ask_question(question, answer):
    user_answer = input(question + "").strip()
    if user_answer.lower() == answer.lower():
        return True
    return False
# function to play the game
def play():
    score = 0
    print('Welcome to quiz game!')
    for q in questions:
        if ask_question(q['question'], q['answer']):
            print("Congratulations! ❤️")
            score += 10
        else:
            print("Incorrect! 🥱")
            score -= 10
    print(f'Your final score is {score}')
if __name__ == "__main__":
    play()