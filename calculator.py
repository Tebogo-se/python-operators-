print("welcome to your calculator")

while True:
        user_input=input("enter your calculation / press 'exit' to leave the calculator: ")
        if user_input.lower() == "exit":
            print("thanks for using the calculator , goodbye")
            break
        try:
            user_calc=eval(user_input)
            print(f"{user_input}={user_calc}")
        
            print()
        except:
             print(" Error: inavlid input enter a correct  calculation ")

             
                 


        
    


