$('document').ready(function () {
    $('DIV#add_item').click(function () {
	const parentElement = $('UL.my_list');
	parentElement.append('<li>Item</li>');
    });
});
