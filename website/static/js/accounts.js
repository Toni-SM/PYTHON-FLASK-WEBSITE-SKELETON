
var REMOVE_ACCOUNT_EMAIL = "";

function validateData(){
    // invalid fields
    if(typeof($("input:invalid")[0])==="object"){
        return false;
    }
    // static fields
    if(!$("#field-name").val().length){
        return false;
    }
    if(!$("#field-surname").val().length){
        return false;
    }
    if(!$("#field-category").val().length){
        return false;
    }
    if(!$("#field-email").val().length){
        return false;
    }
    if(!$("#field-password").val().length){
        return false;
    }
    if(!$("#field-repeat-password").val().length){
        return false;
    }
    return true;
}

function register(){
    // validate
    if(!validateData()){
        showMessage("warning", "There are empty required fields or incorrect data", 2500);
        return;
    }
    
    // check password
    if($("#field-password").val()!=$("#field-repeat-password").val()){
        showMessage("warning", "The passwords didn't match. Try again", 2500);
        return;
    }
    
    if($("#field-password").val().length<8){
        showMessage("warning", "Please choose a stronger password. Try a mix of letters, numbers, and symbols.", 2500);
        return;
    }
    
    var data={
        "name": $("#field-name").val(),
        "surname": $("#field-surname").val(),
        "category": $("#field-category").val(),
        "email": $("#field-email").val(),
        "password": $("#field-password").val()
    };
    
    $.post('/register', {"data": JSON.stringify(data)}, function(response){
        console.log(response);
        if(response.status){
            window.open("/accounts", "_self");
        }
        else{
            showMessage("danger", response.message, 2500);
        }
    });
}

function showModalRemove(data){
    $("#modal-remove-account-name").html(data["name"]);
    $("#modal-remove-account-surname").html(data["surname"]);
    $("#modal-remove-account-category").html(data["category"]);
    $("#modal-remove-account-email").html(data["email"]);
 
    REMOVE_ACCOUNT_EMAIL=data["email"];
    $('#modal-remove-account').modal("show");
}

function remove(){
    var data={"email": REMOVE_ACCOUNT_EMAIL};
    
    $.post('/remove', {"data": JSON.stringify(data)}, function(response){
        console.log(response);
        if(response.status){
            window.open("/accounts", "_self");
        }
        else{
            $('#modal-remove-account').modal("hide");
            showMessage("danger", response.message, 2500);
        }
    });
}

$('#button-register-account').click(function(){
    register();
});

$('#button-remove-account').click(function(){
    remove();
});
