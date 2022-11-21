def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, int):
        return None

    total_students = 0

    for entrance, exit in permanence_period:
        if not isinstance(entrance, int) or not isinstance(exit, int):
            return None
        elif entrance <= target_time <= exit:
            total_students += 1

    return total_students
