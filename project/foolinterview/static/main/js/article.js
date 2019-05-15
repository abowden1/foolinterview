$(document).ready(function() {
    $( "#reload-quotes").on("click", function() {
        console.log("Shuffling")
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
        var csrftoken = getCookie('csrftoken');
        console.log(csrftoken)
        $.ajax({
            url: "/shuffle",
            type: 'POST',
            headers: {"X-CSRFToken" : csrftoken},
            success: console.log("success")
        })
//        console.log(response)
        .done(function(response){
            $("#reloadable").append(response)
        })
    })
});