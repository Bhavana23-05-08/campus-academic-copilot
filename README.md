# Campus Academic Co-Pilot for Alexa+ (MCP Server)

An Agentic AI assistant built using the **Model Context Protocol (MCP)** for **Amazon Alexa+** to help college students stay organized, track academic deadlines, and conduct interactive exam revisions.

Built for the **Amazon Developer Hackathon 2026: Build, Ship, Shape** (*Alexa+ Track*).

---

## 🌟 Overview
College students often struggle to juggle lectures across multiple classrooms, upcoming project deadlines, and internal test revisions. 

Traditional voice assistants rely on rigid pre-programmed intents. **Campus Academic Co-Pilot** leverages **Alexa+ Agent Skills** and **MCP** to enable autonomous tool use. When a student talks to Alexa naturally, the underlying agent dynamically inspects their academic schedule, retrieves deadlines, and pulls practice questions via custom MCP tools.

---

## 🛠️ Tech Stack & Architecture
* **Protocol:** Model Context Protocol (MCP)
* **Framework:** Python FastMCP / MCP SDK
* **Integration:** Alexa+ Agent Skills / Simulated LLM Runtime
* **Deployment Target:** AWS Lambda / Bedrock AgentCore

### Architecture Flow: