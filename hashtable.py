class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # Initialize the hash table with empty lists

    def _hash_function(self, key):
        """Hash function using modular arithmetic."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self._hash_function(key)
        bucket = self.table[index]
        
        # Check if the key already exists, and if so, update its value
        for i, kvp in enumerate(bucket):
            if kvp[0] == key:
                bucket[i] = (key, value)
                return
        
        # If key does not exist, append a new key-value pair
        bucket.append((key, value))

    def search(self, key):
        """Search for a value by key in the hash table."""
        index = self._hash_function(key)
        bucket = self.table[index]
        
        # Search for the key in the bucket
        for kvp in bucket:
            if kvp[0] == key:
                return kvp[1]
        
        # Key not found
        return None

    def delete(self, key):
        """Delete a key-value pair from the hash table."""
        index = self._hash_function(key)
        bucket = self.table[index]
        
        # Search for the key and remove it if found
        for i, kvp in enumerate(bucket):
            if kvp[0] == key:
                del bucket[i]
                return
        
        # Key not found
        return None

    def __str__(self):
        """Return a string representation of the hash table."""
        return str(self.table)

# Example usage
if __name__ == "__main__":
    ht = HashTable(size=10)
    ht.insert("name", "Alice")
    ht.insert("age", 30)
    ht.insert("city", "New York")
    
    print("Search 'name':", ht.search("name"))  # Should output: Alice
    print("Search 'city':", ht.search("city"))  # Should output: New York
    
    ht.delete("age")
    print("Search 'age' after deletion:", ht.search("age"))  # Should output: None

    print("Hash Table:", ht)
