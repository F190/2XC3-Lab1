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