
# count()
pyDev=['DevOps','AWS',1991,2020,1991,'devOps']
print(pyDev.count("AWS"))
print(pyDev.count("Azure"))
print(pyDev.count("DevOps"))
print(pyDev.count(1991))

 # append()
aws=[10,20,30]
aws.append(40)
print(aws)
aws.append('Build on Cloud')
print(aws)
aws.append(['Pashya','Manoj','Reddy'])
print(aws)

 # del()
del aws[2]
print(aws)
print(list(enumerate(aws)))

 # extend()
vcs_github=['Movie','Rating','Year']
raw_data=[10,20,30,40]
print(vcs_github)
print(raw_data)
vcs_github.extend(raw_data)
print(vcs_github)
