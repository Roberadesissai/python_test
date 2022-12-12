import csv


def foo(n):
    return (n % 2 == 0 and n < 0) or (n % 3 == 0 and n > 0)


dicmat = {0: [1, 2],
          1: [0, 2, 3, 4],
          2: [0, 1],
          3: [1, 4],
          4: [1, 3]}

matx = [[0, 1, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 1, 0, 1, 0]]


def is_regular(x):
    node = len(x[0])
    print(node)
    for values in range(len(x)):
        if len(x[values]) != node:
            return False
    return True


def is_prime(x):
    prime = []
    for values in range(1, x+1):
        if x % values == 0:
            prime.append(values)
    return len(prime) == 2


li = [-5, -23, 5, 0, 23, -6, 23, 67]


def sum_li(li):
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            if li[i] > li[j]:
                li[i], li[j] = li[j], li[i]

    return li[1]+li[-2]


with open("file.csv", "r") as file:
    csv_file = csv.DictReader(file)

    def oldest_pet(csv_file):
        oldest = 0
        for values in csv_file:
            if int(values['age']) > oldest:
                oldest = int(values['age'])
        return oldest
    print(oldest_pet(csv_file))


with open("file.csv", "r") as file:
    csv_file = csv.DictReader(file)

    def species(csv_file):
        count = {}
        for values in csv_file:
            if values['species'] in count:
                count[[values['species']]] += 1
            else:
                count[[values['species']]] = 1

dict={0:[1,2],1:[],2:[0,3,4],3:[2],4:[0,3]}
mat=[
  [0,1,0,0,1],
  [0,0,0,0,0],
  [1,1,0,1,0],
  [0,0,0,0,1],
  [1,0,0,0,0]
]

def star_d(n):
  di={}
  for i in range(5):
    di[i]=[0]
  for j in range(1,n):
    di[0].append(j)
  return(di)


def star_m(n):
  mat=[[0 for x in range(n)] for y in range(n)]
  for i in range(1,n):
    mat[0][i]=1
    mat[i][0]=1
  for matrix in mat:
    print(matrix)

di={0:[1,3],1:[0],2:[1,3],3:[2],4:[0]}
def transpose_m(di):
  transpose = [[di[j][i] for j in range(len(di))] for i in range(len(di[0]))]
  for row in transpose:
    print(row)

def transpose_n(di):
    result={}
    for k,v in di.items():
        for node in v:
            if node not in result:
                result[node]=[k]
            else:
                result[node].append(k)
    print(result)

def fooo(n):
    result =[]
    num = 3
    for i in range(n):
        result.append(num)
        num += 3

def anti_diag(n):
  index=-1
  mat=[[0 for i in range(n)] for i in range(n)]
  for x in mat:
    x[index]=1
    index-=1
  for m in mat:
    print(m)
  print("\n")

def small_plus(n):
  max_1=[[0 for i in range(n)] for i in range(n)]
  for num in max_1:
    mid=len(num)//2
    max_1[mid][mid]=1
    max_1[mid][mid-1]=1
    max_1[mid][mid+1]=1
    max_1[mid-1][mid]=1
    max_1[mid+1][mid]=1
  for num in max_1:
    print(num)
  print("\n")

def border(m,n):
  max_2=[[0 for i in range(n)] for i in range(m)]
  l=len(max_2[0])
  i=0
  for num in max_2:
    num[0]=1
    num[l-1]=1
    max_2[0][i-1]=1
    max_2[l][i-1]=1
    i=i+1 
  for m in max_2:
    print(m)

li=[9,1,8,2,7,3,4,6,5]
def bubble_sort(arr):
  i = 0
  n=len(arr)
  while i<n:
      j = 0
      while j<n-1:
          if arr[j+1] < arr[j]:
              arr[j], arr[j+1] = arr[j+1], arr[j]
          j += 1
      i += 1
  return arr


li=[4,5,7,2,3,6]
def swap(li):
  min = li[0]
  minPos = 0;
  firstElement = 0
  for i in range(len(li)):
    if li[i] < min:
      minPos = i
      min = li[i]
  if li[0] != min:
    firstElement = li[0]
    li.remove(li[0])
    li.remove(li[minPos-1])
    li.insert(0,min)
    li.insert(minPos,firstElement)
  return li


di = {0: [1, 2], 1: [2, 3], 2: [0, 3], 3: [0, 1]}
mat = [[0, 1, 1, 0], [0, 0, 1, 1], [1, 0, 0, 1], [1, 1, 0, 0]]
def is_regular_d(di):
  length = []
  for i in range(len(di)):
    length.append(len(di[i]))
  if len(set(length)) == 1:
    return True
  else:
    return False


def is_regular_m(mat):
  length = []
  for i in range(len(mat)):
    length.append(mat[i].count(1))
  if len(set(length)) == 1:
    return True
  else:
    return False

def path_d(n):
  lists=[]
  di={}
  for x in range(n):
    lists.append(x)
    di[x]=[]
    if lists[x] == 0:
      di[x]=[x+1]
    elif lists[x] > 0:
      di[x]=[x-1,x+1]
      if lists[x] == n-1:
        di[x]=[x-1]
        
  for y in di.items(): 
    print(y)
    
  
   
d={
  0:[1,2,4],
  1:[0,2,3,4,5],
  2:[0,1],
  3:[1,4],
  4:[0,1,3],
  5:[1]
}
mat=[[0,1,1,0,1,0],[1,0,1,1,1,1],[1,1,0,0,0,0],[0,1,0,0,1,0],[1,1,0,1,0,0],[0,1,0,0,0,0]]


def min_degree_d(d):
  degree=[]
  for v in d.values():
    degree.append(len(v))
  if degree[-1]==1:
    return degree[-1]
  else:
    return degree[-1]
  
   
def min_degree_m(mat):
  degrees=[]
  for num in mat:
    degrees.append(num[-1])
  if degrees.count(1) < 2:
     return 1
  else:
     return degrees.count(1)
  
    
dic_c5 = {0: [1, 4],
       1: [0, 2],
       2: [1, 3], 
       3: [2, 4], 
       4: [0, 3]}
m_c5=[[0,1,0,0,1],
   [1,0,1,0,0],
   [0,1,0,1,0],
   [0,0,1,0,1],
   [1,0,0,1,0]]

di={"Mike":60,"Li":92,"Joan":88,"Trevor":58,"Betsy":73}
dii={"Mike":78,"Li":92,"Joan":88,"Trevor":58,"Betsy":73}
di_r={3:5,22:10,4:42,20:6}
def grades(di):
  count=0
  for values in di.values():
    if values >= 60:
      count +=1
  return count
def grades_2(dii):
  names=[]
  for keys, values in di.items():
    if values >= 60:
      names.append(keys)
  return names
def grades_3(di):
  for k,v in list(di.items()):
    if  v <= 60:
      del di[k]
  return (di)
def reverse(di_r):
  di={v: k for k,v in di_r.items()}
  return di
    
print(grades(di))
print(grades_2(dii))
print(grades_3(dii))
print(reverse(di_r))


