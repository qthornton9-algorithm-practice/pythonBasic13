# def maxMinAvg(arr):
#   max = arr[0]
#   min = arr[0]
#   sum = 0
#   for i in range (len(arr)):
#     if arr[i] > max:
#       max = arr[i]
#     elif arr[i] < min:
#       min = arr[i]
#     sum += arr[i]
#   avg = sum / len(arr)
#   print(f"Maximum: {max}, Minimum: {min}, Average: {avg}")
#   return max, min, avg
# nums = maxMinAvg([1,4,-8,3])

# def swapNegForZero(arr):
#   for i in range(len(arr)):
#     if arr[i] < 0:
#       arr[i] = "Dojo"
#   print(arr)
# swapNegForZero([1,4,-8,3])

# def oddInt():
#   for int in range(256):
#     if int % 2 != 0:
#       print (int)
# oddInt()

# def printArrVal(arr):
#   for val in arr:
#     print(val)
# print(printArrVal([1,4,-8,3,"love"]))

# def printAvg(arr):
#   sum = 0
#   for num in arr:
#     sum += num
#   avg = sum / len(arr)
#   return avg
# avg = printAvg([1,4,-8,3])
# print(avg)

# def squVal(arr):
#   for i in range(len(arr)):
#     arr[i] = arr[i] * arr[i]
#   return arr
# squrd = squVal([1,4,-8,3])
# print(squrd)

# def negToZero(arr):
#   for i in range(len(arr)):
#     if arr[i] < 0:
#       arr[i] = 0
#   return arr
# arrChg = negToZero([1,4,-8,3])
# print(arrChg)

# def shiftAndLeaveZero(arr):
#   for i in range(len(arr)):
#     if arr[i] == len(arr)-1:
#       arr[i] = 0
#     else:
#       arr[i] = arr[i + 1]
#   return arr
# arrShift = shiftAndLeaveZero([1,4,-8,3])
# print(arrShift)

# def printAll():
#   for i in range(1,256):
#     print(i)
# printAll()

# def printAndSum():
#   sum = 0
#   for i in range(256):
#     sum += i
#     print(i, sum)
# printAndSum()

# def arrMax(arr):
#   max = arr[0]
#   for i in range(len(arr)):
#     if arr[i] > max:
#       max = arr[i]
#   print(max)
# arrMax([1,4,-8,3])

# def arrOdds():
#   arr = []
#   for i in range(1,256,2):
#     arr.append(i)
#   print(arr)
# arrOdds()

def moreThanY(arr,y):
  count = 0
  for i in range(len(arr)):
    if arr[i] > y:
      count += 1
  print(count)
moreThanY([1,4,-8,3],2)