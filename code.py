<<<<<<< HEAD
def are_valid_groups(StudentNumList, GroupList):
    result = True
    for i in StudentNumList:
        for Group in GroupList:
            if i not in Group:
                result = False
    return result
=======
def are_valid_groups(studentnumber, groups):
    List = []
    for x in groups:
       for y in x:
          if y in List:
            return false
          else:
            List.append(y)
    if studentnumber == List:
      return true
>>>>>>> 814bc26abe91b50769b995f537bd5f25c7fd204e
