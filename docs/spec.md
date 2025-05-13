# SACMP Specification

**Secure Agent-Centric Memory Protocol**  
Cryptographically-bound memory vectors for trusted, sovereign, and verifiable AI memory systems.

---

## 📌 Purpose

The **Secure Agent-Centric Memory Protocol (SACMP)** defines a mechanism to protect memory objects (e.g., vector embeddings, knowledge vertices) using cryptographic identity guarantees. The protocol ensures that **only the agent holding the correct keypair** can generate, verify, and operate on memory content.

This approach reframes memory not just as data — but as **verifiable identity-linked evidence**.

---

## 🔍 Why It Matters

SACMP was designed in response to critical gaps in modern AI memory systems:

---

### 1. ✅ Memory Authentication

- Every memory entry (e.g., an embedding or structured vertex) is **cryptographically signed** by the agent's private key.
- Any consumer — including downstream agents or verifier systems — can **verify authenticity** using the agent’s public key.
- This prevents:
  - Injection of fake memories
  - Spoofed memory creation
  - Undetected tampering

> 🔒 Signed memory is trusted memory.

---

### 2. 🔐 Data Exfiltration Defense

- If the vector DB (FAISS, Chroma, Pinecone, etc.) is exfiltrated or leaked:
  - Entries cannot be verified
  - Optionally, entries can be **encrypted**, making them unreadable offline
- SACMP makes stolen memory **cryptographically inert**.

> 🧬 The memory becomes a secure artifact — useless without provenance.

---

### 3. 🧠 Sovereign Agent Identity

- SACMP enforces **agent-specific ownership** of memory.
- Even inside the same organization, agents with different keypairs:
  - Cannot reuse each other’s memories
  - Cannot impersonate or inherit memory context
- Embeddings are **watermarked at the identity layer**.

> 🎯 Memory sovereignty is enforced at the cryptographic boundary.

---

### 4. 🤝 Inter-Agent Trust

- SACMP supports controlled memory exchange:
  - Sign-for-recipient: A memory entry can be signed for another agent’s public key
  - Chain of custody can be logged and proven
- Enables **federated agents**, **multi-agent collaboration**, and **privacy-preserving cooperation**.

> 🧩 Trust scales when cryptographic evidence travels with the memory.

---

### 5. 🌐 Cloud Model Agnosticism

- SACMP operates independently of:
  - The vector DB engine (FAISS, Chroma, etc.)
  - The LLM vendor (OpenAI, Claude, Ollama, etc.)
- You can swap models or run on-prem without losing the integrity of memory.

> 🛠️ Bring your own stack — SACMP still guarantees trust.

---

### 6. 🛡️ Defense Against LLM Surveillance

- SACMP does **not** prevent the LLM provider from logging API calls.
- But it **does** ensure that what is **stored**, **reused**, or **shared** is:
  - Agent-owned
  - Cryptographically sealed
  - Impossible to spoof or hijack

> 🧱 SACMP builds long-term memory on a foundation the LLM provider cannot modify.

---

## 📂 Example Flow

1. The agent generates an embedding from raw text.
2. The embedding is **signed** using the agent’s private key.
3. The signed object is stored in the vector DB.
4. Upon retrieval:
   - The agent (or any client) **verifies the signature** using the public key.
   - Only valid signatures are used in reasoning or search.

---

## 🔐 Cryptographic Details (WIP)

SACMP uses:
- `RSA-2048` for proof-of-concept (upgradeable to ECC or post-quantum)
- `SHA-256` hash before signing
- Embeddings stored with:
  - Original text
  - Vector
  - Signature
  - Agent ID or public key fingerprint

> Future versions may define a binary format, include timestamped signing, and support certificate revocation or rotation.

---

## 📈 SACMP Memory Flow

```text
+-------------+       +--------------------+       +-------------------------+       +------------------+
|  Text Input |       | Embed + Sign with  |       |  Store in Vector DB     |       |   Verify Entry   |
|  ("User is  |  -->  |  Agent Private Key |  -->  |  (FAISS, Chroma, etc.)  |  -->  |  with Public Key |
|   happy")   |       |                    |       |                         |       |   at Retrieval   |
+-------------+       +--------------------+       +-------------------------+       +------------------+
                            |                                           
                            |                                                                              
                            v
             Signature = Sign(embedding + metadata, private_key)
```

---

## 🧭 Roadmap

Planned enhancements:
- [ ] Agent identity rotation and revocation
- [ ] Signature chaining (memory provenance)
- [ ] Encrypted memory with hybrid key exchange
- [ ] Integration with LLM memory frameworks (e.g., LangChain, AutoGen)
- [ ] Zero-knowledge proof mode for memory assertions

---

## 📚 References

- [FAISS](https://github.com/facebookresearch/faiss)
- [Chroma](https://www.trychroma.com/)
- [OpenAI Embeddings](https://platform.openai.com/docs/guides/embeddings)
- [RSA Signing — Python `cryptography`](https://cryptography.io/en/latest/)