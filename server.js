const express = require('express')
const path = require('path')
const app = express()

app.use(express.static(path.join(__dirname)))

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'login.html'))
})

app.get('/dashboard', (req, res) => {
  res.sendFile(path.join(__dirname, 'dashboard.html'))
})

app.get('/home', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'))
})

app.get('/shop', (req, res) => {
  res.sendFile(path.join(__dirname, 'shop.html'))
})

app.get('/cart', (req, res) => {
  res.sendFile(path.join(__dirname, 'cart.html'))
})

app.get('/about', (req, res) => {
  res.sendFile(path.join(__dirname, 'about.html'))
})

const PORT = process.env.PORT || 3000
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`)
})