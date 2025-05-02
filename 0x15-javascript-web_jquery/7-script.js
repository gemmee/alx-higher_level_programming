$('document').ready(function () {
    const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

    $.ajax({
	url: url,
	method: 'GET',
	dataType: 'json',
	success: function(data, textStatus, jqXHR) {
	    $('DIV#character').text(`${data.name}`);
	    console.log('Data: ', data);
	    console.log('Status:', textStatus);
	    console.log('XHR Object:', jqXHR);
	},
	error: function(jqXHR, textStatus, errorThrown) {
	    console.error('AJAX request failed:', textStatus, errorThrown);
	},
	complete: function(jqXHR, textStatus) {
	    console.log('AJAX request completed.');
	}
    });
});
