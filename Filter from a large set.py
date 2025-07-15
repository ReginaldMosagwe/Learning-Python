min_rent = 5000
max_rent = 8000
amenities = ["balcony", "parking", "gym"]

properties = [{"name": "Property A", "rent": 4500, "amenities": ["balcony"]}, {"name": "Property B", "rent": 6000, "amenities": ["balcony", "parking"]}, {"name": "Property C", "rent": 8500, "amenities": ["gym"]}, {"name": "Property D", "rent": 7500, "amenities": ["balcony", "gym"]}]

perfect_matches = [p for p in properties if min_rent <= p["rent"] <= max_rent]
if perfect_matches:
    print("Perfect matches found:")
    for match in perfect_matches:
        print(f"{match['name'], match['rent']}")
    else:
        print("No perfect matches found within the specified range.")
        
perfectmatches = [p for p in properties if min_rent <= p["rent"] < max_rent & p["amenities"] >= "balcony"] #
if perfectmatches:
    print("Perfect matches with amenities found:")
    for match in perfectmatches:
        print(f"{match['name'], match['rent']}") # Shows the client the name and rent of each property matching their search criteria
    else:
        print("No perfect matches with amenities found within the specified range.")

count = len(perfectmatches) # Show the client this is the number of results returning from their search


#Once the property is off the market, it should be removed from the list  of properties
taken_property = "Property B" # Example of a property that has been taken
taken_property_index = properties.index(taken_property) if taken_property in properties else None
if taken_property_index is not None:
    properties.pop(taken_property_index)

# Comparing closeness to initial location
# here n is the various locations of properties. 
current_location = "MXXH+VX Nairobi"  # Set this to the desired initial location according to Google Maps

def myfunc(n):
    return abs(n - current_location) #Set for more in depth coding

perfectmatches.sort(key = myfunc) # Sort the perfect matches based on their closeness to the initial location
print("Sorted perfect matches based on closeness to initial location:")
for match in perfectmatches:
    print(f"{match['name'], match['rent']}")  # Shows the client the name and rent of each property sorted by closeness


