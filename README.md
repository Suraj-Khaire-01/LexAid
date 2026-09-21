# LexAid

## AI-Powered Multilingual Legal Aid Platform for Marginalized Communities

LexAid is an AI-powered multilingual legal assistance platform designed to make legal information more accessible to people who may face language, literacy, or accessibility barriers.

The platform uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from a curated legal corpus before generating responses. It supports multilingual queries, document analysis, OCR, source citations, and legal-resource referrals.

> **Disclaimer:** LexAid is designed to provide legal information and educational assistance. It is not a replacement for a qualified legal professional.

---

## 🚀 Key Features

- 🤖 **AI-Powered Legal Assistance**
  - Ask questions in natural language.
  - Receive answers grounded in retrieved legal sources.

- 🔎 **Retrieval-Augmented Generation (RAG)**
  - Searches a curated legal knowledge base.
  - Retrieves relevant Acts, sections, and clauses.
  - Uses retrieved sources as context for the LLM.

- 🌐 **Multilingual Support**
  - Allows users to interact in supported Indian languages.
  - Uses multilingual embeddings for cross-language retrieval.
  - Uses Google Cloud Translation for language conversion.

- 📄 **Legal Document Analysis**
  - Upload documents such as FIRs, notices, and contracts.
  - Extract text using OCR.
  - Ask questions about uploaded documents.

- 📚 **Source Citations**
  - Responses include relevant legal sources.
  - The system validates citations against retrieved documents.

- 🚨 **Emergency Detection**
  - Detects potentially urgent situations.
  - Provides appropriate guidance and referral information.

- ⚖️ **Legal Resource Referral**
  - Helps users identify relevant legal authorities and support resources.

- 👤 **Authentication & Session History**
  - Secure user authentication.
  - Conversation history and document sessions.

- 📊 **Analytics Dashboard**
  - Usage statistics.
  - Query and retrieval analytics.
  - System performance evaluation.

---

## 🏗️ System Architecture

```text
                         ┌─────────────────────┐
                         │       User          │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   React + Vite      │
                         │   Tailwind CSS      │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │      FastAPI        │
                         │      Backend        │
                         └──────────┬──────────┘
                                    │
                    ┌───────────────┼────────────────┐
                    │               │                │
                    ▼               ▼                ▼
              Translation         OCR          Authentication
                    │               │
                    └───────┬───────┘
                            │
                            ▼
                  ┌─────────────────────┐
                  │    RAG Pipeline     │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Multilingual        │
                  │ Embeddings          │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │       Qdrant        │
                  │    Vector Database  │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Retrieved Legal     │
                  │ Context             │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │      Gemini         │
                  │       LLM           │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Citation Validator  │
                  │ & Safety Checks     │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Translated Response │
                  └──────────┬──────────┘
                             │
                             ▼
                         ┌─────────┐
                         │  User   │
                         └─────────┘