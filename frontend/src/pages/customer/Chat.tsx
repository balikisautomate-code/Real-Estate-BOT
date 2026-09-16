import { useState, useEffect, useRef } from 'react'
import { api } from '../../services/api'
import './Chat.css'

interface Msg {
  id: string
  content: string
  sender_type: string
  created_at: string
  status?: 'sending' | 'sent' | 'failed'
}

export default function CustomerChat() {
  const [conversationId, setConversationId] = useState<string | null>(null)
  const [messages, setMessages] = useState<Msg[]>([])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)
  const [typing, setTyping] = useState(false)
  const bottomRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    // Start a new conversation on mount
    api.createConversation()
      .then((conv) => setConversationId(conv.id))
      .catch(console.error)
  }, [])

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages, typing])

  const send = async () => {
    if (!input.trim() || !conversationId || loading) return

    const text = input.trim()
    setInput('')
    const tempId = `temp-${Date.now()}`
    setMessages((prev) => [
      ...prev,
      { id: tempId, content: text, sender_type: 'CUSTOMER', created_at: new Date().toISOString(), status: 'sending' },
    ])
    setLoading(true)
    setTyping(true)

    try {
      const msg = await api.sendMessage(conversationId, text)
      setMessages((prev) =>
        prev.map((m) => (m.id === tempId ? { ...msg, status: 'sent' } : m))
      )

      // Simulate bot thinking then poll for response (in real flow n8n + AI would push back)
      // For now we show a friendly acknowledgement while n8n processes
      setTimeout(() => {
        setMessages((prev) => [
          ...prev,
          {
            id: `bot-${Date.now()}`,
            content: "Thanks! I've received your message and I'm looking into the best options for you. Our team will follow up shortly.",
            sender_type: 'BOT',
            created_at: new Date().toISOString(),
          },
        ])
        setTyping(false)
      }, 1800)
    } catch (err) {
      setMessages((prev) =>
        prev.map((m) => (m.id === tempId ? { ...m, status: 'failed' } : m))
      )
      setTyping(false)
    } finally {
      setLoading(false)
    }
  }

  const handleKey = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      send()
    }
  }

  return (
    <div className="chat-page">
      <div className="chat-card">
        <header className="chat-header">
          <div className="avatar">🏠</div>
          <div>
            <h1>PrimeHomes Assistant</h1>
            <p>How can we help you find your next home?</p>
          </div>
        </header>

        <div className="chat-messages">
          {messages.length === 0 && (
            <div className="welcome">
              <div className="welcome-bubble">
                Hi there! 👋 I'm the PrimeHomes assistant. Tell me what you're looking for —
                location, budget, number of bedrooms — and I'll help get you started.
              </div>
            </div>
          )}

          {messages.map((m) => (
            <div
              key={m.id}
              className={`message ${m.sender_type === 'CUSTOMER' ? 'customer' : 'bot'} ${m.status === 'failed' ? 'failed' : ''}`}
            >
              <div className="bubble">{m.content}</div>
              {m.status === 'failed' && <span className="error-hint">Failed to send</span>}
            </div>
          ))}

          {typing && (
            <div className="message bot">
              <div className="bubble typing">
                <span></span><span></span><span></span>
              </div>
            </div>
          )}

          <div ref={bottomRef} />
        </div>

        <div className="chat-input-area">
          <textarea
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKey}
            placeholder="Type your message... e.g. I need a 3-bedroom apartment in Lekki"
            rows={1}
            disabled={!conversationId}
          />
          <button onClick={send} disabled={!input.trim() || loading || !conversationId} className="send-btn">
            {loading ? '...' : 'Send'}
          </button>
        </div>
      </div>
    </div>
  )
}
