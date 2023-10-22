from defs.indeed import getIndeedData

indeed = []
for number in range(5):
  indeed.append(getIndeedData('python',number*10))

print(indeed)