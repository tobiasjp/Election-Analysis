counties = ['Arapahoe', 'Denver', 'Jefferson']
# print(counties)
# if counties[0] == "Denver":
#     print(counties[1])
# else:
#     print("better luck next time fool")

# average_temp = int(input("What is the temperature outside?"))

# if average_temp >= 90:
#     print ("Scorching")
# elif average_temp >=80:
#     print("Burning up")
# elif average_temp >= 70:
#     print("Nice weather")
# elif average_temp >= 60:
#     print("It's getting colder")
# else:
#     print ("it's fucking freezing")
# if "El paso" in counties:
#     print("El paso is in the list of counties")
# else:
#     print("El Paso is not in the list of counties")

for county in counties:
    print(county)
counties2 = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#for names in counties2.keys():
    #print(names)
#for voters in counties2.values():
    #print(voters)

# for names, voters in counties2.items():
#      print(names, voters)

for names, voters in counties2.items():
    print(f"{names} county has {voters} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, 
                {"county":"Denver", "registered_voters": 463353}, 
                {"county":"Jefferson", "registered_voters": 432438}]   
# for county_data in voting_data:
for eachcounty in voting_data: 
        print(f"{eachcounty['county']} county has {eachcounty['registered_voters']} number of voters")

