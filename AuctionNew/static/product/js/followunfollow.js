var followunfollow = (function() {
    function follow() {
        var productid = $(this).attr('data-id');
        var request = $.ajax({
            method : 'GET',
            url : '/products/product/follow/'+productid+'/',
            dataType : 'json',
            success: function(data, status, xhr) {
                if (data['result'] === 1) {
                    $(this).removeClass('follow');
                    $(this).addClass('unfollow');
                    $(this).html('unfollow');
                }
            }.bind(this)
        });
    }
    function unfollow() {
        var productid = $(this).attr('data-id');
        $.ajax({
            method : 'GET',
            url : '/products/product/unfollow/'+productid+'/',
            dataType : 'json',
            success: function(data, status, xhr) {
                if (data['result'] === 1) {
                    $(this).removeClass('unfollow');
                    $(this).addClass('follow');
                    $(this).html('follow');
                }
            }.bind(this)
        });
    }
    function handleClick(e) {
        e.preventDefault();
        if ($(this).hasClass('follow')) {
            follow.call(this);
        } else {
            unfollow.call(this);
        }
    }
    return {
        init : function() {
            $("a.fnuf").click(handleClick);
        }
    };
})();
