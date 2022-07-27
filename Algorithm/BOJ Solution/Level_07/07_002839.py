input = int(input())
package_5 = input // 5
left_sugar = input - package_5 * 5
package_3 = left_sugar // 3
output = 0
while left_sugar % 3 != 0 :
    package_5 = package_5 - 1
    left_sugar = left_sugar + 5
    package_3 = left_sugar // 3
output = package_3 + package_5
if package_5 < 0 :
    output = -1
print(output)