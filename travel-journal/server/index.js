const express = require('express')
const app = express()
const cors = require('cors')
const {seed, getCountries, getCities, createCity, deleteCity} = require('./controller.js')
const SERVER_PORT = 4004
app.use(express.json())
app.use(cors())



// DEV
app.post('/seed', seed)

// COUNTRIES
app.get('/countries', getCountries)/

// // CITIES
app.post('/cities', createCity)
app.get('/cities', getCities)
app.delete('/cities/:id', deleteCity)

app.listen(SERVER_PORT, () => console.log(`up on ${SERVER_PORT}`))