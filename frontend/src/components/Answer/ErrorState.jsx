import React from 'react'
import { AlertTriangle } from 'lucide-react'

export default function ErrorState({ message }) {
  return (
    <div
      style={{
        background: 'rgba(252,129,129,0.08)',
        border: '1px solid rgba(252,129,129,0.2)',
        borderRadius: '14px',
        padding: '1rem',
        display: 'flex',
        alignItems: 'flex-start',
        gap: '0.75rem',
        flexWrap: 'wrap',
        overflowWrap: 'break-word',
        color: '#fc8181',
        fontSize: '0.88rem',
        marginTop: '0.5rem',
      }}
    >
      <AlertTriangle size={18} style={{ flexShrink: 0, marginTop: 1 }} />
      <span
        style={{
          flex: 1,
          minWidth: 0,
          wordBreak: 'break-word',
        }}
      >
        {message}
      </span>
    </div>
  )
}