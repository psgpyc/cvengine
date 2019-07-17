import fitz
import re
import nltk
from nltk.corpus import stopwords

class ParseEngine:
    global parsed_value
    parsed_value = {
        'summary': None,

        'personal details': {
            'name': None,
            'address': None,
            'email': None,
            'date of birth': 'Not Disclosed',
            'nationaity': 'Not Disclosed',
            'language': 'Not Disclosed',
            'Religion': 'No Preference',
            'Sex': 'Not Disclosed',
            'Status': 'Not Disclosed'
        },

        'education': {
            'year': None,
            'name': None,
            'field of study': None
        },
        'Experience': {

        },

        'projects': None,

        'skills': None
    }
    global remove_words

    remove_words = ['python', 'java', 'c', 'c++', 'c/c++', 'html', 'css', 'js', 'java script', 'javascript', 'jquery',
                    'C/C++', '/n', '/t', 'HTML', 'CSS', 'HTML/CSS', 'TF-IDF', 'nltk', 'JS', 'django', 'DJANGO',
                    'AWARDS']

    def extract_file(self,file):
        doc = fitz.open(file)
        text1 = ''

        ## extract all text
        for i in range(doc.pageCount):
            text = ''
            text1 += doc[i].getText("text")
            text2 = text1.replace("\n"," ")
            text = text2.replace("Functional CV Sample", " ")


            return text


    def personal_details(self,text):
        new_patter = re.compile(r'(Mr|Mr|Ms|Mrs|Dr|dr)?\.?\s*[A-Z]\w+\s[A-Z]\w+([A-Z]\w+\s|)*')
        self.name = new_patter.search(text)
        # print(self.name.group())
        parsed_value['personal details']['name'] = self.name.group()


        # print(parsed_value)

        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(text))):
            if hasattr(chunk, "label"):
                if chunk.label() == "GPE" :
                    print(chunk)
                    parsed_value['personal details']['address'] = chunk[0][0]
                    break


        self.email = re.finditer(r'[a-zA-Z]+\d*(\.|_)?[a-zA-Z]+\d*@[a-zA-Z]+\.[a-zA-Z]+', text)
        if self.email != None:
            for i in self.email:
                # print(i.group())
                parsed_value['personal details']['email'] = i.group()


        sexpattern = re.compile(r'(Fem|M)ale')
        self.sex = sexpattern.search(text)
        if self.sex != None:
            parsed_value['personal details']['Sex'] = self.sex.group()


        phone = re.compile(r'(\(\d{2,4}\)\s)?(\d{5,11}|\d{2,3}-\d{3,9})')
        self.phone = phone.search(text)
        if self.phone != 0:

                print(i.group())
                parsed_value['personal details']['Phone'] = self.phone.group()


        status = re.compile(r'(Unm|M)arried')
        self.status = status.search(text)
        if self.status != None:
            parsed_value['personal details']['Status'] = self.status.group()



        religion = re.compile(r'(H|h)indu|(B|b)uddhits|(M|m)uslim|(C|c)hristia(n|nity)')
        self.religion = religion.search(text)
        if self.religion != None:
            parsed_value['personal details']['Religion'] = self.religion.group()



        language = re.compile(r'(E|e)nglish')
        self.language = language.search(text)
        print(self.language)

        if self.language != None:
            parsed_value['personal details']['language'] = self.language.group()






        print(parsed_value)

    def cv_toke(self,text):
        toke = nltk.word_tokenize(text)
        s_toke = nltk.sent_tokenize(text)

        stop_words = stopwords.words('english')

        punctuations = ['(', ')', ';', ':', '[', ']', ',', '|', '-', '.', '/', '@']

        keywords = [word for word in toke if not word in stop_words and not word in punctuations]
        # print(keywords)
        # return keywords







        freq = nltk.FreqDist(keywords)
        for i in freq.most_common():
            if i[1] == 1 and i[0] not in remove_words and i[0].isdigit() == False:
                print(i[0])


PE = ParseEngine()
haha=PE.extract_file('pujan.pdf')
PE.personal_details(haha)
# print(PE.parsed_value)
# print(haha)
# PE.cv_toke(haha)







