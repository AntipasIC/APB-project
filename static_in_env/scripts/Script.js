const inputs =document.querySelectorAll('.input');

function focusFunc(){
    let parent = this.parentNode.parentNode;
    parent.classList.add('focus');

}
function blurFunc(){
    let parent = this.parentNode.parentNode;
    if(this.value==""){
        parent.classList.remove('focus');
    }  
}
inputs.forEach(input =>{
    input.addEventListener('focus',focusFunc);
    input.addEventListener('blur',blurFunc);
});
var username =document.forms['form']['username'];
var password =document.forms['form']['password'];

username.addEventListener('textInput',username_Verify);
password.addEventListener('textInput',password_Verify);

var username_error=document.getElementById('username_error');
var password_error = document.getElementById('password_error');

function validated(){
    if (username.value.length<6){
        username.style.color="red";
        username_error.style.display="block";
        username.focus();
        return false;
    }
    if (password.value.length<4){
        password.style.color="red";
        password_error.style.display="block";
        password.focus();
        return false;
    }
}

function username_Verify(){
    if (username.value.length>=8){
        username.style.color="silver";
        username_error.style.display="none";
        return true;
  }
}
function password_Verify(){
    if (password.value.length>=3){
        password.style.color="silver";
        password_error.style.display="none";
        return true;
  }
}
