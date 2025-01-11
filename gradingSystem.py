score = int(input("enter your score"))
name = input("What is your name ")
if score >= 70 and score <= 100:
    message = "you get an A {} and your score is{}".format(name, score)
elif score >= 60 and score < 70:
    message = "you get a B {} and your score is".format(name, score)
elif score >= 50 and score < 60:
    message = "you get a C {} and your score is {}".format(name, score) 
elif score >= 40 and score < 50:
    message = "you get a D {} and your score is {}".format(name, score)
elif score >= 30 and score < 40:
    message = "you get a D {} and your score is {}".format(name, score) 
elif score >= 20 and score < 30:
    message = "you get an F {} and your score is {}".format(name, score)
else: 
    message = "invalid score"    
#anytime u have elif in your system you must end it with else
print(message)