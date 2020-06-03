class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LL:
    def __init__(self):
        #keep track of head
        self.head = None

    def __str__(self):
        r = ""
        cur = self.head

        while cur is not None:
            r += f'({cur.value})'
            if cur.next is not None:
                r += ' -> '

            cur = cur.next

        return r

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node
    
    def find(self, value):
        current = self.head #keep copy of head
        while current is not None: #traverse LL
            if current.value == value:
                return current
            current = current.next
        return None #not in the LL

    def delete(self, value):
        current = self.head
        #if I'm deleting the head
        if current.value == value:
            self.head = self.head.next
            return current
        
        #it's not the head
        #traverse LL with both pointers
        prev = current
        current = current.next
        
        while current is not None:
            if current.value == value:
                prev.next = current.next
                return current
            else:   
                prev = prev.next
                current = current.next

        return None
            
class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.head = None


    def __repr__(self):
             return f'HashTableEntry({repr(self.key)},{repr(self.value)})'


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    """
    def __init__(self, capacity):
        self.capacity = MIN_CAPACITY
        self.data = [None] * self.capacity
        self.load = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.data) # or just self.capacity

    #is overloaded / underloaded

    def get_load_factor(self):  #number of pairs / number of slots in the array (capacity)
        """
        Return the load factor for this hash table.
        """
        load_factor = self.load / len(self.data)
        return load_factor
        

    def fnv1(self, key):   # hashing function
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):   # takes the key and turns it into a slot number
        hash = 5381
        byte_array = key.encode('utf-8')

        for byte in byte_array:
        # the modulus keeps it 32-bit, python integers don't overflow
            hash = ((hash * 33) ^ byte) % 0x100000000

        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value): # key is a string
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.
        
        # get slot
        slot = self.hash_index(key)
        # store the value in that slot
        ''' self.data[slot] = value '''
        # instead of just storing the value
        # store both value and key
        self.data[slot] = HashTableEntry(key, value)
        """
        #Using LL
        #find slot for the key
        """ slot = self.hash_index(key)
        self.data[slot].insert_at_head(Node(key, value)) """

        # get slot
        slot = self.hash_index(key)
        # new entry, instantiate HashTableEntry (like a node)  
        new_entry = HashTableEntry(key, value)
        # if there's something there in that slot:
        if self.data[slot]:
            #append to the head, update pointers
            #My new entry NEXT pointer points to the "head of slot"/"first position"
            new_entry.next = self.data[slot]
            
            #In that first position put there my new entry, making it the "head" of that slot
            self.data[slot] = new_entry 
            self.load += 1
            """ #append to end
            self.data[slot].next = new_entry
            print(" NEXTT!!!", self.data[slot].next) """
             
        # if slot is empty put there my new entry
        else:
            self.data[slot] = new_entry
            self.load += 1
            

        ''' he = HashTableEntry(key, value)
        he.head = self.data[slot]
        #search LL for the key [0, 1, 2]
        if he.head:
            print("ll")
            print("HEAD", head)
            if he.head.key == key: #if it's the same key, update value
                head.value = value
                return
            #key doesn't exist but slot is occupied
            #new's next is the head 
            he.next = head
            #the old head points to the new node
            head = he
            print(head.next)
            print("NEWHEAD", head)
            print("OUT")
            return head
        else:
            self.data[slot] = he '''

        #if found, update it
        #if not found, make a new HashTableEntry
        #and add it to the list


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        self.put(key,None)
        self.load -= 1


    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        """
        # this gives me an index within a range
        slot = self.hash_index(key)
        current = self.data[slot]
        
        # walk the linked list in that slot
        while current is not None:
           
            if current.key == key:
                
                return current.value
            current = current.next
        return None

        """ slot = self.hash_index(key)
        if self.data[slot]:
            return self.data[slot].value
        return None """

        """ slot = self.hash_index(key)
        current = self.data[slot]
        print("CURRENT", current)

        if current:
            while current:
                if current == key:
                    return current.value
                current = current.next
            
            
        return None """
      

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        
        create a copy of old storage
        update the self.capacity to the new capacity
        overwrite old storage based of the new self.capacity
        for each item of the old storage insert in the new storage using the self.put method
        if it's a LL traverse it and insert with put method
    
        """ 
        """ print("DATA FIRST", self.data) """
        # Keep track of capacity and load factor
        if self.get_load_factor() >= 0.7:
            #copy of old list
            old_list = self.data
            #updating storage
            self.capacity = new_capacity
            self.data = [None] * self.capacity
            """ print("THE CAPACITY NOW IS", self.capacity)
            print("DATA HERe", self.data) """
            #iterate through range of the list
            for i in range(len(old_list)): # i 0-7
                current = old_list[i]
                
                while current:
                    print("CURRENT", current)
                    new_slot = self.hash_index(current.key)
                    print("SLOTT", new_slot)
                    print("!!!!", self.data[new_slot])
                    if self.data[new_slot] is None:
                        self.data[new_slot] = (HashTableEntry(current.key, current.value))
                        print("IFDATA HERe", self.data)
                        print("!!!!", self.data[new_slot])
                        current = current.next
                    
                    else:
                        self.data[i].next = self.data[i]
                        print("ELSEDATA HERe", self.data)


            

        else:
            print("underloaded")
        # if its overloaded, resize it
        # By changing the capacity 


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("key-0", "val-0")
    ht.put("key-1", "val-1")
    ht.put("key-2", "val-2")
    ht.put("key-3", "val-3")
    ht.put("key-4", "val-4")
    ht.put("key-5", "val-5")
    ht.put("key-6", "val-6")
    ht.put("key-7", "val-7")
    ht.put("key-8", "val-8")
    ht.put("key-9", "val-9")
    
    
    print("RESIZE", ht.resize(16))
    print("DATA", ht.data)

    """ test = ht.data[0] 

    while test:
        print("TEST", test.key)
        test = test.next  """

    ''' print("")


    

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("") '''
