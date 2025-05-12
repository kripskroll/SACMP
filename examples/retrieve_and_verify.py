from src.signer import verify_signature
from src.store import MemoryStore

store = MemoryStore()
entry = store.retrieve_latest()

if verify_signature(entry):
    print("✅ Valid memory entry:", entry.text)
else:
    print("❌ Invalid or tampered memory!")
