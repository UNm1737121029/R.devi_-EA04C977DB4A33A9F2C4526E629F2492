def linearsearchproduct(productlist,targetproduct):
  indices=[]

  for index,product in enumerate(productlist):
    if product == targetproduct:
     indices.append(index)

  return indices


#Example usage:
products=["shoes","boot","loafer","sandal","shoes"]
target="shoes"
target2="apple"
result = linearsearchproduct(products,target)
print(result)
l1 = ['shoes','cars','laptop']

for i,j in enumerate(l1):
  print(i,j)