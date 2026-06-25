# Edgar Jimenez | Lab 3 | Orange

# Ticket 1 
username = "Edgar_J"
#ticket 2
print (len(username))  #6 
#ticket 3
print (username [1]) #d
#ticket 4
print (username [6]) #J

banner = "Welcome to Loop," + "@" + username + "!"
#print(banner) # Welcome to Loop @Edgar_j !
#ticket 5
print(f"Welcome to Loop, @{username}!")
#Welccome to Loop, @Edgar_J!

#username[0] = "X" # run this, it breaks on purpose
#ticket 6
print (username.upper()) #EDGAR_J

#ticket 7
feed = [
    {"caption" : "Summertime vibez"}, {"caption" : "City Explorer"}, {"caption" : "Coffee & Chisme"}
     ]
print (len(feed))
#ticket 8
feed.append("Model Behavior")
print(feed)
#ticket 9
feed.pop(0)
print(feed)


# Ticket 10

profile = { "username": "Edgar_J", "followers": 250, "verified" : "True"}
print(profile["followers"])   
#profile[0]
#KeyError: 0

profile["followers"] = "250"
profile["bio"] = "I love to read and code" 
print(profile)

print(profile.get("age"))

print(f"@{profile['username']} has {profile['followers']} followers and {len(feed)} posts. Top post: {feed[0]['caption']}")