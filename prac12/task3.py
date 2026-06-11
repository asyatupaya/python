users = ['Admin', 'Guest', 'User', 'Bot']
print(users)

index = users.index('User')
users[index] = 'Moderator'
print(users)

users[-1] = 'SuperAdmin'
print(users)

users.append('Newbie')
print(users)
