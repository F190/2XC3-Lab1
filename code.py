def are_valid_groups(studentnumber, groups):
    for group in groups:
        for members in group:
            if studentnumber in group:
                studentnumber.remove(members)
            else:
                return False
    if not studentnumber:
        return True
    else:
        return False

