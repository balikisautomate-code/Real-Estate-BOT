# n8n Workflows

This folder contains n8n workflow definitions and related configuration for the Real Estate Lead Bot.

## Planned Workflows

| Workflow Name              | Purpose                                      |
|----------------------------|----------------------------------------------|
| `PRH-LEAD-PROCESS-MESSAGE` | Main message processing + AI extraction      |
| `PRH-LEAD-QUALIFY`         | Deterministic lead scoring & classification  |
| `PRH-LEAD-NOTIFY-SALES`    | Notify sales team for HOT leads              |
| `PRH-FOLLOWUP-REMINDER`    | Scheduled follow-up reminders                |
| `PRH-SHEET-SYNC-LEAD`      | Sync leads to Google Sheets (operational)    |
| `PRH-ERROR-HANDLER`        | Central error handling & alerting            |

## Directory Layout

```text
n8n/
├── workflows/
│   ├── lead-process-message.json
│   ├── lead-qualify.json
│   ├── lead-notify-sales.json
│   ├── followup-reminder.json
│   ├── sheet-sync-lead.json
│   └── error-handler.json
└── README.md
```

Workflows will be exported as JSON and version-controlled here.
