class Group(object):
	def __init__(self, _name):
		self.name = _name
		self.users = []
		self.groups = []
	def add_user(self,user):
		self.users.append(user)
	def add_group(self,group):
		self.groups.append(group)
	def get_groups(self):
		return self.groups 
	def get_users(self):
		return self.users 
	def get_name(self):
		return self.name 


def is_user_in_group(user, group):
	if user in group.get_users():
		return True
	if len(group.get_groups()) == 0:
		return False
	for i_groups in group.get_groups():
		output = is_user_in_group(user,i_groups)
		if output:
			return True
	return False


#%% Testing official
# Testing preparation
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# Normal Cases:
print('Normal Cases:')
print(is_user_in_group(user='parent_user', group=parent))
# False
print(is_user_in_group(user='child_user', group=parent))
# False
print(is_user_in_group(user='sub_child_user', group=parent), '\n')
# True

# Edge Cases:
print('Edge Cases:')
print(is_user_in_group(user='', group=parent))
# False
print(is_user_in_group(user='', group=child))
# False