a = input("You want to Code or Decode? (C/D) : ")
if(a.lower() == "c"):
  
  z = input("Enter the message to Code : ")
  if(len(z) >= 3):
    random1 = "bfj"
    random2 = "dhf"
    z = z[1:] + z[0]
    secret = (random1) + z + (random2)
    print(f"Your secret message is {secret}")
  else:
    z = z[::-1]
    print(z)
    
elif a.lower() == "d":
    z = input("Enter the message to Decode : ")
    if(len(z) >= 3):
      secret = z[-4] + z[3:-4]
      print(f"Your secret message was {secret}")
    else:
      z = z[::-1]
      print(f"Your secret message was {z}")
else:
  print("Invalid Input")
  exit()