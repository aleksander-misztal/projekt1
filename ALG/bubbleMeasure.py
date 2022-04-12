import time
import csv

def bubblesort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def generateTable(size):
    l=[]
    for i in range(size):
        l.append(size-i)
    return l

results = {}
n=100
start_size=1

for i in range(1,n):
    
    a = generateTable(start_size)
    start = time.time()
    bubblesort(a)
    end = time.time()
    exec_time=end-start
    print(i,start_size,exec_time)

    results[start_size]=exec_time

    start_size+=(10*i)

print(results)


with open('measurements.csv','wb') as f:
    w = csv.writer(f)
    w.writerows(results.items())