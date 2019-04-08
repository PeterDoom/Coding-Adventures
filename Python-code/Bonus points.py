score= int(input())
if score <= 100:
    if score % 2 == 0:
        bonuspoints = 6
        print(bonuspoints)
        print(bonuspoints + score)
    else:
    bonuspoints = 5
    print(bonuspoints)
    print(bonuspoints + score)
elif score >= 100:
    bonuspoints= 20/100 * score
    print(bonuspoints)
    print(bonuspoints + score)
elif