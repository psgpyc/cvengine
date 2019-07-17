import re
from nltk import word_tokenize
from nltk.corpus import stopwords
import collections


corp = {

    'DETAILS':['summary','Summary','SUMMARY','Details'],
    'PERSONAL DETAILS' :['personal details','PERSONAL DETAILS','Personal Details','Details','Personal details'],
    'EXPERIENCE': ['Working Experience','experience','personal experience','professional experience','EXPERIENCE','Related Work History','RELATED WORK HISTORY'],
    'EDUCATION':['education','Education details','Education Details','EDUCATION DETAILS','EDUCATION','Education'],
    'SKILLS':['Technical Skills','TECHNICAL SKILLS','Technical skills','SKILLS'],
    'Interest': ['Interest and Accomplishment', 'Interest and hobbies', 'Interests and hobbies'],

    'PROJECTS':['Projects accomplished','PROJECT ACCOMPLISHED','PROJECTS','Projects Accomplished'],
    'AWARDS':['awards','AWARDS AND ACHIEVMENTS','awards and achievments'],
    'WEB':['WEB','WEB LINKS','web links'],
    'Professional Development' : ['Professional Development ',"Professional development",'PROFESSIONAL DEVELOPMENT','Professional Experience']
}

Peron_details = ['Full name','Date of birth','Nationality','Languages','Religion','Sex, marital status']




remove_words = ['python','java','c','c++','c/c++','html','css','js','java script','javescript','jquery','C/C++','/n','/t','HTML','CSS','HTML/CSS','TF-IDF','nltk','JS','django','DJANGO','AWARDS','Interests']

'''

cv2 = '''Elizabeth Brown 336 N. Moudania Str, Thessaloniki, Greece 12 345 0030-6977-000000 e:e.brown@ihu.edu.gr Objective Process management opportunity that utilizes my communication and analytical skills to influence  organizational growth and bottom line profitability. Achievements Research Information and Analyze Options  Researched and purchased better heat exchanger that alleviated our heat loading problem.   Saved company four to six hours of downtime per eight-hour shift and improved product yield  at extruder.  Purchased     and refurbished used gearbox as spare.  Saved 12 days downtime and eliminated  risk involved to rebuild critical pieces of equipment.  During emergency rebuild we are down 2  days rather than 2 weeks. Manage People and Projects  Successfully led refurbishment campaign on all three extruder gearboxes.  Pro-active rebuild of  gearboxes puts downtime at two days rather than two weeks.  Reallocated resources during two-week annual shutdown so that no down time was  encountered and all projects finished on time. Extrapolate Essential Data  Proved that product quality issue was not due to equipment processing parameters.  Product  design team discovered fault in their print test methods.  Evaluated trends of real time data on AFG grinder.  Proactive identification of problem  prevented coarse particle contamination.   Utilize Subject Matter Expertise to Influence Management Decisions  Determined capital project would need to be undertaken pro-actively to avoid having to use our business resumption plan in the event of catastrophic failure.  Company will save about 1  million dollars.  Created viable process for extrusion, during new product development,  with no start-up  difficulties. Effective Communication Throughout the Organization  Implemented     safety related information to senior staff, peers and subordinatates.  Frequently requested to explain processing issues involving  extruder and batching processes.  Provide technical information to senior management as well as operational information to the  process operators and managers on the floor.

toke = word_tokenize(cv2)

punctuations = ['(',')',';',':','[',']',',','|','-','.','/','@']

stop_words = stopwords.words('english')

keywords = [word for word in toke if not word in stop_words and  not word in punctuations]

headings = []
keypair = {}

new_patter = re.compile(r'(Mr|Mr|Ms|Mrs|Dr|dr)?\.?\s*[A-Z]\w+\s[A-Z]\w+\s([A-Z]\w+\s|)*')
match = new_patter.search(cv2)
print(match)


def ignore(values):
    if values not in remove_words:
        return values






final_keys = []
for keys in corp.keys():
    for values in corp[keys]:
        if values in cv2:
            values= ignore(values)
            headings.append(values)




index = []
for i in headings:
    index.append(cv2.find(i))

def find_head_ind(headings):
    for i in headings:
        index.append(cv2.find(i))
    keypair = dict(zip(headings,index))

    return keypair

sp = find_head_ind(headings)
print(sp)



parsed_value = []
i = 0



# print(find_head_ind(headings))

while i<len(index):
    if i == len(index)-1:
        parsed_value.append(cv2[index[i]:])

    else:
        parsed_value.append(cv2[index[i]:index[i+1]])
    i+=1

final_parse = dict(zip(headings,parsed_value))
# print(final_parse)

#starting for personal details

for keys in final_parse:
    if keys == 'Personal details':



        Person_details_index = []
        for i in Peron_details:
            # print("{}:{}".format(i, cv2.find(i)))
            (Person_details_index.append(cv2.find(i)))

        # print(Person_details_index)
        parsed_personal_details = []
        i = 0
        while i < len(Person_details_index):
            if i == len(Person_details_index) - 1:

                    parsed_personal_details.append(cv2[Person_details_index[i]:458])


            else:

                    parsed_personal_details.append(cv2[Person_details_index[i]:Person_details_index[i + 1]])

            i += 1

        # print(parsed_personal_details)
        xyz = []
        personal_dict = {}
        for i in parsed_personal_details:
            xyz.append(tuple(i.split(':')))
        for i in xyz:
            personal_dict[i[0]] = i[1]

        # print(personal_dict)


        final_parse['Personal details'] = personal_dict



    # print(final_parse)

    edu_details = ['Year','Level','School/College','Grades']

    if keys == 'Education details':
        pass

    if keys == 'Projects accomplished':


        # print(tuple((final_parse[keys].split(":",1))))
        goal=tuple((final_parse[keys].split(":",1)))[1].split('\n')
        # for i in goal:
        #     print(i)
        #     print("------------------")
        #     # pass

    if keys == 'Technical skills':
       print(final_parse[keys])
       final_parse[keys] = (final_parse[keys].split(":",1))
       parsed_item = []
       parsed_item.append(final_parse[keys][0])
       final_parse[keys].pop(0)
       print(final_parse[keys])





    if keys in final_parse[keys]:
        keyss = keys+":"
        final_parse[keys]=final_parse[keys].replace(keyss,"")
        final_parse[keys]=final_parse[keys].replace('\n',"")





print(final_parse)
