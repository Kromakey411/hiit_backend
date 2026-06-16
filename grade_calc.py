coursecode =input("Enter course code: ")
score = (input("Enter score: "))

if score.isdigit():
    score = int(score)

         #70-100
    if score >= 70 and score <= 100:
        grade = "A"

#60 -69
    if score >= 60 and score < 70:
        grade = "B"

#50 - 59
    if score >= 50 and score < 60:
        grade = "C"

#45 -49
    if score >= 45 and score < 50:
        grade = "D"

#40 - 44
    if score >= 40 and score < 45:
        grade = "E"

#0 - 39
    if score >= 0 and score < 40:
        grade = "F"

    print(f"{coursecode} - {score} - {grade}")

  

else:
    print("Only numbers are required")    



