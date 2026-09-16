# Frontend — React

Customer chat interface and sales dashboard for the **PrimeHomes Realty Real Estate Lead Bot**.

## Responsibilities

- Customer chat UI
- Sales dashboard
- Lead list / detail views
- Follow-up management
- Conversation history display

## Recommended Structure

```text
frontend/
├── src/
│   ├── components/
│   │   ├── ui/
│   │   ├── chat/
│   │   ├── leads/
│   │   ├── dashboard/
│   │   └── followups/
│   ├── pages/
│   │   ├── customer/
│   │   ├── auth/
│   │   └── dashboard/
│   ├── services/
│   ├── hooks/
│   ├── types/
│   ├── utils/
│   └── app/
├── package.json
└── README.md
```

## Local Development

```bash
cd frontend
npm install
npm run dev
```

The app will typically run on http://localhost:5173 (Vite) or http://localhost:3000.

> Note: Full React scaffolding (Vite + TypeScript + React Router) will be added in the next implementation step.
