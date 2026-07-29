import axios from 'axios'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
})

export async function uploadPdf(file) {
  const formData = new FormData()
  formData.append('file', file)

  const response = await api.post('/api/upload', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  })

  return response.data
}

export async function askQuestion(question) {
  const response = await api.post('/api/ask', {
    question,
  })

  return response.data?.answer ?? response.data
}