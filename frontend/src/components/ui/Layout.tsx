import { ReactNode } from 'react'
import { Link, useLocation } from 'react-router-dom'
import './Layout.css'

export default function Layout({ children }: { children: ReactNode }) {
  const location = useLocation()

  return (
    <div className="layout">
      <aside className="sidebar">
        <div className="brand">
          <span className="brand-icon">🏠</span>
          <div>
            <strong>PrimeHomes</strong>
            <small>Lead Bot</small>
          </div>
        </div>
        <nav>
          <Link to="/dashboard" className={location.pathname === '/dashboard' ? 'active' : ''}>
            Dashboard
          </Link>
          <Link to="/dashboard/leads" className={location.pathname.includes('/leads') ? 'active' : ''}>
            Leads
          </Link>
          <Link to="/chat" className="chat-link">
            Open Chat →
          </Link>
        </nav>
      </aside>
      <main className="main">{children}</main>
    </div>
  )
}
