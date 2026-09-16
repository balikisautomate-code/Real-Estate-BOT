# PRD — Real Estate Lead Bot

**Product:** PrimeHomes Realty — Real Estate Lead Bot  
**Document:** Product Requirements Document (PRD)  
**Version:** 1.0  
**Status:** Draft  
**Primary Stack:** React + FastAPI + n8n + SQL Database + Google Sheets  
**Product Type:** AI-powered Lead Management & Qualification System

---

## 1. Executive Summary

PrimeHomes Realty receives potential customer enquiries through digital channels. These enquiries vary significantly in structure, completeness, and intent.

For example:

> “Hi, I’m looking for a 3-bedroom apartment around Lekki. My budget is around ₦80 million.”

Another customer may simply say:

> “Hello, I want to buy a house.”

The current manual process requires sales representatives to read messages, understand customer requirements, extract relevant information, determine lead quality, respond to the customer, and follow up.

At higher message volumes, this creates several problems:

- Slow response times
- Incomplete lead information
- Missed opportunities
- Inconsistent lead qualification
- Poor follow-up
- Difficulty tracking customer progress
- Lack of centralized lead information

### Proposed Solution

The Real Estate Lead Bot will act as an AI-powered digital receptionist for PrimeHomes Realty.

The system will:

1. Receive customer messages.
2. Understand customer intent.
3. Extract structured requirements.
4. Identify missing information.
5. Continue the conversation when necessary.
6. Create and store a lead.
7. Score and classify the lead.
8. Respond appropriately to the customer.
9. Notify the sales team when required.
10. Allow sales representatives to follow up.
11. Track the lead lifecycle.
12. Maintain a record of customer interactions.

The system will use:

- **React** for the customer-facing interface.
- **FastAPI** for backend APIs and business logic.
- **n8n** for workflow orchestration and integrations.
- **AI services** for natural-language understanding.
- **SQL** as the primary structured database.
- **Google Sheets** where lightweight operational visibility or n8n-based reporting is useful.

---

## 2. Product Vision

To provide real estate companies with an intelligent digital receptionist that can automatically understand, organize, qualify, and route potential customers while keeping human sales representatives in control of the final sales process.

The system is **not intended to replace sales representatives**.

Instead:

> **AI handles repetitive qualification and organization.**
>
> **Sales representatives handle relationship building and closing.**

---

## 3. Business Problem

PrimeHomes Realty may receive hundreds of enquiries from potential customers.

These enquiries contain valuable information, but the information is usually unstructured.

For example:

> “I need a 3 bedroom somewhere around Lekki, budget is about 80m and I want to move in soon.”

Important information exists inside the sentence:

| Field | Extracted Value |
|---|---|
| Intent | Buying |
| Property Type | Apartment |
| Bedrooms | 3 |
| Location | Lekki |
| Budget | ₦80,000,000 |
| Timeline | Immediate / Short-term |

Without automation, a sales representative must manually extract this information.

At scale, this can result in:

- Leads not being recorded
- Important information being missed
- Slow responses
- Inconsistent qualification
- Poor prioritization
- Lost leads
- Difficult reporting
- Poor visibility into sales pipeline

---

## 4. Problem Statement

### Current State

Potential customers send enquiries through digital channels.

Sales representatives manually:

```text
Read message
    ↓
Understand customer
    ↓
Extract requirements
    ↓
Ask missing questions
    ↓
Record information
    ↓
Determine lead quality
    ↓
Respond
    ↓
Follow up
```

### Desired State

The system should automate much of this process:

```text
Customer Message
       ↓
AI Understanding
       ↓
Information Extraction
       ↓
Lead Qualification
       ↓
Database
       ↓
Customer Response
       ↓
Sales Notification
       ↓
Human Follow-up
       ↓
Lead Tracking
```

---

## 5. Product Goals

### G1 — Automate Lead Capture

Automatically convert customer messages into structured lead records.

### G2 — Understand Natural Language

Allow customers to communicate naturally rather than forcing them to complete a rigid form.

### G3 — Extract Customer Requirements

Extract relevant property and customer information from conversations.

### G4 — Qualify Leads

Determine the potential value and urgency of a lead using defined business rules.

### G5 — Improve Response Time

Provide an immediate response to customers whenever possible.

### G6 — Reduce Sales Team Workload

