import React from 'react'
import { MessageSquare } from 'lucide-react'

export default function QuestionInput({ question, setQuestion }) {
  return (
    <div className="mb-3">
      <p
        style={{
          fontSize: '0.72rem',
          fontWeight: 600,
          letterSpacing: '0.12em',
          color: '#718096',
          textTransform: 'uppercase',
          marginBottom: '0.9rem',
        }}
      >
        <MessageSquare size={12} style={{ display: 'inline', marginRight: 5 }} />
        Ask a Question
      </p>
      <textarea
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="e.g. Summarise Chapter 3"
        rows={4}
        style={{
          width: '100%',
          background: 'rgba(255,255,255,0.04)',
          border: '1px solid rgba(255,255,255,0.08)',
          borderRadius: '14px',
          color: '#e2e8f0',
          fontFamily: "'Sora', sans-serif",
          fontSize: '0.9rem',
          padding: '0.75rem 1rem',
          boxSizing: 'border-box',
          resize: 'none',
          outline: 'none',
          transition: 'border-color 0.2s ease, box-shadow 0.2s ease',
        }}
        onFocus={(e) => {
          e.target.style.borderColor = '#63b3ed'
          e.target.style.boxShadow = '0 0 0 3px rgba(99,179,237,0.12)'
        }}
        onBlur={(e) => {
          e.target.style.borderColor = 'rgba(255,255,255,0.08)'
          e.target.style.boxShadow = 'none'
        }}
      />
    </div>
  )
}