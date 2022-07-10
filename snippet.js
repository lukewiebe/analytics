const params = {
		version: 1.0
};
const options = {
		method: 'POST',
		body: JSON.stringify( params )
};
fetch( 'http://127.0.0.1:5000', options )