Remove repetitive information collection and data entry from the sales process.

### G7 — Improve Lead Visibility

Give the sales team a structured view of leads and their current status.

### G8 — Enable Follow-up

Ensure leads can be assigned, contacted, updated, and tracked.

### G9 — Maintain Data Consistency

Create a reliable structured record of each lead and its interactions.

---

## 6. Non-Goals

The first version should not attempt to become a complete real estate ERP/CRM.

The following are outside the initial MVP:

- Full property marketplace
- Property listing management
- Property valuation
- Automated negotiation
- Automated contract generation
- Payment processing
- Property ownership verification
- Legal document management
- Automated sales closing
- Mortgage processing
- Advanced predictive sales forecasting
- Fully autonomous AI sales agent
- AI making binding commitments to customers

The AI should assist the sales process, not make decisions that require human authorization.

---

## 7. Target Users

### 7.1 Potential Customer / Lead

A person interested in:

- Buying property
- Renting property
- Buying land
- Selling property
- Enquiring about available properties

They interact primarily with the bot.

### 7.2 Sales Representative

Responsible for:

- Reviewing leads
- Contacting customers
- Following up
- Updating lead status
- Scheduling meetings/viewings
- Converting qualified leads

### 7.3 Sales Manager

Responsible for:

- Monitoring leads
- Assigning leads
- Reviewing team performance
- Monitoring high-value leads
- Reviewing pipeline
- Managing qualification rules

### 7.4 System Administrator

Responsible for:

- System configuration
- User management
- Integration configuration
- Monitoring
- Managing system-level settings

---

## 8. Core User Journey

The primary journey is:

```text
Customer arrives
      ↓
Starts conversation
      ↓
Bot welcomes customer
      ↓
Customer describes requirement
      ↓
AI understands message
      ↓
Information extracted
      ↓
Missing information identified
      ↓
Bot asks relevant questions
      ↓
Lead becomes sufficiently qualified
      ↓
Lead scored
      ↓
Lead stored
      ↓
Customer receives response
      ↓
Sales team notified
      ↓
Sales representative follows up
      ↓
Lead status updated
      ↓
Lead eventually converted/lost
```

---

## 9. Core Lead Information

The system should maintain structured information about each lead.

### 9.1 Customer Information

```text
lead_id
name
email
phone
preferred_contact_channel
```

Some fields may initially be unknown.

**The system must not invent missing information.**

### 9.2 Property Requirements

```text
property_type
bedrooms
bathrooms
location
preferred_locations
budget_min
budget_max
currency
property_condition
```

Potential property types:

- Apartment
- House
- Duplex
- Terrace
- Detached House
- Land
- Commercial Property
- Office
- Other

### 9.3 Transaction Intent

`transaction_type`

Possible values:

```text
BUY
RENT
SELL
INQUIRE
```

### 9.4 Timeline

Possible values:

```text
IMMEDIATE
WITHIN_1_MONTH
WITHIN_3_MONTHS
WITHIN_6_MONTHS
RESEARCHING
UNKNOWN
```

### 9.5 Lead Status

Example lifecycle:

```text
NEW
QUALIFYING
QUALIFIED
ASSIGNED
CONTACTED
ENGAGED
VIEWING_SCHEDULED
NEGOTIATING
CONVERTED
LOST
NURTURE
```

The exact state machine will be defined in the System Architecture / Technical Specification.

---

## 10. AI Requirements

The AI layer should perform several specific tasks.

### 10.1 Intent Detection

Determine what the customer is trying to accomplish.

Example:

> “I need to rent a 2-bedroom apartment in Ikeja.”

Output:

```json
{
  "intent": "RENT",
  "property_type": "APARTMENT",
  "bedrooms": 2,
  "location": "Ikeja"
}
```

### 10.2 Entity Extraction

Extract structured information from natural language.

Example:

> “I have about ₦80m and need a 3-bedroom around Lekki.”

Output:

```json
{
  "property_type": "APARTMENT",
  "bedrooms": 3,
  "location": "Lekki",
  "budget_max": 80000000,
  "currency": "NGN"
}
```

### 10.3 Missing Information Detection

The AI should determine what important information is still missing.

Example:

**Known:**

```text
Property: Apartment
Bedrooms: 3
Location: Lekki
```

**Missing:**

