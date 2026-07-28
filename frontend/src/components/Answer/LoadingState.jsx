import React from 'react'

export default function LoadingState() {
  return (
    <div
      style={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        gap: '1rem',
        padding: '3rem 1rem',
        color: '#718096',
        fontSize: '0.88rem',
        textAlign: 'center',
      }}
    >
      <div className="spinner" />
      <span>Processing your document and generating an answer…</span>
    </div>
  )
}