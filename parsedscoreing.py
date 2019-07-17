import re
class Scoring:

    def parse_date(date):
        date = re.search(r'\w*\s*\d+\s?\w*[-.]*\s?\d*\s*w*\d*\w*', date).group()
        try:
            start1, end1 = (date.split("-"))
            start = re.search(r'\d+', start1).group()
            end = re.search(r'\d+', end1).group()


        except Exception:
            if Exception:
                start_list = date.split(" ")
                for j in start_list:
                    if j.isdigit() == True:
                        start = j
                end = 2018
        time = int(end) - int(start)
        return time




    def parse_grade(grade):
        grade_score =0
        if grade >= 80:
            grade_score = 1.5
        if grade > 60 and grade < 80:
            grade_score = 1.25
        if grade <= 60  and grade > 50:
            grade_score = 0.5
        if grade == 0:
            grade_score = 0
        return grade_score



    def parse_score(time):
        score_field = 0

        if time == 1:
            score_field = 4
        if time == 2:
            score_field = 3.5

        if time > 2 and time < 4:
            score_field = 1

        if time == 4:
            score_field = 3

        if time > 4 and time <= 6:
            score_field = 1.5

        if time > 6:
            score_field = 0

        return score_field







