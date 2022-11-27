from operator import itemgetter

count = int(input())
users = []
for i in range(count):
    n, v = [x for x in input().split()]
    users.append({'name': n, 'value': int(v)})

newUsers = sorted(users, key=itemgetter('value'), reverse=True)

for user in range(len(users)):
    print(newUsers[user]["name"], newUsers[user]["value"])


