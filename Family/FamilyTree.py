from Member import Member

class FamilyTree:
    def __init__(self):
        self.family = dict()
        
    def build(self):
        self.family['Shan'] = Member('Shan', 'Male', {
            'Father': None,
            'Mother': None,
            'Husband': None,
            'Wife': 'Anga',
            'Children': ['Chit', 'Ish', 'Vich', 'Aras', 'Satya'] 
        })
        self.family['Anga'] = Member('Anga', 'Female', {
            'Father': None,
            'Mother': None,
            'Husband': 'Shan',
            'Wife': None,
            'Children': ['Chit', 'Ish', 'Vich', 'Aras', 'Satya'] 
        })
        self.family['Chit'] = Member('Chit', 'Male', {
            'Father': 'Shan',
            'Mother': 'Anga',
            'Husband': None,
            'Wife': 'Amba',
            'Children': ['Dritha', 'Tritha', 'Vritha']
        })
        self.family['Amba'] = Member('Amba', 'Female', {
            'Father': 'Shan',
            'Mother': 'Anga',
            'Husband': 'Chit',
            'Wife': None,
            'Children': ['Dritha', 'Tritha', 'Vritha']
        })
        self.family['Ish'] = Member('Ish', 'Female', {
            'Father': 'Shan',
            'Mother': 'Anga',
            'Husband': None,
            'Wife': None,
            'Children': []
        })
        self.family['Vich'] = Member('Vich', 'Male', {
            'Father': 'Shan',
            'Mother': 'Anga',
            'Husband': None,
            'Wife': 'Lika',
            'Children': ['Vila', 'Chika']
        })
        self.family['Lika'] = Member('Lika', 'Female', {
            'Father': 'Shan',
            'Mother': 'Anga',
            'Husband': 'Vich',
            'Wife': None,
            'Children': ['Vila', 'Chika']
        })
        self.family['Aras'] = Member('Aras', 'Male', {
            'Father': 'Shan',
            'Mother': 'Anga',
            'Husband': None,
            'Wife': 'Chitra',
            'Children': ['Jnki', 'Ahit']
        })
        self.family['Chitra'] = Member('Chitra', 'Female', {
            'Father': 'Shan',
            'Mother': 'Anga',
            'Husband': 'Aras',
            'Wife': None,
            'Children': ['Jnki', 'Ahit']
        })
        self.family['Satya'] = Member('Satya', 'Female', {
            'Father': 'Shan',
            'Mother': 'Anga',
            'Husband': 'Vyan',
            'Wife': None,
            'Children': ['Satvy', 'Asva', 'Krpi', 'Vyas', 'Atya']
        })
        self.family['Vyan'] = Member('Vyan', 'Male', {
            'Father': 'Shan',
            'Mother': 'Anga',
            'Husband': None,
            'Wife': 'Satya',
            'Children': ['Asva', 'Vyas', 'Atya']
        })
        self.family['Dritha'] = Member('Dritha', 'Female', {
            'Father': 'Chit',
            'Mother': 'Amba',
            'Husband': 'Jaya',
            'Wife': None,
            'Children': ['Yodhan']
        })
        self.family['Jaya'] = Member('Jaya', 'Male', {
            'Father': 'Chit',
            'Mother': 'Amba',
            'Husband': None,
            'Wife': 'Dritha',
            'Children': ['Yodhan']
        })
        self.family['Tritha'] = Member('Tritha', 'Female', {
            'Father': 'Chit',
            'Mother': 'Amba',
            'Husband': None,
            'Wife': None,
            'Children': []
        })
        self.family['Vritha'] = Member('Vritha', 'Male', {
            'Father': 'Chit',
            'Mother': 'Amba',
            'Husband': None,
            'Wife': None,
            'Children': []
        })
        self.family['Vila'] = Member('Vila', 'Female', {
            'Father': 'Vich',
            'Mother': 'Lika',
            'Husband': None,
            'Wife': None,
            'Children': []
        })
        self.family['Chika'] = Member('Chika', 'Female', {
            'Father': 'Vich',
            'Mother': 'Lika',
            'Husband': None,
            'Wife': None,
            'Children': []
        })
        self.family['Arit'] = Member('Arit', 'Male', {
            'Father': 'Aras',
            'Mother': 'Chitra',
            'Husband': None,
            'Wife': 'Jnki',
            'Children': ['Laki', 'Lavnya']
        })
        self.family['Jnki'] = Member('Jnki', 'Female', {
            'Father': 'Aras',
            'Mother': 'Chitra',
            'Husband': 'Arit',
            'Wife': None,
            'Children': ['Laki', 'Lavnya']
        })
        self.family['Ahit'] = Member('Ahit', 'Male', {
            'Father': 'Aras',
            'Mother': 'Chitra',
            'Husband': None,
            'Wife': None,
            'Children': []
        })
        self.family['Satvy'] = Member('Satvy', 'Female', {
            'Father': 'Vyan',
            'Mother': 'Satya',
            'Husband': 'Asva',
            'Wife': None,
            'Children': ['Vasa']
        })
        self.family['Asva'] = Member('Asva', 'Male', {
            'Father': 'Vyan',
            'Mother': 'Satya',
            'Husband': None,
            'Wife': 'Satvy',
            'Children': ['Vasa']
        })
        self.family['Krpi'] = Member('Krpi', 'Female', {
            'Father': 'Vyan',
            'Mother': 'Satya',
            'Husband': 'Vyas',
            'Wife': None,
            'Children': ['Kriya', 'Krithi']
        })
        self.family['Vyas'] = Member('Vyas', 'Male', {
            'Father': 'Vyan',
            'Mother': 'Satya',
            'Husband': None,
            'Wife': 'Krpi',
            'Children': ['Kriya', 'Krithi']
        })
        self.family['Atya'] = Member('Atya', 'Female', {
            'Father': 'Vyan',
            'Mother': 'Satya',
            'Husband': None,
            'Wife': None,
            'Children': []
        })
        self.family['Yodhan'] = Member('Yodhan', 'Male', {
            'Father': 'Jaya',
            'Mother': 'Dritha',
            'Husband': None,
            'Wife': None,
            'Children': []
        })
        self.family['Laki'] = Member('Laki', 'Male', {
            'Father': 'Arit',
            'Mother': 'Jnki',
            'Husband': None,
            'Wife': None,
            'Children': []
        })
        self.family['Lavnya'] = Member('Lavnya', 'Female', {
            'Father': 'Arit',
            'Mother': 'Jnki',
            'Husband': None,
            'Wife': None,
            'Children': []
        })
        self.family['Vasa'] = Member('Vasa', 'Male', {
            'Father': 'Asva',
            'Mother': 'Satvy',
            'Husband': None,
            'Wife': None,
            'Children': []
        })
        self.family['Kriya'] = Member('Kriya', 'Male', {
            'Father': 'Vyas',
            'Mother': 'Krpi',
            'Husband': None,
            'Wife': None,
            'Children': []
        })
        self.family['Krithi'] = Member('Krithi', 'Female', {
            'Father': 'Vyas',
            'Mother': 'Krpi',
            'Husband': None,
            'Wife': None,
            'Children': []
        })
