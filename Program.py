###   Make My Trip   ###
a = input("What is Your Name:: \n")
#]print("Helllo",a)
def Taxi_cost(Airport):
  if Airport=="Domestic":
    return 1500
  elif Airport=="International":
    return 2500
  else:
    print("Sorry we Dont Have Data For:: \n",Airport)   
    return 0 
Airport= input("Which Airport are you Going:: \n")
print("Taxi cost for" ,Airport ,"is",Taxi_cost(Airport))

