import sys
from enum import Enum
from FamilyTree import FamilyTree
from Member import Member

class RelationShips(Enum):
	PATERNALUNCLE='Paternal-Uncle'
	MATERNALUNCLE='Maternal-Uncle'
	PATERNALAUNT='Paternal-Aunt'
	MATERNALAUNT='Maternal-Aunt'
	SISTERINLAW='Sister-In-Law'
	BROTHERINLAW='Brother-In-Law'
	SON='Son'
	DAUGHTER='Daughter'
	SIBLINGS='Siblings'


class Operations(Enum):
	ADDCHILD='ADD_CHILD'
	GETRELATIONSHIP='GET_RELATIONSHIP'


class Notes(Enum):
	NONE='NONE'
	PERSONNOTFOUND='PERSON_NOT_FOUND'
	CHILDADDITIONSUCCEEDED='CHILD_ADDITION_SUCCEEDED'
	CHILDADDITIONFAILED='CHILD_ADDITION_FAILED'


class Family:
	def __init__(self, family):
		self.family = family
		self.log = []

	def isEmpty(self, line_items):
		return True if len(line_items) == 0 else False

	def member_in_family(self, name) -> bool:
		if name is not None and name in self.family:
			return True

		return False

	def add_child(self, parent, child, gender):
		if self.member_in_family(parent):
			parent_in_family = self.family[parent]
			# Add child to family with parent information
			self.family[child] = Member(child, gender, {
				'Husband': None,
				'Wife': None,
				'Children': []
			})
			if parent_in_family.gender == 'Female':
				self.family[child].relationship['Mother'] = parent_in_family.name
				self.family[child].relationship['Father'] = parent_in_family.relationship['Husband']
			elif parent_in_family.gender == 'Male':
				self.family[child].relationship['Father'] = parent_in_family.name
				self.family[child].relationship['Mother'] = parent_in_family.relationship['Wife']

			# Add children to the list
			self.family[parent].relationship['Children'].append(child)
			self.log.append(Notes.CHILDADDITIONSUCCEEDED.value)
		else:
			self.log.append(Notes.CHILDADDITIONFAILED.value)
			self.log.append(Notes.PERSONNOTFOUND.value)

	def find_siblings(self, name):
		mother = self.family[name].relationship['Mother']
		father = self.family[name].relationship['Father']
		parent = mother if mother is not None else father

		if self.member_in_family(parent):
			return [child for child in self.family[parent].relationship['Children'] if child != name]
		return []

	def find_paternal(self, name, AUNT=True):
		parent = self.family[name].relationship['Father']
		siblings_of_parent = self.find_siblings(parent)
		gender = 'Female' if AUNT else 'Male'
		return [sibling for sibling in siblings_of_parent if self.family[sibling].gender == gender]

	def find_maternal(self, name, AUNT=True):
		parent = self.family[name].relationship['Mother']
		siblings_of_parent = self.find_siblings(parent)
		gender = 'Female' if AUNT else 'Male'
		return [sibling for sibling in siblings_of_parent if self.family[sibling].gender == gender]

	def find_in_laws(self, name, SISTERINLAW=True):
		member = self.family[name]
		if member.gender == 'Female':
			return self.find_maternal(name, True) if SISTERINLAW else self.find_maternal(name, False)
		if member.gender == 'Male':
			return self.find_paternal(name, True) if SISTERINLAW else self.find_paternal(name, False)
		
		return []

	def find_related(self, name, relationship) -> None:
		if self.member_in_family(name):
			members_related = []
			
			# Find the person and her/his relatives
			if relationship == RelationShips.DAUGHTER.value:
				children = self.family[name].relationship['Children']
				members_related = [child for child in children if self.family[child].gender == 'Female']

			elif relationship == RelationShips.SON.value:
				children = self.family[name].relationship['Children']
				members_related = [child for child in children if self.family[child].gender == 'Male']
			
			elif relationship == RelationShips.SIBLINGS.value:
				members_related = self.find_siblings(name)
			
			elif relationship == RelationShips.PATERNALAUNT.value:
				members_related = self.find_paternal(name, AUNT=True)
			elif relationship == RelationShips.PATERNALUNCLE.value:
				members_related = self.find_paternal(name, AUNT=False)
			
			elif relationship == RelationShips.MATERNALAUNT.value:
				members_related = self.find_maternal(name, AUNT=True)
			elif relationship == RelationShips.MATERNALUNCLE.value:
				members_related = self.find_maternal(name, AUNT=False)
			
			elif relationship == RelationShips.SISTERINLAW.value:
				members_related = self.find_in_laws(name, SISTERINLAW=True)
			elif relationship == RelationShips.BROTHERINLAW.value:
				members_related = self.find_in_laws(name, SISTERINLAW=False)
			else:
				members_related = []	
			#######################################
			
			if self.isEmpty(members_related):
				self.log.append(Notes.NONE.value)
			else:
				self.log.append(' '.join(members_related))
		else:
			self.log.append(Notes.PERSONNOTFOUND.value)

def Execute(commands, tree):
	family = Family(tree)
	for command in commands:
		operation = command.split(' ')[0]
		if operation == Operations.ADDCHILD.value:
			_, parent, child, gender = command.split(' ')
			family.add_child(parent, child, gender)
		elif operation == Operations.GETRELATIONSHIP.value:
			_, name, relationship = command.split(' ')
			family.find_related(name, relationship)
		else:
			family.logs.append(Notes.NONE.value)
	
	[print(log) for log in family.log]


if __name__ == '__main__':
	# Build family tree
	family_tree = FamilyTree()
	family_tree.build()

	# Commands from the requirements.txt
	input_commands = []
	with open(sys.argv[1], "r") as fh:
		for line in fh:
			input_commands.append(line.rstrip())

	#print(input_commands)
	# Execute Commands and print logs
	Execute(input_commands, family_tree.family)
