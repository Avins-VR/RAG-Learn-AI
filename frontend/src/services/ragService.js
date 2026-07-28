import axios from 'axios'

export async function uploadPdf(file) {
  const formData = new FormData()
  formData.append('file', file)
  const response = await axios.post('/api/upload', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  })
  return response.data
}

export async function askQuestion(question) {
  const response = await axios.post('/api/ask', { question })
  return response.data?.answer ?? response.data
}