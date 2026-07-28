import React, { useState } from 'react'
import { Menu, X } from 'lucide-react'
import SidebarLayout from './SidebarLayout'
import MainLayout from './MainLayout'

export default function AppLayout({ sidebarContent, mainContent }) {
  const [sidebarOpen, setSidebarOpen] = useState(false)

  return (
    <div className="flex h-screen overflow-hidden">
      {/* Mobile Menu Button */}
      <button
        onClick={() => setSidebarOpen(true)}
        className="md:hidden"
        style={{
          position: 'fixed',
          top: '1rem',
          left: '1rem',
          zIndex: 1001,
          background: '#0f1117',
          border: '1px solid rgba(255,255,255,0.08)',
          borderRadius: '10px',
          padding: '0.6rem',
          color: '#63b3ed',
        }}
      >
        <Menu size={20} />
      </button>

      {/* Overlay */}
      {sidebarOpen && (
        <div
          className="md:hidden"
          onClick={() => setSidebarOpen(false)}
          style={{
            position: 'fixed',
            inset: 0,
            background: 'rgba(0,0,0,0.5)',
            zIndex: 999,
          }}
        />
      )}

      <SidebarLayout
        sidebarOpen={sidebarOpen}
        setSidebarOpen={setSidebarOpen}
      >
        {sidebarContent}
      </SidebarLayout>

      <MainLayout>{mainContent}</MainLayout>
    </div>
  )
}