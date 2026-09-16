import { useEffect, useState } from 'react'
import { api } from '../../services/api'
import './Dashboard.css'

interface Lead {
  id: string
  name: string | null
  location: string | null
  property_type: string | null
  score: number | null
  classification: string | null
  status: string
  created_at: string
}

export default function Dashboard() {
  const [leads, setLeads] = useState<Lead[]>([])
  const [total, setTotal] = useState(0)
  const [loading, setLoading] = useState(true)
  const [filter, setFilter] = useState<string>('')

  const load = async () => {
    setLoading(true)
    try {
      const data = await api.listLeads({
        classification: filter || undefined,
      })
      setLeads(data.items)
      setTotal(data.total)
    } catch (e) {
      console.error(e)
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    load()
  }, [filter])

  const hot = leads.filter((l) => l.classification === 'HOT').length
  const warm = leads.filter((l) => l.classification === 'WARM').length

  return (
    <div className="dashboard">
      <header className="dash-header">
        <div>
          <h1>Sales Dashboard</h1>
          <p>Manage and follow up on real-estate leads</p>
        </div>
      </header>

      <div className="stats">
        <div className="stat-card">
          <span className="stat-label">Total Leads</span>
          <strong>{total}</strong>
        </div>
        <div className="stat-card hot">
          <span className="stat-label">🔥 Hot</span>
          <strong>{hot}</strong>
        </div>
        <div className="stat-card warm">
          <span className="stat-label">Warm</span>
          <strong>{warm}</strong>
        </div>
      </div>

      <div className="filters">
        <button className={!filter ? 'active' : ''} onClick={() => setFilter('')}>
          All
        </button>
        <button className={filter === 'HOT' ? 'active' : ''} onClick={() => setFilter('HOT')}>
          Hot
        </button>
        <button className={filter === 'WARM' ? 'active' : ''} onClick={() => setFilter('WARM')}>
          Warm
        </button>
        <button className={filter === 'COLD' ? 'active' : ''} onClick={() => setFilter('COLD')}>
          Cold
        </button>
      </div>

      <div className="leads-table-wrap">
        {loading ? (
          <div className="loading">Loading leads...</div>
        ) : leads.length === 0 ? (
          <div className="empty">
            <p>No leads yet.</p>
            <p className="hint">Customer conversations will appear here once they start chatting.</p>
          </div>
        ) : (
          <table className="leads-table">
            <thead>
              <tr>
                <th>Name</th>
                <th>Property</th>
                <th>Location</th>
                <th>Score</th>
                <th>Status</th>
                <th>Created</th>
              </tr>
            </thead>
            <tbody>
              {leads.map((lead) => (
                <tr key={lead.id}>
                  <td>{lead.name || '—'}</td>
                  <td>{lead.property_type || '—'}</td>
                  <td>{lead.location || '—'}</td>
                  <td>
                    <span className={`badge ${(lead.classification || '').toLowerCase()}`}>
                      {lead.score ?? '—'} {lead.classification ? `· ${lead.classification}` : ''}
                    </span>
                  </td>
                  <td>{lead.status}</td>
                  <td>{new Date(lead.created_at).toLocaleDateString()}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  )
}
