from supabase import create_client

import math


url = "https://lejveivwlyrotymexzem.supabase.co"

key = "sb_publishable_Q94aJl0egnEtmAivKlEPCQ_-YRdp8hQ"

supabase = create_client(url, key)

response = supabase.table("properties").select("*").execute()

data = response.data
print(data)

def distance(lat1, lon1, lat2,lon2):
    first = math.pow((lat1-lat2),2)
    second = math.pow((lon1-lon2),2)
    return math.sqrt(first+second)

def danger(lat,lon,radius):
    count = 0
    inRadius = []
    for nums in data:
        coor = nums["geometry"]["coordinates"]
        lat2 = coor[0]
        lon2 = coor[1]
        dist = distance(lat,lon,lat2,lon2)
        if dist <= radius:
            inRadius.append(nums)
    for nums in inRadius:
        count += math.pow(10,nums["magnitude"])

    return count