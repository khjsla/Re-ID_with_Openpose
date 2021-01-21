const express = require('express');
const app = express();
const cors = require('cors'); //for use cors
const bodyParser = require('body-parser');
const port = process.env.PORT || 3001;
//리액트와 포트번호가 충돌나면 안되므로, 다른 포트번호를 사용해야 한다. 
//즉, default 의 경우, 3000포트를 피해서 설정을 해준다
const route = require('./routes/index'); // THIS IS ROUTER !

app.use(cors()); //for use cors
//for 외부 접속 ㅇㅇ

app.use(bodyParser.json());
app.use('/api', route); // app.use('/api', (req, res)=> res.json({username:'bryan'}));
//app.use('/api', (req, res) => res.json({ username: 'DY and HJ' }));

app.listen(port, () => {
    console.log(`express is running on ${port}`);
})