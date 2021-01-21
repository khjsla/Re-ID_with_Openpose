//to use 프록시
const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function (app) {
    app.use(
        createProxyMiddleware('/api', {
            target: 'http://localhost:3001/',
            changeOrigin: true
        })
    )
};
//proxy ---> createProxyMiddleware 로 변경
//1.0.0 버전부터. 나는 1.0.6
