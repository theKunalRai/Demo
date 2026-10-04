nums = [100, 200, 300, 400, 500]
grtr_300 = []
for i, num in enumerate(nums):
    print(i, num)
    if num >= 300:
        grtr_300.append(num)
        print("Found numbers greater than 300: ", grtr_300)
        break
