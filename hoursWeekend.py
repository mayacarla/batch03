#Maya Carla Loleatha Anderson
#maya.anderson86@myhunter.cuny.edu
#this program prints: how many hours until the weekend from users input

hours = int(input("Enter number of hours: "))
days = hours // 24
leftovers = hours % 24

print("Days: " + str(days))
print("Hours: " + str(leftovers))
