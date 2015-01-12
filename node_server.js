var http = require('http'),
    url = require('url'),
    fs = require('fs'),
    path = require('path'),
    file_to_serve = 'index.html';

var mime_types = {'js': 'application/javascript', 
		  'css': 'text/css', 
		  'html': 'text/html',
		  'png': 'image/png'}

function serveError(message, response) {
    response.writeHead(500, {"Content-Type": "text/plain"});
    response.write(message + "\n");
    // console.log('Got an Error with message', message);
    response.end();
    return;
}

function serveFile(pathname, response) {
    fs.readFile(pathname, function(err, file) {
	if (err) return serveError(err, response);
	response.writeHead(200, {'Content-Type': mime_types[path.extname(pathname).slice(1)], 'Content-Length': file.length});
	response.write(file);
	// console.log('Serving file', pathname, ' with type', mime_types[path.extname(pathname).slice(1)]);
	response.end();
    })
}

function statResource(resource, response) {

}

function handle_request(request, response) {
    var resource = url.parse(request.url).path;
    
    resource = path.normalize(path.join(process.cwd(), resource));
    if (resource.indexOf(process.cwd()) !== 0) {
        response.writeHead(500, {"Content-Type": "text/plain"});
        response.write("Cannot supply specified request.\n");
        response.end();
        return;
    }
    fs.stat(resource, function(err, stats) {
	if (err) return serveError(err, response);

	if (stats.isDirectory()) {
	    resource = path.join(resource, file_to_serve);
	    serveFile(resource, response);
	}
	if (stats.isFile()) 
	    serveFile(resource, response);
    })
}

var server = http.createServer(handle_request).listen(8000 || Number(process.argv[2]));

