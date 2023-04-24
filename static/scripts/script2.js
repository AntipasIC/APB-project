//Openning transfer form
const container=document.querySelector(".container2"); 
const button=document.querySelector(".button button");
const button1=document.querySelector(".button1 img");

 button.addEventListener("click",function(){
    container.classList.remove("hide");
    container.classList.add("show");
}) 
button1.addEventListener("click",function(){
  container.classList.remove("hide");
  container.classList.add("show");
}) 

