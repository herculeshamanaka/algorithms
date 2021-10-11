class BinarySearch():
  
  def searchInteractive(self, list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
      mid = (low + high) // 2
      guess = list[mid]
      if guess == item:
        return mid
      
      if guess > item:
        high = mid - 2
      else:
        low = mid + 1
    
    return None
  
  def searchRecursive(self, list, low, high, item):
    if high >= low:
      mid = (high + low) // 2
      guess = list[mid]
      if guess == item:
        return mid
      elif guess >= item:
        return self.searchRecursive(list, low, mid - 1, item)
      else:
        return self.searchRecursive(list, mid + 1, high, item)
    else:
      return None
  
if __name__ == "__main__":
  bs = BinarySearch()
  orderedList = [1, 3, 5, 7, 9, 11]
  print(bs.searchInteractive(orderedList, 3))
  print(bs.searchInteractive(orderedList, 13))