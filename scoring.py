from model import parsed_value,uni_model
from parsedscoreing import Scoring
import re
global degrees_masters
global degrees_bach
global degrees_phd

degrees_masters = ['MSc','MSC','Msc','msc','Masters','MASTERS','MASTER','master','Master']
degrees_bach = ['Bachelor','BACHELORS','bachelors','UNDERGRADUATE','BE','be','B.E.']
degrees_phd = ['Ph.D.','Ph.D','PHD','Phd','PhD']


parsed_valuemain1 ={'objective': '\nAn enthusiastic and reliable worker with excellent knowledge of business administration. I am able to \nmeet deadlines and can work within a team or on the own initiative. I am keen to find a position within an\noffice environment which will enable me to utilise my IT skills whilst providing me with a challenge\n', 'skills': ['ms word', 'excel', 'access', 'outlook'], 'experience': [{'date':'Mar 2005 - July 2011', 'position': 'Administrative Assistant'}, {'date': 'Sept 2001 -Feb 2005', 'position': 'Assistant Sales Administrator'}, {'date': 'Oct 1996 - Sept 2000', 'position': 'Office Junior'}], 'education': [{'university': 'Hellenic University', 'date': '2010-2011', 'degree': 'MSc in Management '}, {'university': 'University of ABC', 'date': '1992-1996', 'degree': 'Bachelor in Economics '}], 'personal': {'emails': ['j.sirname@ihu.edu'], 'address': 'Moudania', 'phones': ['310-123456'], 'name': 'JHON PAPADOPOULOS '}}
parsed_valuemain = {'objective': None, 'skills': ['c++', 'vba', 'jmp', 'autocad', '3dsmax', 'photoshop', 'aftereffect'], 'personal': {'address': None, 'name': 'MARIA PAPADOPOULOS ', 'websites': None, 'emails': ['m.sirname@ihu.edu'], 'phones': ['310-123456']}, 'trainings': None, 'experience':[{'date': 'Dec 2011-present', 'position': 'Application Engineer'}, {'date': 'July 2011-Sep 2011', 'position': 'Cpu Assembly Engineer'}, {'date': 'June 2011'}, {'date': 'June 2011 '}], 'education': [{'university': 'Hellenic University', 'date': 'Sep 2010 -2011', 'degree': 'MSc in Information '}, {'university': 'Shanghai University', 'date': '2008 - 2012', 'degree': 'BE'}, {'date': 'May 2011 ', 'degree': 'Bachelor in Mechanical '}, {'degree': 'Certified Public Accounting Training (CPA) '}]}
parsed_valuemain2 = {'education': [{'degree': ' SLC ', 'grade': '81.75%', 'date': '2010 '}, {'degree': ' +2 (Science) ', 'grade': '77.70%', 'date': '2010 - 2012'}, {'degree': ' B.E. (Computer) ', 'grade': '72.33%', 'date': '2013 -2017'}],

'experience': None,

'skills': ['c/c++', 'html/css', 'javascript', 'java', 'python', 'windows', 'linux', 'android', 'jquery', 'java', 'postgresql', 'mysql', 'lat ex', 'git', 'bootstrap','software engineering', 'c++'],

'trainings': None,

'personal': {'religion': 'Hindu ', 'marital status': 'Unmarried', 'date of birth': '9th March, 1995 (Falgun 25, 2051)', 'emails': None, 'phones': None, 'name': 'Pujan Maharjan','address': None},

'objective': '\nA Computer Engineer who is responsible, determined, passionate & committed for accomplishment of the task and a fast learner with good communication skills.\n'}

score = 0


objective=parsed_valuemain['objective']
education = parsed_valuemain['education']
experience = parsed_valuemain['experience']
details = parsed_valuemain['personal']

score_education = 0
def check_education(education):

    score_uni = 0
    score_phd = 0
e
    score_field_date = 0
    score_bachelors = 0
    i = 0

    for key in education:

        for keys in (key.keys()):

            if keys == 'university':

                if (education[i][keys]) in uni_model.keys():
                    score_uni += uni_model[education[i][keys]]

            if keys == 'degree':

                type = re.compile(r'(MSc|MSC|msc|Bachelor|bachelors|Master|Masters|MASTERS|BE|B.E.|Phd|phd|PHD|Phd.|Ph.D.)')


                degree_type = type.search(education[i][keys])
                # print(degree_type)

                if degree_type != None:


                    if degree_type.group() in degrees_phd:
                        score_phd += 5


                    if degree_type.group() in degrees_masters:   #masters

                        if education[i]['grade'] != None:
                            mast_grade = float(education[i]['grade'].rstrip('%'))
                        else:
                            mast_grade = 0

                        time = Scoring.parse_date(education[i]['date'])

                        score_field_date += Scoring.parse_score(time) + Scoring.parse_grade(bach_grade)


                    if degree_type.group() in degrees_bach:   #bachelors
                        if education[i]['grade'] != None:
                            bach_grade = float(education[i]['grade'].rstrip('%'))
                        else:
                            bach_grade = 0

                        time = Scoring.parse_date(education[i]['date'])

                        score_bachelors = Scoring.parse_score(time) + Scoring.parse_grade(bach_grade)

                i += 1

    # print(score_field_date,score_bachelors,score_uni)
    educational_score = score_field_date + score_bachelors + score_uni + score_phd


    return educational_score

def score_experience(experience):
    if experience is not None:
        i = 0
        exp_score = 0
        for keys in experience:

            print(keys)
    else:
        return 0



def score_personal(details):

    personal_score = 0
    for keys in details.keys():
        if details[keys] != None:
            if keys in parsed_value['personal_main'].keys():
                personal_score += 1
            if keys in parsed_value['personal_opt'].keys():
                personal_score += 0.5


    return personal_score


final_score_education=check_education(education)
score_experience(experience)
# print("Educational Score: " + str(final_score_education))
per_score=score_personal(details)
# print("Personal Score:" + str(per_score))
# summary = check_lang(objective)
# print("summary score:" + str(summary) +"/5")
exp = score_experience(experience)
print("Experience:" + str(exp))
