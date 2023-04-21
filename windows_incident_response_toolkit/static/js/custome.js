var term = new Terminal({
    scrollback: 10000,
    // scrollOnInput: true,
    // scrollOnOutput: true
});
term.open(document.getElementById('terminal'));

term.resize(Math.floor(window.innerHeight), Math.floor(window.innerWidth));

// listen for resize events and adjust the terminal size accordingly
window.addEventListener('resize', () => {
    term.resize(Math.floor(window.innerHeight), Math.floor(window.innerWidth));
});

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

            term.write(data.action + '\r\n')
            for (var i = 0; i < data.data.length; i++) {
                term.write(data.data[i] + '\r\n')
                    // term.write('\n')
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