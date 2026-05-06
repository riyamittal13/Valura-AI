🧠 VALURA AI — AI CO-INVESTOR MICROSERVICE

### 📌 OVERVIEW

This project is an AI microservice that acts as a co-investor assistant for users.
It classifies financial queries, routes them to specialized agents, and streams structured responses in real time.

The system is designed around four core investor needs:

-> Build → Help users start investing
-> Monitor → Track portfolio health
-> Grow → Suggest improvements & strategies
-> Protect → Identify risk & unsafe behavior

---

### 🏗️ SYSTEM ARCHITECTURE 

🔄 Request Flow

User Query
   ↓
Safety Guard (pre-LLM filter)
   ↓
Intent Classifier (rule-based routing engine)
   ↓
Router (agent dispatcher)
   ↓
Specialist Agent Execution
   ↓
Streaming Response (SSE)

---

### ⚙️ COMPONENTS

1. 🛡️ Safety Guard

-> Runs BEFORE any LLM/classifier logic
-> Fully deterministic (no API calls)
-> Blocks harmful financial intent

Responsibilities:
-> Detect unsafe queries (fraud, manipulation, etc.)
-> Return safe refusal messages
-> Ensure system compliance

Design Choice:
✔ Fast (<10ms)
✔ No external dependency
✔ Prevents unnecessary LLM usage

2. 🧠 Intent Classifier

-> Rule-based classifier (no LLM dependency)
-> Maps user query → correct financial intent

Supported Intents:
-> portfolio_health
-> market_research
-> investment_strategy
-> financial_planning
-> risk_assessment
-> financial_calculator
-> product_recommendation
-> predictive_analysis
-> customer_support
-> general_query

Key Design Decisions:
-> Keyword + regex hybrid approach
-> Market detection handled via custom scoring function
-> Order-sensitive rule system (priority-based routing)

Edge Case Handling:
-> Unknown queries → general_query
-> Ticker detection support (AAPL, TSLA, etc.)

3. 🚦 Router (Agent Dispatcher)

-> Maps classified intent → execution agent
-> Uses registry-based design (scalable architecture)

Reason of registry-based

Instead of large if-else chains:
-> Cleaner architecture
-> Easy to extend
-> Production-ready design pattern

4. 📊 Portfolio Health Agent (Core Agent)

This is the most advanced implemented agent.

Responsibilities:
-> Portfolio concentration risk analysis
-> Sector exposure detection
-> Diversification evaluation
-> Basic performance interpretation

Outputs:
-> Human-readable risk summary
-> Actionable insights
-> Regulatory disclaimer

Design Philosophy:
✔ Simple, explainable outputs for novice investors
✔ Avoids financial jargon
✔ Focus on 1–2 key risks instead of overload

5. 📈 Market Research Agent

-> Provides structured market insights

Returns:
-> summary
-> insights
-> suggestions
-> disclaimer 

Design Choice:
-> Deterministic output (no hallucination risk)
-> Stable formatting for evaluation

6. 🧩 Stub Agents

All non-core agents return structured placeholders:

-> investment_strategy
-> financial_planning
-> risk_assessment
-> predictive_analysis
-> financial_calculator
-> product_recommendation
-> customer_support

Why stubs exist:
✔ Required by assignment
✔ Ensures routing correctness
✔ Keeps architecture extensible

7. 🌐 HTTP Layer (FastAPI + SSE)

Endpoint:
GET /query?q=<user_query>

Features:
-> Server-Sent Events (streaming response)
-> Step-wise execution:
  ->safety → classification → routing → response
-> Real-time character streaming simulation

Reason of SSE
-> Low latency perception
-> Better UX for long responses
-> Aligns with “AI assistant” behavior

---

### 🔐 Safety Design Philosophy
-> Safety Guard runs FIRST (hard gate)
-> Classifier safety is informational only
-> Guard is the only enforcement layer

Key principle:
“Never allow unsafe intent to reach LLM/agents”

---

### ⚡ Performance Considerations

Metric	                    Approach
Latency	                    Lightweight rule-based system
Cost	                      No LLM dependency in classifier
Streaming	                  Character-level SSE
Scalability	                Registry-based agent system

---

### 🧪 Testing Strategy
-> Manual endpoint testing via /docs
-> Deterministic outputs for validation
-> Stub agents ensure full routing coverage
-> Handles edge cases:
  -> empty portfolio
  -> unknown queries
  -> follow-up queries

---

### 🧠 Key Design Tradeoffs

1. Rule-based vs LLM classifier

✔ Chose rule-based for:

-> predictability
-> low cost
-> test stability

2. Stub agents instead of full implementations

✔ Ensures:
-> routing correctness
-> scalable architecture demonstration

3. Deterministic outputs

✔ Avoids hallucination risk
✔ Improves evaluation consistency

---

### 🚀 How to Run

Install dependencies:
pip install -r requirements.txt

Setup environment:
cp .env.example .env   # (Linux/macOS)
copy .env.example .env # (Windows)

Start server:
python -m uvicorn src.main:app --reload

---

### 📡 API Usage
Example request:
GET /query?q=how is my portfolio doing?

---

📌 Required Environment Variables

OPENAI_API_KEY=your_key_here

Note: This project currently uses a rule-based classifier and does not require OpenAI API calls in the core pipeline. The key is included for future extensibility and compliance with assignment structure.

---

### 🧾 Key Takeaways

-> Built a modular AI microservice
-> Implemented multi-agent architecture
-> Designed deterministic classifier system
-> Ensured safety-first financial reasoning
-> Built streaming-ready API (SSE)
-> Created scalable agent registry system

---

### 🎥 Defence Video (To be added)

Link: https://www.loom.com/share/8f15997084c942b782e596c53675bc7f 

---

🏁 Final Note

This system is designed to be:
extensible, safe, deterministic, and production-aligned AI infrastructure for financial intelligence.
