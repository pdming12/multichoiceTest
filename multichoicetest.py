from Questions import Question

question_prompt = [
  "Can you define something in Python?\n\nA. Yes\nB. No\n\n",
  "Is a Rubik's  Cube with one twisted corner solvable?\n\nA. Yes\nB. No\n\n",
  "Who is the person who made with this test?\n\n",
  "What year is it?\n\n"
]

questions = [
  Question(question_prompt[0], "A"),
  Question(question_prompt[1], "B"),
  Question(question_prompt[2], "Minh"),
  Question(question_prompt[3], "2022")
]

def runtest(questions):
  score = 0
  for question in questions:
    answer = input(question.prompt)
    if answer == question.answer:
      score = score + 1
  print(f"Score: {score} / {len(questions)}")

runtest(questions)
