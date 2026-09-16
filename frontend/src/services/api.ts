const API_BASE = import.meta.env.VITE_API_URL || '/api/v1'

async function request<T>(path: string, options: RequestInit = {}): Promise<T> {
  const res = await fetch(`${API_BASE}${path}`, {
    headers: {
      'Content-Type': 'application/json',
      ...options.headers,
    },
    ...options,
  })

  if (!res.ok) {
    const err = await res.json().catch(() => ({ error: { message: res.statusText } }))
    throw new Error(err?.error?.message || err?.detail || 'Request failed')
  }

  return res.json()
}

export const api = {
  // Conversations
  createConversation: (channel = 'WEB') =>
    request<{ id: string; lead_id: string }>('/conversations', {
      method: 'POST',
      body: JSON.stringify({ channel }),
    }),

  sendMessage: (conversationId: string, content: string) =>
    request<{ id: string; content: string; sender_type: string; created_at: string }>(
      `/conversations/${conversationId}/messages`,
      {
        method: 'POST',
        body: JSON.stringify({ content, sender_type: 'CUSTOMER' }),
      }
    ),

  getMessages: (conversationId: string) =>
    request<{ items: Array<{ id: string; content: string; sender_type: string; created_at: string }> }>(
      `/conversations/${conversationId}/messages`
    ),

  // Leads
  listLeads: (params?: { page?: number; classification?: string }) => {
    const q = new URLSearchParams()
    if (params?.page) q.set('page', String(params.page))
    if (params?.classification) q.set('classification', params.classification)
    return request<{ items: any[]; total: number }>(`/leads?${q.toString()}`)
  },

  getLead: (id: string) => request<any>(`/leads/${id}`),

  health: () => request<{ status: string }>('/health'),
}
