n= int(input())

rows = (n-3)//2
dashes = n-2

print("*"*dashes + '\\'+ ' '+ '/'+ '*'*dashes)

for row in range(0,rows):
    print("-"*dashes + '\\'+ ' '+ '/'+ '-'*dashes)
    print("*"*dashes+ '\\'+ ' '+ '/'+ '*'*dashes)

print(' '*(n-1)+'@'+' '*(n-1))

for row in range(0,rows):
    print("*" * dashes + '/' + ' ' + '\\' + '*' * dashes)
    print("-" * dashes + '/' + ' ' + '\\' + '-' * dashes)

print("*"*dashes + '/'+ ' '+ '\\'+ '*'*dashes)