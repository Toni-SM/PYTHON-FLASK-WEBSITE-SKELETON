
function validateData(){
    if(!$("#field-username").val().length){
        return false;
    }
    if(!$("#field-password").val().length){
        return false;
    }
    return true;
}

function login(){
    // validate
    if(!validateData())
        return;
    
    var data={
        "username": $("#field-username").val(),
        "password": $("#field-password").val()
    };
    
    $.post('/login', {"data": JSON.stringify(data)}, function(response){
        console.log(response);
        if(response.status){
            window.open("/", "_self");
        }
        else{
            showMessage("warning", response.message, 1000);
        }
    });
}

$('#button-login').click(function(){
    login();
});
