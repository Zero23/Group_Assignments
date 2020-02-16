d1=[3,2,3,2,3,3,3,4]
d2=[3,3,3,2,3,2,3,4]
d3=[3,3,4,3,3,3,3,4]
design=[0.0357,0.1071,0.1785,0.2143,0.0714,0,0.25,0.1429]

score1=sum([i*j for (i, j) in zip(d1, design)])
score2=sum([i*j for (i, j) in zip(d2, design)])
score3=sum([i*j for (i, j) in zip(d3, design)])
print(score1,score2,score3)