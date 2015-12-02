var autocomplete = (function() {

	function searching() {
		console.log("hey");
		$(document).ready(function() {
			$("#id_name").autocomplete({
				source: function(request, response) {
					$.ajax({
						 method : 'GET',
						 url: '/account/search_product/?name=' + $('#id_name').val(),
						 type: 'json',
						 success: function(data){
							response($.map(data,function(v,i) {
								return {
									id: v.id,
									label: v.title,
									value: v.title
								}
							}))
						}
					});
				},
				select: function(e, ui){
					window.location.href = '/products/product/' + ui.item.id + '/';
				}
			});
		});
	}

	return {
		init: function() {
			searching();
		}
	};
})();

						
