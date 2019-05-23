
function showMessage(_message_class, _message_html, _message_timeout){
    $("#message-"+_message_class).html(_message_html);
    $("#message-"+_message_class).css("display", "block");
    setTimeout(function(){
        $("#message-"+_message_class).css("display", "none");
    }, _message_timeout);
}
