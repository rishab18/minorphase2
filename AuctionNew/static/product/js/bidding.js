var bidding = (function(){
	
    function loadContent() {
        var productid = $(this).attr('data-id');
	 console.log(productid);
	var start = $(this).attr('bid-start');
	 console.log(start);
	var present = $(this).attr('current-bid');
	 console.log(present);
	$("#add-bid-btn").attr("data-id",productid);
	$("#start-bid").html(start);
	$("#current-bid").html(present);
        $.ajax({
            dataType: 'json',
            method: 'GET',
            url: '/products/product/productBidded/' + productid +"/",
            success: function(data){
                console.log(data);
            }
	});
    }
    
    return {
        init : function() {
            $(".bid-now-button").click(loadContent);
        }
    };
})()
