$('document').ready(function () {
    const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

    $.getJSON(url, function(data, textStatus, jqXHR) {
	for (const item of data.results) {
		const title = item.title;
	    	console.log(title);
	    	$('UL#list_movies').append(`<li>${title}</li>`);
	}
	console.log('JSON Data:', data);
	console.log('Status:', textStatus);
	console.log('XHR Object:', jqXHR);
    })
    .done(function() {
	console.log('JSON request finished successfully.');
    })
    .fail(function(jqXHR, textStatus, errorThrown) {
	console.error('JSON request failed:', textStatus, errorThrown);
    })
    .always(function() {
	console.log('JSON request completed.');
    });
});
