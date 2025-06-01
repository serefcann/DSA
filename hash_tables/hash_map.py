class SimpleHashMap:  # also this consist a key value pair
    def __init__(self):
        self.buckets = [[] for _ in range(10)]
    
    def hash_function(self, key):
        # numeric sum then % 10 
        return sum(int(char) for char in key if char.isnumeric()) % 10
    
    def put(self, key, value): ## hash_sets can also change the value of buckets in addition to hash_maps
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
    
    def get(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return (k, v)
    
    def remove(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
    
    def print_map(self):
        for i, bucket in enumerate(self.buckets):
            print(f"index {i}: {bucket}")

hash_map = SimpleHashMap()    
hash_map.put("123-4567", "Charlotte")
hash_map.put("123-4568", "Thomas")
hash_map.put("123-4569", "Jens")
hash_map.put("123-4570", "Peter")
hash_map.put("123-4571", "Lisa")
hash_map.print_map()
hash_map.get('123-4567')
hash_map.put("123-4570","san")
hash_map.remove("123-4570")
hash_map.print_map()

