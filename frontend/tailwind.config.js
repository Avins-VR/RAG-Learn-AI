/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Sora', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
      },
      colors: {
        bg:       '#0a0c10',
        surface:  '#0f1117',
        accent:   '#63b3ed',
        accent2:  '#76e4b0',
        text:     '#e2e8f0',
        muted:    '#718096',
        danger:   '#fc8181',
        warn:     '#f6ad55',
      },
      borderColor: {
        DEFAULT: 'rgba(255,255,255,0.08)',
      },
    },
  },
  plugins: [],
}