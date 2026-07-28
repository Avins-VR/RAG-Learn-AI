import React from 'react'
import { FileText } from 'lucide-react'
import AppLayout from '../components/Layout/AppLayout.jsx'
import Sidebar from '../components/Sidebar/Sidebar.jsx'
import EmptyState from '../components/Answer/EmptyState.jsx'
import LoadingState from '../components/Answer/LoadingState.jsx'
import ErrorState from '../components/Answer/ErrorState.jsx'
import QuestionBadge from '../components/Answer/QuestionBadge.jsx'
import AnswerCard from '../components/Answer/AnswerCard.jsx'
import { useRag } from '../hooks/useRag.js'

export default function Home() {
  const {
    uploadedFile, setUploadedFile,
    question, setQuestion,
    answer,
    loading,
    error,
    handleSubmit,
  } = useRag()

  const sidebarContent = (
    <Sidebar
      uploadedFile={uploadedFile}
      setUploadedFile={setUploadedFile}
      question={question}
      setQuestion={setQuestion}
      onSubmit={handleSubmit}
      loading={loading}
    />
  )

  const mainContent = (
    <>
      {/* Title */}
      <div className="flex items-center gap-2 mb-1">
        <FileText size={22} color="#63b3ed" />
        <h1
          style={{
            fontSize: '1.75rem',
            fontWeight: 700,
            letterSpacing: '-0.01em',
            background: 'linear-gradient(135deg, #e2e8f0 30%, #63b3ed 100%)',
            WebkitBackgroundClip: 'text',
            WebkitTextFillColor: 'transparent',
            backgroundClip: 'text',
          }}
        >
          Answer
        </h1>
      </div>

      <p style={{ color: '#718096', fontSize: '0.82rem', marginBottom: '0.75rem' }}>
        The generated answer will appear below once you submit a question.
      </p>

      <hr style={{ borderColor: 'rgba(255,255,255,0.08)', margin: '0.75rem 0 1.25rem' }} />

      {/* States */}
      {loading && <LoadingState />}

      {!loading && error && <ErrorState message={error} />}

      {!loading && !error && answer && (
        <>
          <QuestionBadge question={question} />
          <hr style={{ borderColor: 'rgba(255,255,255,0.08)', margin: '0 0 0.75rem' }} />
          <AnswerCard answer={answer} />
        </>
      )}

      {!loading && !error && !answer && <EmptyState />}
    </>
  )

  return (
    <AppLayout
      sidebarContent={sidebarContent}
      mainContent={mainContent}
    />
  )
}