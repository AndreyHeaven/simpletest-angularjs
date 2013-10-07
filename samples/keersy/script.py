import math
res = resources
p1 = [0 for x in range(14)]
for p in answers:
  i = int(int(p)%7)
  v = int(answers[p])
  idx = i*2+v
  p1[idx]=p1[idx]+1

t = max(p1[0],p1[1])*2-5
t+= max(p1[2]+p1[4],p1[3]+p1[5])-10
t+= max(p1[6]+p1[8],p1[7]+p1[9])-10
t+= max(p1[10]+p1[12],p1[11]+p1[13])-10
print res['number'] % t
r = 'E' if p1[0]>p1[1] else 'I'
r+=('S' if p1[2]+p1[4]>p1[3]+p1[5] else 'N')
r+=('T' if p1[6]+p1[8]>p1[7]+p1[9] else 'F')
r+=('J' if p1[10]+p1[12]>p1[11]+p1[13] else 'P')
print res[r]