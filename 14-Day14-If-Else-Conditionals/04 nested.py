name = input("Enter your name : ").upper()

current_time = time.strftime('%HH:%MM:%SS')
print("Your current time is : ", current_time)

if(('01:00:00') <= current_time < ('14:00:00') ):
    print("Good Morning", name, "☀🌄","Have a nice day!!")
   

elif(('14:00:00') <= current_time < ('16:00:00') ):
    print("Good Afternoon", name, "🌞", "Go to outside for a while and enjoy the Nature")

elif(('16:00:00') <= current_time < ('21:00:00') ):
    print("Good Evening", name, "🌇", "Try to come back home and spend some time with your Family ")

else:
    print("Good night", name, "🌆")
    print("Go to the Bed for your sweet dreams!!")
