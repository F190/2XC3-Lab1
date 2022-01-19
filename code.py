def are_valid_groups(StudentNumList, GroupList):
    result = True
    for i in StudentNumList:
        for Group in GroupList:
            if i not in Group:
                result = False
    return result
