const proxy = require('http-proxy-middleware')
    
module.exports = function(app) {
  console.log('proxy setup')
  app.use(proxy('/api', { target: 'http://localhost:5000/' }))
}