import React from 'react'
import { Search } from 'lucide-react'

export default function SubmitButton({ onSubmit, loading }) {
  return (
    <button
      onClick={onSubmit}
      disabled={loading}
      style={{
        width: '100%',
        background: 'linear-gradient(135deg, #3a7bd5 0%, #63b3ed 100%)',
        border: 'none',
        borderRadius: '14px',
        color: '#fff',
        fontFamily: "'Sora', sans-serif",
        fontWeight: 600,
        fontSize: '0.88rem',
        textAlign: 'center',
        letterSpacing: '0.05em',
        padding: '0.75rem 1rem',
        cursor: loading ? 'not-allowed' : 'pointer',
        opacity: loading ? 0.7 : 1,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        gap: '0.5rem',
        transition: 'opacity 0.2s ease, transform 0.15s ease, box-shadow 0.2s ease',
        boxShadow: '0 4px 20px rgba(99,179,237,0.25)',
        marginTop: '1rem',
        marginBottom: '1.3rem',
      }}
      onMouseEnter={(e) => {
        if (!loading) {
          e.currentTarget.style.opacity = '0.9'
          e.currentTarget.style.transform = 'translateY(-1px)'
          e.currentTarget.style.boxShadow = '0 8px 28px rgba(99,179,237,0.35)'
        }
      }}
      onMouseLeave={(e) => {
        e.currentTarget.style.opacity = loading ? '0.7' : '1'
        e.currentTarget.style.transform = 'translateY(0)'
        e.currentTarget.style.boxShadow = '0 4px 20px rgba(99,179,237,0.25)'
      }}
      onMouseDown={(e) => {
        e.currentTarget.style.transform = 'translateY(0)'
      }}
    >
      <Search size={15} />
      {loading ? 'Processing…' : 'Get Answer'}
    </button>
  )
}