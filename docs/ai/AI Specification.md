# AI Specification

## PrimeHomes Realty — Real Estate Lead Bot

**Document:** AI Specification  
**Version:** 1.0  
**Status:** Draft  
**AI Role:** Natural Language Understanding, Extraction, Classification, Response Generation  
**Orchestration:** n8n  
**Backend:** FastAPI / Python  
**Database:** PostgreSQL  
**Frontend:** React

---

# 1. Purpose

This document defines how Artificial Intelligence is used within the PrimeHomes Realty Real Estate Lead Bot.

The AI layer is responsible for understanding customer messages and converting unstructured conversations into useful structured information.

The AI may also generate customer-facing responses, conversation summaries, and clarification questions.

The AI is **not** responsible for:

- Authentication.
- Authorization.
- Database integrity.
- Final business rules.
- Financial transactions.
- Property availability verification.
- Lead ownership.
- User permissions.
- Direct database writes.

The AI provides intelligence; the application provides control.

---

# 2. AI Architecture

The AI layer fits into the system as follows:

```text
Customer
   ↓
React
   ↓
FastAPI
   ↓
n8n
   ↓
AI Layer
   ├── Intent Classification
   ├── Information Extraction
   ├── Qualification Support
   ├── Response Generation
   └── Conversation Summary
   ↓
FastAPI
   ↓
PostgreSQL
```

---

# 3. AI Responsibility Boundary

## AI should answer:

```text
What does the customer want?

What information did the customer provide?

What information is missing?

How confident are we?

What would be an appropriate response?

Does the customer appear to be asking for human assistance?
```

## Application should answer:

```text
Is this user authenticated?

Is this action allowed?

Is the lead valid?

Can this lead change status?

What is the official lead score?

Who owns the lead?

Is a property actually available?

What data should be persisted?

What notification should be sent?
```

---

# 4. Golden Rule

> **Never allow the AI model to become the source of truth for business-critical data.**

AI output must pass through deterministic validation and application rules before being persisted or acted upon.

---

*Full original content restored from git history. See the complete AI Specification in the repository for all remaining sections (Intent Taxonomy, Extraction Schema, Confidence Rules, Response Generation, Human Handoff, Prompt Architecture, Observability, and more).*
