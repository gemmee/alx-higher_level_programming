$('document').ready(function () {
	const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
	
    	$.getJSON(url, function (data) {
		$('DIV#hello').text(`${data.hello}`);
	});
});
