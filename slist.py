class SList:
    class SListNode:
        def __init__ (self, value = None):
            self.value = value
            self.next = None
            self._number = 0

        def number(self):
            '''Find the index position of the current node within the list'''
            current = self
            index = 0
            while current:
                if current._number == self._number:
                    return index
                current = current.next
                index += 1
            return -1

    def __init__ (self):
        self._head = None
        self._size = 0

    def insert(self, value):
        '''Insert a new value in the list. Maintain nondecreasing ordering of elements'''
        new_node = self.SListNode(value)
        current = self._head
        if not current:
            self._head = new_node
            self._size += 1
        elif current.value is None or value <= current.value:
            new_node.next = self._head
            self._head = new_node
            self._size += 1
        else:
            while current.next and current.next.value < value:
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self._size += 1

    def find(self, value):
        '''Search for a value in the list, return it if found, None otherwise'''
        current = self._head
        while current:
            if value == current.value:
                return current
            current = current.next
        return None

    def remove(self, value):
        '''Remove the first occurence of value.'''
        current = self._head
        if not self._head:
            return False
        elif current is not None:
            if value == current.value:
                self._head = current.next
                current = None
                self._size -= 1
                return True
        while current is not None:
            if value == current.value:
                break
            prev = current
            current = current.next
        if current is None:
            return False
        prev.next = current.next
        current.next = None
        current = None
        self._size -= 1
        return True

    def remove_all(self, value):
        '''Remove all instances of value'''
        current = self._head
        prev = None
        while current is not None and current.value == value:
            self._head = current.next
            current = self._head
        while current is not None:
            while current is not None and current.value != value:
                prev = current
                current = current.next
            if current is None:
                break
            prev.next = current.next
            current = prev.next
            self._size -= 1

    def __str__(self):
        '''Convert the list to a string and return it'''
        lyst = []
        current = self._head
        while current:
            lyst.append(str(current.value))
            current = current.next
        return "["+', '.join(lyst)+"]"

    def __iter__(self):
        '''Return an iterator for the list'''
        return self.__next__()

    def __next__(self):
        '''Return the next value in the iteration'''
        current = self._head
        while current:
            yield current.value
            current = current.next

    def __len__(self):
        '''returns the size of the list'''
        return self._size

    def __getitem__(self, index):
        '''Return the item at the given index, or throw an exception if invalid index'''
        current = self._head
        if not self._head:
            return False
        else:
            for i in range(index):
                current = current.next
            return current.value
