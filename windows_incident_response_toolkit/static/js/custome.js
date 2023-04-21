var term = new Terminal();
term.open(document.getElementById('terminal'));



function scan(host, action) {



    let csf = $("input[name=csrfmiddlewaretoken]").val();

    // for (var action = 1; action <= 12; action++) {


    var data = {
        host: host,
        action: action
    };

    $.ajax({
        headers: { "X-CSRFToken": csf },
        mode: "same-origin",
        url: "/action",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(data) {
            console.log(data);
            for (var i = 0; i < data.data.length; i++) {
                term.write(data.data[i])
                term.write('\n')
            }
            // term.write(data.data)
            if (action <= 13) {
                action = action + 1;
                scan(host, action)
            }
            // if (data.msg == "sucess") {
            //     alertify.success("Success");
            // } else {
            //     alertify.error("error");
            // }
        },
        // complete: function() {
        //     $(".preloader").css("visibility", "hidden");
        // },
    });
}
// }