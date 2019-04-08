n= int(input())

dots = n+1
underscores= n +2
dashes_top = (n * 2) + 1

print('.'*dots + '_'*dashes_top + '.'*dots)

dots = n
for row in range(0,n):
    print('.'*dots +'//'+ '_'*underscores+ '\\'+ '\\' + '.'*dots )
    dots-=1
    underscores+=2

mids = (n*2)-9
print('//'+ '_'*mids + 'STOP!'+ '_'*mids + "\\"+'\\')

underscores+=2
for row in range(0,n):
    underscores-=2
    print('.' * dots + '\\'+'\\' + '_' * underscores + '//' + '.' * dots)
    dots+=1