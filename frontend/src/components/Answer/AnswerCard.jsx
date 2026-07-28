import React from 'react'
import { motion } from 'framer-motion'

export default function AnswerCard({ answer }) {
  const lines = typeof answer === 'string' ? answer : JSON.stringify(answer, null, 2)

  return (
    <motion.div
      initial={{ opacity: 0, y: 12 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4, ease: 'easeOut' }}
      style={{
        background: 'rgba(255,255,255,0.04)',
        border: '1px solid rgba(255,255,255,0.08)',
        borderRadius: '14px',
        padding: '1.75rem 2rem',
        marginTop: '0.75rem',
        lineHeight: 1.8,
        fontSize: '0.95rem',
        color: '#e2e8f0',
        whiteSpace: 'pre-wrap',
        wordBreak: 'break-word',
      }}
    >
      {lines}
    </motion.div>
  )
}