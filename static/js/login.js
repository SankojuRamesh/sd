$(document).ready(function(){

 base_url = "http://"+$("#base_url").val()

    $("#signin").click(function(){
       $("#loginnModel").modal('show');
        data=  JSON.stringify({email :$("#email").val(),
        "password" : $("#pwd").val()
         })
         
        $.ajax({
            url: 'http://localhost:8000/api/signin/',  
            data:  data,  
            contentType: "application/json",
            method:"POST", 
            success: function(response) { 
                console.log('Response from server:', response);
                localStorage.setItem("Token", JSON.stringify(response));
                window.location.replace(base_url);
                
            },
            error: function(xhr, status, err) {
             
               
            }
          });
})
})