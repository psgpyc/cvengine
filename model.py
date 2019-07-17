global parsed_value

parsed_value = {
            'objective': None,

            'personal_main': {
                'name': None,
                'address': None,
                'emails': None,
                'phones': None,
                'date of birth': 'Not Disclosed'
                         },

            'personal_opt':{

                'nationaity': 'Not Disclosed',
                'languages': 'Not Disclosed',
                'religion': 'No Preference',
                'sex': 'Not Disclosed',
                'status': 'Not Disclosed',
                'websites': None

            },


            'education': {
                'date': None,
                'grade': None,
                'degree': None,
                'university': None
            },
            'experience': {
                'date':None,
                'position': None


            },

            'training': None,

            'skills': None
        }


parsed_valuemain = {'objective': None,
                    'skills': ['c++', 'vba', 'jmp', 'autocad', '3dsmax', 'photoshop', 'aftereffect'],
                    'personal': {'address': None, 'name': 'MARIA PAPADOPOULOS ', 'websites': None, 'emails': ['m.sirname@ihu.edu'], 'phones': ['310-123456']},
                    'trainings': None,
                    'experience':[{'date': 'Dec 2011-present', 'position': 'Application Engineer'},
                                  {'date': 'July 2011-Sep 2011', 'position': 'Cpu Assembly Engineer'},
                                  {'date': 'June 2011'}, {'date': 'June 2011 '}],
                    'education': [{'university': 'Hellenic University', 'date': 'Sep 2010 -2011', 'degree': 'MSc in Information '},
                                  {'university': 'Shanghai University', 'date': '2008 - 2012', 'degree': 'BE'},
                                  {'date': 'May 2011 ', 'degree': 'Bachelor in Mechanical '},
                                  {'degree': 'Certified Public Accounting Training (CPA) '}]}

















uni_model = {

    'Hellenic University' : 3,
    'Shanghai University' : 3,
    'Kantipur Engineering College' : 4,
    'Pulcowk Engineering College' : 4,
    "Pulchowk Campus" : 4,
    'Gandaki College Of Engineering' : 4
}

experience_model = {
    'intern' : 0.5,
    'trainee' : 1,
    'junior' : 2,
    'mid': 3,
    'manager': 4,
    'senior': 5






}
