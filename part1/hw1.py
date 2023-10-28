from random import randint
N, M = int(input()),int(input())
n_list, m_list = [],[]
for i in range(N):
    n_list.append(randint(1,100))
for i in range(M):
    m_list.append(randint(1,100))
n_set, m_set = set(n_list),set(m_list)
print(len(n_set.intersection(m_set)))
