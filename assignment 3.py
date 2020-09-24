#question 1
photo = {
  "id": 1,
  "description": "A photo of the Old Port of Marseille",
  "loc": [5.3772133, 43.302424]}
print(photo)

#question 2
photo["user"] = "bob"
print(photo)

#question 3
# the_keys = photo
print("description" in photo)
print(photo)

the_get = photo.get("loc")
print(the_get)

#question 4
del photo["user"]
print(photo)

photo["loc"] = [5.3692712, 43.2949627] 
print(photo)
