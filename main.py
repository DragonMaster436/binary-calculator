print("Welcome to the binary calculator! \n")

while True:
  
  while True:
    try:
      num = input("\nWhat number do you want to see binary?\n \n")
      user_num = num
      num = num.replace(",", "")
      num = int(num)
  
    except:
      print("\nError: Please enter a number like '1' or '2'...\n")
  
    else:
      break
  
  print(f'\nThe binary version of {user_num} is, {num:b}.\n')

  print("Is that all you want to do, or do you want to do another number?")
  
  while True:
    try:
      answer = input("Type 'yes' or 'no': ")
      answer = answer.lower()
      answer = answer.replace(".", "")

      if answer == "yes":
        break

        print("\nThank you for using the binary calculator!")
        break

      else:
        print("\nError: Please type 'yes' or 'no'...\n")
  
      if answer == "no":
    except:
      print("Error: Please type 'yes' or 'no'...")

      
  if answer == "no":
    exit()
  