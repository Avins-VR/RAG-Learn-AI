import React from 'react'
import { BookOpen } from 'lucide-react'
import UploadSection from './UploadSection.jsx'
import QuestionInput from './QuestionInput.jsx'
import SubmitButton from './SubmitButton.jsx'

export default function Sidebar({
  uploadedFile, setUploadedFile,
  question, setQuestion,
  onSubmit, loading,
}) {
  return (
    <div className="flex flex-col gap-0 px-4 sm:px-5 py-5 sm:py-6 h-full">
      {/* Brand */}
      <div className="flex items-center gap-2 mb-2">
        <BookOpen size={20} color="#63b3ed" strokeWidth={2} />
          <span
            className="font-bold tracking-widest uppercase"
            style={{
              fontSize: '1.1rem',
              color: '#63b3ed',
              letterSpacing: '0.06em',
              wordBreak: 'break-word',
            }}
          >
          RAG Learn AI
        </span>
      </div>
      <p
        style={{
          color: '#718096',
          fontSize: '0.75rem',
          wordBreak: 'break-word',
        }}
        className="mb-5"
      >
        100% RAG · Powered by Groq
      </p>

      <Divider />

      <UploadSection uploadedFile={uploadedFile} setUploadedFile={setUploadedFile} />

      <Divider />

      <QuestionInput question={question} setQuestion={setQuestion} />

      <SubmitButton onSubmit={onSubmit} loading={loading} />

      <Divider />

      <p style={{ color: '#718096', fontSize: '0.75rem', lineHeight: 1.6 }}>
        Upload a PDF, enter your question, then click{' '}
        <strong style={{ color: '#e2e8f0' }}>Get Answer</strong>.
      </p>
    </div>
  )
}

function Divider() {
  return (
    <hr
      style={{
        borderColor: 'rgba(255,255,255,0.08)',
        margin: '1rem 0',
      }}
    />
  )
}