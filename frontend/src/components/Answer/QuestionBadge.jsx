import React from 'react'
import { MessageSquare } from 'lucide-react'

export default function QuestionBadge({ question }) {
  return (
    <div
      style={{
        display: 'inline-flex',
        alignItems: 'center',
        gap: '0.5rem',
        flexWrap: 'wrap',
        background: 'rgba(99,179,237,0.1)',
        border: '1px solid rgba(99,179,237,0.2)',
        borderRadius: '999px',
        padding: '0.4rem 1rem',
        fontSize: '0.82rem',
        color: '#63b3ed',
        fontWeight: 500,
        marginBottom: '1rem',
        maxWidth: '100%',
        wordBreak: 'break-word',
        overflowWrap: 'break-word',
      }}
    >
      <MessageSquare size={14} style={{ flexShrink: 0 }} />
      {question}
    </div>
  )
}