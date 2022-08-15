// snippet.js
// use fetch API to send POST request

const url = 'http://analytics.lukewiebe.tech';

// post body data
const body = {
	client_version: '1.0',
	source_page: 'test'
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
