def round_scores(student_scores):
    """
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """

    return [round(el) for el in student_scores]


def count_failed_students(student_scores):
    """
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """

    return len([el for el in student_scores if el <= 40])


def above_threshold(student_scores, threshold):
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """

    return [el for el in student_scores if el >= threshold]


def letter_grades(highest):
    """
    :param highest: integer of highest exam score.
    :return: list of integer score thresholds for each F-A letter grades.
    """

    return list(el for el in range(41, highest, round((highest - 41) / 4)))


def student_ranking(student_scores, student_names):
    """
     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format ["<rank>. <student name>: <score>"].
     """

    return [f"{el[0] + 1}. {el[1][1]}: {el[1][0]}" for el in enumerate(zip(student_scores, student_names))]


def perfect_score(student_info):
    """
    :param student_info: list of [<student name>, <score>] lists
    :return: first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    for element in student_info:
        if element[1] == 100:
            return element
    return []
