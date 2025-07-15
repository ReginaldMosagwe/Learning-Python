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
        
perfectmatches = [p for p in properties if min_rent <= p["rent"] < max_rent & p["amenities"] == "balcony"] 