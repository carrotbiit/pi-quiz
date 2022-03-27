from datetime import datetime

#checking if teacher

password = "ryanisthebest"
teacher = input("are you a teacher? (yes/no)\n")
if teacher == "yes":
  try_password = input("what is the password?\n")
  if try_password.lower() == password:
    while True:
      #teacher actions
      action = input("teacher actions:\nc - clear all pi day data\ns - view scores\ni - view inputs\ne - exit\nplease input an action\n")
      if action.lower() == "c":
        inputs = open("inputs.txt", "r+")
        inputs.truncate(0)
        inputs.close()
        scores = open("scores.txt", "r+")
        scores.truncate(0)
        scores.close()
        print("all data erased")
      if action.lower() == "s":
        scores = open("scores.txt", "r")
        contents = scores.read()
        print(contents)
      if action.lower() == "i":
        inputs = open("inputs.txt", "r")
        contents = inputs.read()
        print(contents)
      if action.lower() == "e":
        print("exiting program")
        break
#student input

else:
  while True:
    name = input("your full name:\n")
    classroom = input("your class:\n")
    confirm = input("confirm data: \n are you sure this data is clear, correct, and you would like to proceed? (yes / no)\n")
    if confirm.lower() == "yes":
      break
  print("how to use:\n- type digits of pi AFTER the decimal point\n- only type numbers, or else the results will not be accurate\n- when you have typed all your digits of pi press ENTER")
  while True:
    pi = input("pi = 3.")
    pi_list = []
    pi_list_correct = []
    for i in pi:
      pi_list.append(i)
    
    #checking student input for errors
    with open("pi.txt") as file:
      for i in range(len(pi_list)):
        char = file.read(1)
        pi_list_correct.append(char)
    
    
    
    error = False
    count = 0
    for i in range(len(pi_list)):
      if pi_list[i] == pi_list_correct[i] and error == False:
        count += 1
      else:
        error = True
    proceed = input("confirm input:\nare you sure this is your final answer? (yes/no)")
    if proceed.lower() == "yes":
      break
    else:
      print("requizing...")
  
  print("thank you for your submission")

  #adding student data to database
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  data = "time of input: "+current_time+" name: "+ name+ ", class: "+ classroom+ ", digits memorized: "+ str(count)+ "\n"
  statsdump = "time of input: "+current_time+" name: "+ name+ ", class: "+ classroom+ ", input: "+ pi+ "\n"
  
  
  stats = open("scores.txt", "a")
  stats.write(data)
  stats.close()
  inputs = open("inputs.txt", "a")
  inputs.write(statsdump)
  inputs.close()
