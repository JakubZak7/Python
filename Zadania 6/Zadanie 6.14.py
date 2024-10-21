facebook = True
twitter = False
instagram = True

counter = 0

if facebook or twitter or instagram:
    counter += 1
    if twitter:
        counter += 1
    if instagram:
        counter += 1

if counter >= 2:
    print("You are good influencer! ")