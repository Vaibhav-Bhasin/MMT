
def flight_cost1(city):
  if city=="Mumbai":
    return 35000
  elif city=="Jaipur":
    return 24000
  elif city=="Goa":
    return 30000
  elif city=="Dibrugarh":
    return  25000
  else:
    return 0



def flight_cost2(fcity):
  if fcity=="Hong Kong,Hong Kong":
    return 35000
  elif fcity=="Singapore,Singapore":
    return 24000
  elif fcity=="Bangkok,Thailand":
    return 30000
  elif fcity=="London,UK":
    return  25000
  else:
       
    return 0

if Taxi_cost == 2500:
  fcity = input("Enter foreign city: ")
  if flight_cost2(fcity)==0:
    print("Sorry we Dont Have Data For:: \n",fcity)
  else:
    print("fight cost for ",fcity,"is",flight_cost2(fcity))
else:
  city= input("Enter Domestic city: ")
  if flight_cost1(city)==0:
    print("Sorry we Dont Have Data For:: \n",city)
  else:
    print("fight cost for",city,"is",flight_cost1(city))

