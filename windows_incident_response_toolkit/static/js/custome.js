function scan(host) {

    let csf = $("input[name=csrfmiddlewaretoken]").val();

    // for (var action = 1; action <= 12; action++) {


    var data = {
        host: host,
        action: 1
    };

    $.ajax({
        headers: { "X-CSRFToken": csf },
        mode: "same-origin",
        url: "/action",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(data) {



            if (data.msg == "sucess") {
                alertify.success("Success");
            } else {
                alertify.error("error");
            }
        },
        // complete: function() {
        //     $(".preloader").css("visibility", "hidden");
        // },
    });
}
// }