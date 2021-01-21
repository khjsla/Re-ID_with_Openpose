//proxy 사용 
const express = require('express');
const router = express.Router();

//for python
var { PythonShell } = require('python-shell');

router.get('/', (req, res)=>res.json({username:'OMG'}));
router.get('/group', (req, res)=>res.json({username:'hi node js!'}));

//Router to handle the incoming request. 
router.get("/py", (req, res, next)=>{ 
    //Here are the option object in which arguments can be passed for the python_test.js. 
    let options = { 
        mode: 'json', 
        pythonOptions: ['-u'], // get print results in real-time 
        scriptPath: '', //If you are having python_test.py script in same folder, then it's optional. 
        args: ['value1'] //An argument which can be accessed in the script using sys.argv[1] 
    }; 
      
    PythonShell.run('./python/test.py', options, function (err, result){ 
          if (err) throw err; 
          // result is an array consisting of messages collected  
          //during execution of script. 
          //let res = result.split(':')
        //   JSON.parse("/\n")
        //   result = JSON.parse(result)
          console.log('result: ', res.toString()); 
          res.json({username:res.toString()}) 
    }); 
}); 

module.exports = router;