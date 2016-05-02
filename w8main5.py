sentence='sangmyung university'
d=dict()
for c in sentence:
    if c not in d:
        d[c]=1
        print d
    else:
        d[c]=d[c]+1
print d


%matplotlib inline

import matplotlib
import matplotlib.pyplot as plt

plt.bar(range(len(d)),d.values(), align='center')
plt.xticks(range(len(d)), list(d.keys()))
plt.show()

