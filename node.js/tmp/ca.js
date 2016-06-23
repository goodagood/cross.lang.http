

request = require('request-json');

//var client = request.createClient('http://localhost:8888/');
var client = request.createClient('http://localhost:5565/');


const p = console.log;
 
var data = {
    ask4: 'math_2_plus_2',
    title: 'my title',
    content: 'my content'
};


client.post('/json_input', data, function(err, res, body) {
    //p(err, res, body);
    p(body);
    p(typeof(body));

    return console.log(res.statusCode);
});


if(require.main === module){

}
