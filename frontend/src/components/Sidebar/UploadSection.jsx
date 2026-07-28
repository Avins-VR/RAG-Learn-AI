import React, { useRef } from 'react'
import { FolderOpen, File } from 'lucide-react'

export default function UploadSection({ uploadedFile, setUploadedFile }) {
  const inputRef = useRef(null)

  const handleFileChange = (e) => {
    const file = e.target.files?.[0]
    if (file) setUploadedFile(file)
  }

  const handleDrop = (e) => {
    e.preventDefault()
    const file = e.dataTransfer.files?.[0]
    if (file && file.type === 'application/pdf') setUploadedFile(file)
  }

  const handleDragOver = (e) => e.preventDefault()

  return (
    <div className="mb-1">
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
        <FolderOpen size={12} style={{ display: 'inline', marginRight: 5 }} />
        Upload Document
      </p>

      <div
        onClick={() => inputRef.current?.click()}
        onDrop={handleDrop}
        onDragOver={handleDragOver}
        style={{
          background: 'rgba(255,255,255,0.04)',
          border: '1px dashed rgba(99,179,237,0.35)',
          borderRadius: '14px',
          padding: '1rem',
          cursor: 'pointer',
          transition: 'border-color 0.2s ease',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          gap: '0.5rem',
          textAlign: 'center',
          width: '100%',
          boxSizing: 'border-box',
        }}
        onMouseEnter={(e) => {
          e.currentTarget.style.borderColor = '#63b3ed'
        }}
        onMouseLeave={(e) => {
          e.currentTarget.style.borderColor = 'rgba(99,179,237,0.35)'
        }}
      >
        {uploadedFile ? (
          <>
            <File size={20} color="#76e4b0" />
            <span style={{ color: '#76e4b0', fontSize: '0.8rem', fontWeight: 500, wordBreak: 'break-all' }}>
              {uploadedFile.name}
            </span>
          </>
        ) : (
          <>
            <FolderOpen size={20} color="#718096" />
            <span
              style={{
                color: '#718096',
                fontSize: '0.8rem',
                wordBreak: 'break-word',
              }}
            >
              Click or drag a PDF here
            </span>
          </>
        )}
      </div>

      <input
        ref={inputRef}
        type="file"
        accept="application/pdf"
        className="hidden"
        onChange={handleFileChange}
      />
    </div>
  )
}