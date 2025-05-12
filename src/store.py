import json
from pathlib import Path
from src.memory_entry import MemoryEntry

STORE_PATH = Path("memory_store.json")

class MemoryStore:
    def store(self, entry: MemoryEntry):
        STORE_PATH.write_text(json.dumps(entry.to_dict(), indent=2))

    def retrieve_latest(self) -> MemoryEntry:
        if STORE_PATH.exists():
            data = json.loads(STORE_PATH.read_text())
            return MemoryEntry.from_dict(data)
        raise FileNotFoundError("No stored memory found.")