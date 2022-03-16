const express = require('express')

const app = express()

app.get('/', (req, res) => {
    res.end("Hello from our nodejs server")
})

app.listen(3000, () => {
    console.log('web server is working')
})