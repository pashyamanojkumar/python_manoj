# union(): Returns the union of set 'a' and the set elements in iterable with set 'b'
a=[1,2,3,8,9]
b=[3,4,5,6,7]
print(set(a),set(b))
print(set(a).union(set(b)))

# intersection(): Returns the insection of set 'a' and the set elements in iterable
print(set(a).intersection(b))

# difference()
print(set(a).difference(b))

# update()
s = set([1,2,3,4,5])
s.update(set([5,6,7,8]))
print(s)

# add()
s1 = set([1,2,3,4,5])
s1.add(8)
print(s1)

# remove() and discard()
s2 = set([1,2,3,4,5,6])
#s2.remove(6)
s2.discard(8)
print(s2)

# pop()
s3 = set([1,2,3,4,5])
print(s3.pop())
print(s3)

#issubset()
s4 = set([1,2,3,4,5])
s5 = set([1,2,3,4,5,6,7,8])
print(s4.issubset(s5))
print("")

S = set([2,9,7,1])
print(S.issubset(S))
print(set([2,9,7,1]).issubset(set([1,7])))
print(set([2,9,7,1]).issubset(set([1,2,3,4])))
print(set([2,9,7,1]).issubset(set([1,2,3,4,5,6,7,8,9])))
print("")

# issuperset()
S1 = set([2,9,7,1])
print(S1.issuperset(S1))
print(S1.issuperset(set([1,7])))
print(S1.issuperset(set([1,2,3,4])))
print(S1.issuperset(set([1,2,3,4,5,6,7,8,9])))
print(S1.issuperset(set([1,2,7,9])))
