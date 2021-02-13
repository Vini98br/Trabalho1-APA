def quickPartition(arr, indexArr, left, right):
  pivot = arr[right].degree
  index = left - 1

  for i in range(left, right):
    if arr[i].degree >= pivot:
      index += 1
      arr[index],arr[i] = arr[i],arr[index]
      indexArr[index],indexArr[i] = indexArr[i],indexArr[index]
  
  arr[index+1],arr[right] = arr[right],arr[index+1]
  indexArr[index+1],indexArr[right] = indexArr[right],indexArr[index+1]
  return index + 1


def quickSort(arr, indexArr, left, right):
  if left < right:
    pi = quickPartition(arr, indexArr, left, right)

    quickSort(arr, indexArr, left, pi-1)
    quickSort(arr, indexArr, pi+1, right)
  return arr
