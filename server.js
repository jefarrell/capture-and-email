
var express = require('express')
var app = express()


var port = 3000;
var server = require('http').Server(app);
server.listen(port);
console.log('Server listening at port:', port)


function listen() {
	app.get('/', function (req, res) {
		console.log("got request");
		res.end();
		
	})		
}

listen();
