function validate(){
    var nmregex = /^[0-9]+$/;
    var username = document.getElementById("username").value;//.match(nmregex);
    var password = document.getElementById("password").value;
    var pwdlen = password.length;
    if(username.length == 0)
    {
        alert("Fill Username");
        document.getElementById("username").focus();
        return false;
    }
    else if(password.length == 0)
    {
        alert("Fill Password");
        document.getElementById("password").focus();
        return false;   
    }
    
}