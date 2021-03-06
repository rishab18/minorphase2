var CoursesManager = (function(formHelper) {
    function add() {
	console.log('h');
        var form = $('#add-course-form')[0];
        var name = $(form).find('input[name=Title]').val();
        var tagline = $(form).find('input[name=BidStart]').val();
        var form_data = new FormData(form);
        console.log(form_data);

        formHelper.clearErrors.call(form);

        function onSuccess(data, status, xhr) {
	    console.log('i');
            var el = $('<li/>');
            el.addClass('collection-item').html(
                name + "<a class='right'>" + "abc" + "</a>"
            );
            $('#course-list').append(el);

            $('#addcourse').closeModal();
            formHelper.clear.call(form);
        }

        $.ajax({
            //url : document.location.origin + '/products/upload/',
            url : '/products/upload/',
            type: 'POST',
            dataType: 'json',
            data: form_data,
            processData: false,
            contentType: false,
            success: onSuccess,
            error: formHelper.handleErrors.bind(form),
        });
    }

    return {
        init : function()  {
            $('#add-course-btn').click(add);
        }
    };
})(AjaxFormHelper);
