class SimpleHashSet:
    def __init__(self):
        self.buckets = [[] for _ in range(10)]
    
    def hash_function(self, value):
       return sum(ord(char) for char in value) % 10
   
    def add(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        bucket.append(value)
        
    def contains(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        return value in bucket
    
    def remove(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value in bucket:
            bucket.remove(value)
    def print_set(self):
        for i, bucket in enumerate(self.buckets):
            print(f"index {i}: {bucket}")
        
hash_set = SimpleHashSet()
hash_set.add("Charlotte")
hash_set.add("Thomas")
hash_set.add("Jens")
hash_set.add("Peter")
hash_set.print_set()
hash_set.contains('Peter')
hash_set.remove('Peter')
hash_set.print_set()
