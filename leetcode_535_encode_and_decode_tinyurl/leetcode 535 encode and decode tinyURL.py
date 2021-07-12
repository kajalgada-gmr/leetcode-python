class Codec:
    
    url_db = {}
    key_db = {}
    chars = string.ascii_letters + string.digits
    
    def compute_key(self) -> str:
        key = ''
        for _ in range(6):
            key += random.choice(self.chars)
        return key

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.url_db:
            return url_db[longUrl]
        
        key_longUrl = self.compute_key()
        while key_longUrl in self.key_db:
            key_longUrl = self.compute_key()
            
        self.key_db[key_longUrl] = longUrl
        self.url_db[longUrl] = key_longUrl
        
        return key_longUrl
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        
        return self.key_db[shortUrl]
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
