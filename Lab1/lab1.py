import math

food = "pizza"
print(food)

is_adult = False
is_child = True

if is_adult:
    print(is_adult)
elif is_child:
    print(is_child)


is_snowing = False
is_raining = False


print("is_snowing:", not is_snowing)
print("is_raining:", not is_raining)

x=0.042
y=3.03

result = 13 * (x ** 4) * math.log((y + x)) + math.tan(math.sqrt(y)) * x
print(result)

