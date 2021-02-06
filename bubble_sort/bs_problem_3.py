number = int(input())
restaurant_rating = {}
maximum = -1
while number:
    temp = input().split()
    rating = int(temp[1])
    restaurant_rating.setdefault(rating, [])
    restaurant_rating[rating].append(temp[0])
    if rating > maximum:
        maximum = rating
    number -= 1

print(sorted(restaurant_rating[maximum])[0])
