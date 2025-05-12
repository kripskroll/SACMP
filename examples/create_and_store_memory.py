from src.secure_embedder import SecureEmbedder
from src.store import MemoryStore

embedder = SecureEmbedder(private_key_path="agent_keys/agent_private_key.pem")
store = MemoryStore()

text = "User successfully authenticated."
entry = embedder.embed_and_sign(text)
store.store(entry)

print("Memory stored:", entry.id)