```text
Budget
Timeline
Contact information
```

The bot can then ask:

> “Great. What budget range are you working with?”

### 10.4 Conversation Understanding

The system must maintain conversation context.

Example:

**Customer:**

> I need a house in Lekki.

**Bot:**

> Sure. Are you looking to buy or rent?

**Customer:**

> Buy.

The system should understand that:

```text
transaction_type = BUY
location = Lekki
property_type = HOUSE
```

rather than treating “Buy” as an independent enquiry.

---

## 11. Lead Qualification

The system should assign a lead score based on defined business rules.

The score should initially be explainable and deterministic, rather than relying entirely on an AI-generated score.

For example:

| Signal | Example |
|---|---:|
| Budget provided | +20 |
| Phone/email provided | +15 |
| Specific location | +15 |
| Specific property requirement | +15 |
| Immediate timeline | +20 |
| Clear buying/renting intent | +10 |
| Very vague enquiry | -10 |

Example:

```text
Lead Score: 85
Classification: HOT
```

Possible classifications:

```text
HOT
WARM
COLD
UNQUALIFIED
```

### Important Requirement

The AI may extract signals, but the backend/workflow should ideally perform the final scoring using documented rules.

This keeps qualification:

- Explainable
- Testable
- Auditable
- Consistent

---

## 12. Lead Routing

Once qualified, the system should determine what happens next.

Example:

```text
Score >= 80
     ↓
HOT
     ↓
Immediate Sales Notification

Score 50–79
     ↓
WARM
     ↓
Normal Sales Queue

Score < 50
     ↓
COLD
     ↓
Nurture / Follow-up
```

Routing rules should eventually be configurable rather than hard-coded wherever practical.

---

## 13. Customer Response Requirements

The bot should provide appropriate responses based on the current conversation state.

### Example — Complete Lead

**Customer:**

> “I need a 3-bedroom apartment in Lekki. Budget is ₦80m. I want to buy within two months.”

**Bot:**

> “Thanks! I’ve captured your requirements for a 3-bedroom apartment in Lekki with a budget around ₦80 million. Our sales team will review suitable options and get back to you shortly.”

### Example — Missing Information

**Customer:**

> “I want a 3-bedroom apartment in Lekki.”

**Bot:**

> “Absolutely. Are you looking to buy or rent, and what budget range are you considering?”

### Example — Very Vague

**Customer:**

> “I want a house.”

**Bot:**

> “Sure, I’d be happy to help. Are you looking to buy or rent, and which location are you interested in?”

---

## 14. Human Handoff

AI should not attempt to handle every situation indefinitely.

The system should support escalation to a human sales representative.

Triggers may include:

- Customer explicitly requests a human
- High-value lead
- Customer expresses urgency
- Complex enquiry
- AI confidence below threshold
- Complaint
- Negotiation
- Sensitive issue
- AI unable to understand request

Example:

```text
AI
 ↓
Human assistance required
 ↓
Sales Team
```

The conversation history and extracted lead information should be available to the sales representative.

---

## 15. Sales Team Requirements

Sales representatives should be able to view:

- Lead ID
- Customer
- Intent
- Property
- Location
- Budget
- Score
- Priority
- Status
- Assigned Agent
- Created At
- Last Contact

### Update Lead

They should be able to modify:

- Status
- Assignment
- Notes
- Priority
- Follow-up date
- Contact outcome

### Follow Up

The system should support recording:

- Contacted
- Call completed
- WhatsApp contacted
- Meeting scheduled
- Property viewing
- Customer requested more options
- No response
- Converted
- Lost

---

## 16. Lead Lifecycle

The system should maintain a traceable lifecycle.

```text
NEW
 ↓
QUALIFYING
 ↓
QUALIFIED
 ↓
ASSIGNED
 ↓
CONTACTED
 ↓
ENGAGED
 ↓
VIEWING_SCHEDULED
 ↓
NEGOTIATING
 ↓
CONVERTED
```

Alternative outcome:

```text
CONTACTED
 ↓
NO RESPONSE
 ↓
NURTURE
```

or:

```text
QUALIFIED
 ↓
LOST
```

Every significant state change should ideally be recorded in an activity/history log.

---

## 17. System Components

The product will initially consist of five major layers.

### 1. React Frontend

Responsible for:

