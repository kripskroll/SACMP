import hashlib
from src.memory_entry import MemoryEntry
from src.signer import load_private_key, sign_message

class SecureEmbedder:
    # This class is responsible for embedding text and signing the resulting vector
    # with a private key. It uses a placeholder embedding method for demonstration.
    # In a real-world scenario, you would replace this with an actual embedding model.
    def __init__(self, private_key_path):
        self.private_key = load_private_key(private_key_path)

    def fake_embed(self, text):
        # Placeholder embedder — returns a fixed-size vector
        h = hashlib.sha256(text.encode()).digest()
        return [float(b) / 255 for b in h[:16]]

    def embed_and_sign(self, text):
        vector = self.fake_embed(text)
        message = text.encode() + b"||" + b",".join(str(v).encode() for v in vector)
        signature = sign_message(self.private_key, message)
        return MemoryEntry(text=text, vector=vector, signature=signature)