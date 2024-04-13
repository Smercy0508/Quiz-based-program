#python quiz game

questions=("What is the capital of India?: ",
           "How many bones are in the human body?: ",
           "How many continents are there in the world?: ",
           "How many days are there in a year?: ")

options=(("A. Rajasthan", "B. New Delhi","C. TamilNadu"),
         ("A.116", "B. 206","C.201"),
         ("A.7 ","B.6 ", "C. 8 "),
         ("A.366 ","B.367 ", "C.365"))

answers = ("B", "B", "A","C")
guesses = []
score = 0
question_num = 0

for question in questions:
  print(question)
  for option in options[question_num]:
    print(option)

  guess = input("Enter (A,B,C): ").upper()
  guesses.append(guess)
  if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
  else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
  question_num += 1
  
print(" RESULT ")
print("**********")

print("answer: ", end="")
for answer in answers:
    print(answer, end="")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end="")
print()

score = int(score / len(questions) * 100 )
print(f" Your Score is:{score}%")