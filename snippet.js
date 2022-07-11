// snippet.js
// use fetch API to send POST request

const url = 'http://127.0.0.1:5000';

// post body data
const body = {
	client_version: '1.0'
};

// request options
const options = {
	method: 'POST',
	body: JSON.stringify(body),
	headers: {
		'Content-Type': 'application/json'
	}
}

fetch(url, options)
