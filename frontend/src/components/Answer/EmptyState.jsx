import React from 'react'
import { FileText } from 'lucide-react'

export default function EmptyState() {
  return (
    <div
      style={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        gap: '0.75rem',
        padding: '2rem 1rem',
        color: '#718096',
        fontSize: '0.9rem',
        textAlign: 'center',
      }}
    >
      <FileText size={40} style={{ opacity: 0.35 }} />
      <span>
        Upload a PDF and ask a question using the sidebar
        <br />
        to get an AI-generated answer here.
      </span>
    </div>
  )
}