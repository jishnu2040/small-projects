questions = [
  [
        "Which language was used to create Facebook?",
        "Python", "French", "JavaScript", "Php", None, 4
    ],
    [
        "What programming language is commonly used for web development and was originally developed by Guido van Rossum?",
        "Python", "Java", "C++", "Ruby", None, 1
    ],
    [
        "Which programming language is primarily used for client-side web development?",
        "Python", "French", "JavaScript", "Php", None, 3
    ],
    [
        "What programming language is commonly used for server-side scripting and web development?",
        "Python", "French", "JavaScript", "Php", None, 4
    ],
     [
        "Which programming language is known for its simplicity, readability, and versatility, making it suitable for various applications including web development, scientific computing, and artificial intelligence?",
        "Python", "Java", "C++", "Ruby", None, 1
    ],
    [
        "What programming language is commonly used for building mobile applications, especially for Android devices?",
        "Python", "Java", "Swift", "C#", None, 2
    ],
    [
        "Which language is commonly used for data analysis, statistical modeling, and machine learning?",
        "Python", "Java", "R", "Scala", None, 3
    ],
    [
        "What language is primarily used for creating dynamic and interactive web pages?",
        "Python", "French", "JavaScript", "Php", None, 3
    ],
    [
        "Which language is often used for game development, particularly for indie games and mobile games?",
        "Python", "JavaScript", "C#", "UnityScript", None, 3
    ],
    [
        "What language is commonly used for system administration, automation, and configuration management?",
        "Python", "Bash", "Ruby", "Perl", None, 2
    ]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(questions)):
  
  question = questions[i]
  
  print(f'\n\n{i+1}.{question[0]}')
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}          d. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
      money = 320000
    elif(i == 14):
      money = 10000000
  else:
    print("Wrong answer!")
    break 

print(f"Your take home money is {money}")