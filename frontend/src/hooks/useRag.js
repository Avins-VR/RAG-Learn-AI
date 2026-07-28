import { useState } from 'react'
import { uploadPdf, askQuestion } from '../services/ragService.js'

export function useRag() {
  const [uploadedFile, setUploadedFile] = useState(null)
  const [question, setQuestion]         = useState('')
  const [answer, setAnswer]             = useState(null)
  const [loading, setLoading]           = useState(false)
  const [error, setError]               = useState(null)

  const handleSubmit = async () => {
    if (!uploadedFile || !question.trim()) {
      setError('Please upload a PDF and enter a question before submitting.')
      return
    }

    setError(null)
    setAnswer(null)
    setLoading(true)

    try {
      await uploadPdf(uploadedFile)
      const result = await askQuestion(question)
      setAnswer(result)
    } catch (err) {
      setError(err?.response?.data?.detail || 'Something went wrong. Please try again.')
    } finally {
      setLoading(false)
    }
  }

  return {
    uploadedFile, setUploadedFile,
    question, setQuestion,
    answer,
    loading,
    error, setError,
    handleSubmit,
  }
}