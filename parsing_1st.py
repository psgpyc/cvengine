import re
from nltk import word_tokenize
from nltk.corpus import stopwords
import collections

from collections import OrderedDict
import string
import nltk
my_text = 'abcdefghijklmnopqrstuvwxyz1234567890'


cv = '''Amit Garu  Bhaktapur | (977) 9866089074 |  amitgaru2@gmail.com     EXPERIENCE  Assisted PhD scholar  Mr. Phanindra Bhandari  Coded and solved the algorithm designed by Mr. Phanindra Bhandari the  PhD scholar at Mathematics Department T.U.  Website Design - Sanjeevani Foundation Nepal  Designed website for the non-profit social organization named  Sanjeevani Foundation Nepal.  MIS Data Entry - Khwopa Engineering College  Part of Data Entry team during the development of MIS of Khwopa  Engineering College.  EDUCATION  Khwopa Engineering College / BE Computer - Bhaktapur  September 2013 - 2018  Grade   3.47 (upto 7th sem).  PROJECTS  Department Store Information System / C  - 3rd sem  Developed department store information system in C programming  language with the features like Billing,  Searching, Decision Support.  Disease Recognition System / PHP - 5th sem  The system recognizes the disease based on the maximum probability  resulted from the input symptoms of the user. The project implements  Machine Learning algorithm i.e Naive Bayes Theorem.  Khec FAQ Chatbot / Python, nltk  -  Final year  Developed Frequently Asked Question Chatbot that answers related  queries about Khwopa Engineering College. The project is completely  based on Natural Language Processing with use of algorithms like Edit  Distance, Language Modeling,  TF-IDF.  SKILLS  Python, Django  HTML/CSS, JS, jQuery  C/C++  AWARDS AND ACHIEVEMENTS  Became 3rd in live C  programming competition  in  Khwopa expo ‘070 - 2070.  Exhibitor and team member  of Black line tracking robot in  Khwopa expo ‘070 - 2070.  Exhibitor and team member  at Final year project  exhibition in Khwopa  Engineering College - 2074.  WEB LINKS  http://github.com/arneec /  http://amitgaru.com.np/       
'''


cv2 = '''Pujan Maharjan sunakothi, Lalitpur, Nepal\n(+977) 984-3815209 | 070bct526@ioe.edu.np\nSummary:\nA Computer Engineer who is responsible, determined, passionate & committed for accomplishment of the  task and a fast learner with good communication skills.\nPersonal details:\n Full name: Pujan Maharjan  Date of birth: 9th March, 1995 (Falgun 25, 2051)  Nationality: Nepali  Languages: English, Nepali, Newari  Religion: Hindu  Sex, marital status: Male, Unmarried\nEducation details:\nYear   Level            School/College Grades\n2010    SLC       William Public School 81.75%\n2010 - 2012 +2 (Science)        Caribbean College 77.70%\n2013 -2017    B.E. (Computer)        Pulchowk Campus, Institute of Engineering 72.33%\nTechnical skills:\n Programming languages: C/C++, HTML/CSS, Javascript,  Java, Python.   Operating systems: Windows, Linux, Android  Databases: PostgreSQL, MySQL  Tools and frameworks: Microsoft Office, LaT ex, Git, Bootstrap, jQuery \n Sound knowledge of Object-Oriented programming and Software Engineering \nPractices\nInterests and hobbies :          Web development, Database Management, Machine Learning, Data Mining,           Game Development, Mobile App Development, T raveling, Social activities.\nProjects accomplished:\n AVIN(Automatic Vehicle Identification in Nepal)  \nAn application  that facilitates in recognizing the Nepali vehicle number plates through  their images.\nSkills used: Image processing, MATLAB , Machine Learning \n Run & Escape A user interactive single player running game based on tackling with obstacles\nSkills used: C++, SDL \nFitness Club Management System \nA Dynamic website for managing a fitness club.\nSkills used: HTML/CSS, PHP \n Interactive Voice Response System with Speech Recognition\nAn application that enables task accomplishment in accordance with voice command.\nSkills used: Speech processing, Machine Learning, Python, PyQT. \n'
Message Input'''


new_patter = re.compile(r'(Mr|Mr|Ms|Mrs|Dr|dr)?\.?\s*[A-Z]\w+\s[A-Z]\w+\s([A-Z]\w+\s|)*')

phone_pattern = re.compile(new_patter)

match = new_patter.search(cv)
print(match)
toke = word_tokenize(cv)

punctuations = ['(',')',';',':','[',']',',','|','-','.','/','@']

stop_words = stopwords.words('english')

keywords = [word for word in toke if not word in stop_words and  not word in punctuations]
freq=nltk.FreqDist(keywords)




remove_words = ['python','java','c','c++','c/c++','html','css','js','java script','javescript','jquery','C/C++','/n','/t','HTML','CSS','HTML/CSS','TF-IDF','nltk','JS','django','DJANGO','AWARDS']

# for i in freq.most_common():
#     if i[1] == 1 and i[0] not in remove_words and i[0].isdigit() == False:
#         print(i)

headings = []
keyparir = {}
for i in keywords:
    if i not in remove_words:
        if i.isupper() and len(i)>3:

            headings.append(i)
            keyparir[i] = None

index = []
for i in headings:
    index.append(cv.find(i))# print(toke)

# key_index = collections.OrderedDict(zip(headings,index))

parsed_value = []
i = 0
# print(len(index))
while i<len(index):
    if i == len(index)-1:
        # print(cv[index[i]:])
        parsed_value.append(cv[index[i]:])
        # parsed_value.append('\n')

    else:
        # print(cv[index[i]:index[i+1]])
        parsed_value.append(cv[index[i]:index[i+1]])
        # parsed_value.append('\n')
    i+=1

final_parse = dict(zip(headings,parsed_value))



for keys in final_parse.keys():
    print(final_parse[keys])