- Chat UI
- Lead forms
- Sales dashboard
- Lead details
- Status management
- Follow-up interface

### 2. FastAPI Backend

Responsible for:

- API endpoints
- Request validation
- Authentication/authorization
- Business logic
- Lead operations
- Database access where appropriate
- Security
- Integration boundaries

### 3. n8n

Responsible primarily for:

- Workflow orchestration
- Trigger handling
- AI workflow execution
- Notifications
- Integrations
- Google Sheets synchronization
- Follow-up automation

### 4. SQL Database

The SQL database will be the primary system of record for structured application data.

Potential candidates:

- PostgreSQL
- MySQL

The final choice will be documented in the Architecture/Database specification.

### 5. Google Sheets

Google Sheets may be used for:

- Operational visibility
- Simple reporting
- Sales-team exports
- n8n-friendly business workflows
- Temporary/secondary operational data

**Important architectural principle:**

> Google Sheets should not automatically become the authoritative database if a SQL database is being used.

The architecture document will define exactly which data belongs in SQL versus Sheets.

---

## 18. Functional Requirements

### FR-001 — Receive Customer Message

The system must be able to receive a customer message through the supported frontend/channel.

### FR-002 — Validate Incoming Data

The system must validate incoming requests before processing.

Invalid requests should return structured errors.

### FR-003 — Create Conversation

The system must associate messages with a conversation/session.

### FR-004 — Process Customer Message

The system must send relevant customer messages to the AI processing workflow.

### FR-005 — Extract Lead Information

The system must extract relevant structured information.

### FR-006 — Preserve Unknown Fields

If information is not provided, the system must represent it as unknown/null rather than inventing values.

### FR-007 — Identify Missing Information

The system must determine whether additional information is needed to qualify the lead.

### FR-008 — Generate Response

The system must generate an appropriate response based on:

- Current conversation
- Known lead information
- Missing information
- Business rules

### FR-009 — Calculate Lead Score

The system must calculate a lead score according to defined qualification rules.

### FR-010 — Classify Lead

The system must classify leads according to their score and/or business rules.

### FR-011 — Store Lead

Qualified and captured leads must be persisted in the SQL database.

### FR-012 — Notify Sales Team

The system must notify the relevant sales team when defined conditions are met.

### FR-013 — Assign Lead

Authorized sales users must be able to assign leads.

### FR-014 — Update Lead Status

Authorized users must be able to update lead lifecycle status.

### FR-015 — Record Follow-up

The system must allow sales representatives to record follow-up activities.

### FR-016 — View Conversation History

Authorized users should be able to view relevant customer conversation history.

### FR-017 — Track Lead Activity

Important lead events should be recorded.

Examples:

```text
Lead Created
AI Qualified
Score Changed
Assigned
Sales Contacted
Status Changed
Follow-up Scheduled
Converted
Lost
```

---

## 19. Non-Functional Requirements

These are extremely important because this is a real system rather than just an automation demo.

### Performance

The system should provide an initial acknowledgement quickly, even if AI processing takes longer.

Where appropriate:

```text
Request
 ↓
Immediate acknowledgement
 ↓
Asynchronous processing
```

rather than keeping the client connection open unnecessarily.

### Reliability

Failures in one component should not unnecessarily destroy the entire lead.

For example:

```text
AI fails
 ↓
Lead should still be recorded where possible
```

### Security

The system should:

- Authenticate internal users
- Authorize actions
- Protect customer information
- Secure API endpoints
- Protect secrets
- Validate external requests
- Avoid exposing internal system details
- Log security-relevant events

### Observability

The system should provide:

- Application logs
- Workflow logs
- Error tracking
- Request identifiers
- AI processing status
- Lead processing status

### Scalability

The architecture should initially support the expected workload while allowing future scaling.

The system should not prematurely introduce unnecessary microservices.

A **modular monolith + n8n orchestration** approach may be sufficient initially.

---

## 20. Data Ownership Principle

This needs to be established early.

### SQL Database — System of Record

PostgreSQL is the authoritative source of truth for leads, conversations, messages, scores, assignments, follow-ups, and activities.

### Google Sheets — Operational Projection

Google Sheets may mirror or summarize data for operational convenience, but it is not the system of record.

---

*Full PRD content is preserved from the original document. This file was relocated into `docs/prd/` during project scaffolding.*
