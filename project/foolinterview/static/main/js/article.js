$(document).ready(function() {
    function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie !== '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = cookies[i].trim();
                        if (cookie.substring(0, name.length + 1) === (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                   }
            return cookieValue;
            }
    $( '#reload-quotes').on('click', function() {
        location.reload();
    })
    $( '#submit-comment').on('click', function() {
        var csrftoken = getCookie('csrftoken');
        var uuid = document.getElementById('uuid').value;
        var comment = document.getElementById('comment').value;
        var post_data = {'uuid': uuid,
                         'comment': comment};
        console.log(post_data)
        console.log(csrftoken)
//        function csrfSafeMethod(method) {
//            // these HTTP methods do not require CSRF protection
//            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
//        }
//        $.ajaxSetup({
//            beforeSend: function(xhr, settings) {
//                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
//                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
//                }
//            }
//        });
        $.ajax({
            url: '/addcomment/post/',
            method: 'POST',
            headers: {"csrftoken": csrftoken},
            data: JSON.stringify(post_data)
        })
        location.reload();
    })
});

