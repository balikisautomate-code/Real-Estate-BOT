import { Routes, Route, Navigate } from 'react-router-dom'
import CustomerChat from '../pages/customer/Chat'
import Dashboard from '../pages/dashboard/Dashboard'
import Layout from '../components/ui/Layout'

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<CustomerChat />} />
      <Route path="/chat" element={<CustomerChat />} />
      <Route
        path="/dashboard/*"
        element={
          <Layout>
            <Dashboard />
          </Layout>
        }
      />
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  )
}
