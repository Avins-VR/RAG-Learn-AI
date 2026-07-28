import React from 'react'
import { X } from 'lucide-react'

export default function SidebarLayout({
  children,
  sidebarOpen,
  setSidebarOpen,
}) {
  return (
    <aside
      style={{
        background: '#0f1117',
        borderRight: '1px solid rgba(255,255,255,0.08)',
      }}
      className={`
        fixed md:relative
        top-0 left-0
        h-full
        w-[420px] lg:w-99
        z-[1000]
        flex flex-col
        overflow-y-auto
        transition-transform duration-300
        ${sidebarOpen ? 'translate-x-0' : '-translate-x-full'}
        md:translate-x-0
      `}
    >
      <button
        onClick={() => setSidebarOpen(false)}
        className="md:hidden"
        style={{
          position: 'absolute',
          top: '1rem',
          right: '1rem',
          background: 'transparent',
          border: 'none',
          color: '#fff',
        }}
      >
        <X size={20} />
      </button>

      {children}
    </aside>
  )
}