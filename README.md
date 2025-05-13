# SACMP

**Secure Agent-Centric Memory Protocol**  
Cryptographically signed memory vectors for AI agents that demand trust, privacy, and control.

---

## 🧠 Summary

SACMP introduces a new layer of **trust and integrity** into memory-based AI systems.

> 🧩 **Traditional assumption**: If you can access the database, you can trust the memory.  
> 🔐 **SACMP’s principle**: _Trust only what your agent actually signed._

With SACMP, every memory object (e.g., vector embedding) is:
- Cryptographically **signed** by the originating agent
- Verifiable by any recipient with the **public key**
- Inert if tampered with or accessed without authorization

---

## 🚀 Why SACMP Matters

SACMP ties vector memories to a **specific agent identity**, ensuring cryptographic integrity throughout memory usage and sharing.

### ✅ Key Advantages

- **Memory Authentication**  
  Every memory entry is signed using the agent's private key. Authenticity can be verified with the public key — no more memory spoofing.

- **Data Leak Protection**  
  Even if the vector DB (e.g., FAISS, Chroma) is leaked, entries are **unusable** unless verified and optionally decrypted.

- **Agent Sovereignty**  
  Memory is watermarked at the cryptographic level. Unauthorized agents — even from the same team — can’t reuse it.

- **Inter-Agent Trust**  
  Enables **controlled sharing**: entries can be re-signed or encrypted for other agents. Supports decentralized AI ecosystems.

- **LLM-Agnostic by Design**  
  SACMP works independently of the LLM vendor — OpenAI, Claude, Ollama, or local models.

- **Defense Against Model Surveillance**  
  While SACMP can't stop cloud providers from logging inputs, it ensures long-term memory is **owned** and **verifiable** by your agent alone.

---

## 📄 Learn More

- 📘 **Full Specification**: [docs/spec.md](docs/spec.md)
- 🧪 **Examples**: [examples/](examples/)
- 🔐 **Key Management**: [agent_keys/](agent_keys/)
- ⚙️ **Implementation**: [src/](src/)

---

## 💡 Use Cases

- AI agents with **long-term memory**
- Privacy-focused **LLM wrappers**
- Zero-trust **collaborative agents**
- Secure **multi-agent environments**

---

## 🛠️ Installation

```bash
git clone https://github.com/yourname/sacmp.git
cd sacmp
pip install -r requirements.txt
```

---

## 🧪 Quickstart

```bash
python examples/create_and_store_memory.py
python examples/retrieve_and_verify.py
```

---
