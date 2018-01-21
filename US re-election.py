#The last U.S. election was investigated and it was discovered that Donald Trump had paid
#an hacker to increase his vote. The United State Electoral Committee wrote a proposal to
#Planet NEST to develop and digital electoral pool for the makeup election. The proposal
#goes thus:
#Hello Planet NEST,
#We write to your o ffice to develop a pooling system to be used for the make up election
#between Hillary Clinton and Donald Trump in 19th December, 2017. We would like you to
#express the final result in percentage (Donald Trump: 39% Hillary Clinton: 61%).
#We want this software to be ready by Monday 18th December, 2017. Our recommendation
#suggests this should not be an issue for you to tackle


candidate = { 'clinton': 0, 'trump': 0 }

end_vote = False

clintons_vote = candidate['clinton']
trumps_vote = candidate['trump']

while not end_vote:
    choice = input('Enter (c) for clinton and (t) for trump: ')

    if choice == 'c':
        clintons_vote += 1
    elif choice == 't':
        trumps_vote += 1
    else:
        end_vote = True

clinton_pct = clintons_vote * (1/100)
trump_pct = trumps_vote * (1/100)

print('clinton has ',clinton_pct,'%')
print('trump has ',trump_pct,'%')
