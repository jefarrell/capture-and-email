var pythonShell = require('python-shell');
var express = require('express')
var app = express()


var port = 3000;
var server = require('http').Server(app);
server.listen(port);
console.log('Server listening at port:', port)


function listen() {
	app.get('/', function (req, res) {
		console.log("Got a request");
		res.end();

		pythonShell.run('captureUpload.py', function(err) {
			if (err) throw err;
			console.log('finished');
		});
	});		
}

listen();
