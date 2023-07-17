$(document).ready(function(){

 base_url = $("#base_url").val()
 

    $("#signin").click(function(){
        email = $("#email").val()
        pwd = $("#pwd").val()
        loginData = JSON.stringify({
            "email": email,
            "password": pwd
        })
        // axios.post("http://localhost:8000/api/user/sign-in/",  {
        //     params:loginData
            
        //   }, {headers: {
        //     "Accept": "application/json",
        //     "Content-Type": "application/json"
        // }})
        //   .then(function (response) {
        //       console.log(response);
        //   })
        //   .catch(function (error) {
        //     console.log(error);
        //   });
 
        $.post({
            url: 'http://localhost:8000/api/signin/', // Replace this with the URL of your server endpoint
            data:  loginData, // The data to be sent to the server in JSON format
            contentType: 'application/json', 
            accept:"application/json", // The content type of the data being sent
            dataType: 'json', // The expected data type of the response from the server
            success: function(response) {
              // This function is called if the request is successful
              console.log('Response from server:', response);
            },
            error: function(jqXHR, textStatus, errorThrown) {
              // This function is called if there's an error with the request
              console.error('Error:', textStatus, errorThrown);
            }
          });
})
})