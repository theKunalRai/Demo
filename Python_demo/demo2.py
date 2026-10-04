nums = [100, 200, 300, 400, 500]
grtr_300 = []
for i, num in enumerate(nums):
    print(f"{i}: {num}")
print("\n")

grtr_300 = [n for n in nums if n >= 300]
print(grtr_300)
    # if num >= 300:
    #     grtr_300.append(num)
    #     print("Found numbers greater than 300: ", grtr_300)
    #     break
