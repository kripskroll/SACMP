import base64
import uuid

class MemoryEntry:
    def __init__(self, text, vector, signature):
        self.id = str(uuid.uuid4())
        self.text = text
        self.vector = vector
        self.signature = base64.b64encode(signature).decode()

    def to_dict(self):
        return {
            "id": self.id,
            "text": self.text,
            "vector": self.vector,
            "signature": self.signature,
        }

    @staticmethod
    def from_dict(d):
        import base64
        obj = MemoryEntry(d["text"], d["vector"], base64.b64decode(d["signature"]))
        obj.id = d["id"]
        return obj