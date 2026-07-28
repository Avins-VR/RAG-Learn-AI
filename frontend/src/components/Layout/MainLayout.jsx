import React from 'react'

export default function MainLayout({ children }) {
  return (
    <main className="flex-1 h-full overflow-y-auto md:ml-0" style={{ background: 'transparent' }}>
      <div className="max-w-5xl mx-auto px-4 md:px-8 pt-10 pb-16">
        {children}
      </div>
    </main>
  )
}