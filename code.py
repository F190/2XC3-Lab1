def are_valid_groups(list_of_student_numbers, list_of_groups):
    for lists in list_of_groups:
        for members in lists:
            if members in list_of_student_numbers:
                list_of_student_numbers.remove(members)
            else:
                return False
    if not list_of_student_numbers:
        return True
    else:
        return False


#print(are_valid_groups([1,2,3,4],[[1],[2],[3]]))
