counties = ["arapahoe","denver","jefferson"]
if "arapahoe" in counties and "el paso" not in counties:
   print("Only arapahoe is in the list of counties.")
else:
    print("arapahoe is in the list of counties and el paso is not in the list of counties.")
for county in counties:
    print(county)
numbers = [0,1,2,3,4]
for num in range(5):
    print(num)
for i in range(len(counties)):
    print(counties[i])
counties_dict={"arapahoe":422892,"denver":463353,"jefferson":432438}
for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
    print(counties_dict[county])
for county, voters in counties_dict.items():
    print(county, voters)

for county, voters in counties_dict.items():
    print(county, "has", voters, "registered voters")
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
for county_dict in voting_data:  

     print(county_dict.values())