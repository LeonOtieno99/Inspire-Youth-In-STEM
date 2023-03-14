
function check_age(){
    let driversname = document.getElementById("dsname").value;
    var agenumber = document.getElementById("age").value;
    console.log("button clicked!")

    if(agenumber === "" || driversname === ""){
        alert("Please fill all boxes")
    }else{
        if(agenumber >= 18){
            msg = "You can drive.";
            console.log("Welcome to my club")
            var full_msg ="Welcome!"+" "+driversname + ", " +msg;
        }else{
            msg = "Your still too young to drive."
            console.log("You are not allowed")
            full_msg = "Sorry!"+" "+driversname + ", " +msg;
        }
    }
   
    document.getElementById("message").innerHTML = full_msg;
}