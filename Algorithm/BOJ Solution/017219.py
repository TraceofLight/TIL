import sys

site_info, password_number = list(map(int, sys.stdin.readline().split()))
site_info_list = []

for info_idx in range(site_info):
    site_url, password = sys.stdin.readline().split()
    site_info_list.append([site_url, password])

site_dict = dict(site_info_list)

output = []

for password in range(password_number):
    output.append(site_dict.get(sys.stdin.readline().strip()))

print(*output, sep='\n')