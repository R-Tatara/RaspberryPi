var http = require('http');
var socketio = require('socket.io');
var fs = require('fs'); //Filestream module
var exec = require('child_process').exec; //For linux command
var port = 8080;
var pi_data;
var pi_state = '1';

var server = http.createServer(serveron);
server.listen(port);
var io = socketio.listen(server);
console.log('http websocket server started.');

//Callbak function for http request
function serveron(req,res) {
    if(req.url == '/favicon.ico'){
        return;
    }

    //console.log(req.method); //GET
    res.writeHead(200, {'Content-Type' : 'text/html'});
    res.end(fs.readFileSync(__dirname + '/index.html', 'utf-8'));
}

//Callback function for connection
io.sockets.on('connection', function(socket){
    console.log('socket connected.');
    setInterval(function(){
        //Send data
        socket.emit('Pi_data', {value : pi_data});
        socket.emit('Pi_state', {value : pi_state});
    }, 1);
});

//Get data
setInterval(function(){
    exec('date +"%Y/%m/%d %H:%M:%S.%3N"', function(err, stdout, stderr){
        pi_data = stdout;
    });
}, 1);
