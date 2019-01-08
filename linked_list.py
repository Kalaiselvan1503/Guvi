#LL
class LinkedList(object):
    def __init__(s, head=None):
        s.head = head
    def insert(s, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        s.head = new_node
    def delete(s, data):
        current = s.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
