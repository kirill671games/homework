def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def gcd_multiple(*nums):
    result = nums[0]
    for number in nums[1:]:
        result = gcd(result, number)
    return result

result1 = gcd_multiple(3)
print(result1)
result2 = gcd_multiple(36, 48, 156, 100500)
print(result2)