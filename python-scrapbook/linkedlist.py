class Element():
	def __init__(self,value):
		self.value = value
		self.next = None	

class LinkedList():
	def __init__(self,head=None):
		self.head = head

	def append(self,new_element):
		if self.head:
			counter_element = self.head
			while counter_element.next:
				counter_element = counter_element.next
			counter_element.next = 	new_element

		else:
			self.head = new_element	

	def get_element(self,position):
		"""Get an element from a particular position. 
		Assume the first position is "1".
		Return "None" if position is not in the list.

		position = int. Positive integers only. 
		"""
		counter_position = 1
		counter_element = self.head
		while counter_position != position and counter_element.next:
			counter_element = counter_element.next
			counter_position += 1

		if counter_position == position:
			return counter_element
		else:	 	
			return None

	def delete(self,rm_value):
		#Delete the first element found with a given value.
		counter_element = self.head
		prev_element = None
		
		while counter_element.value != rm_value and counter_element.next:
			prev_element = counter_element
			counter_element = counter_element.next

		if 	counter_element.value == rm_value:
			if prev_element:
				# Checks for middle and last element
				prev_element.next = counter_element.next
			else:
				# Checks for the first element
				self.head = counter_element.next
		
		return("Element {} not found".format(rm_value))	






