
console.log("ss")
function login(){
    var email = document.getElementById('loginEmail').value
    var password = document.getElementById('loginPassword').value
    var csrf = document.getElementById('csrf').value

    if(email == '' && password == ''){
        alert('You must enter both')
    }

    var data = {
        'email' : email,
        'password' : password
    }

    fetch('/api/login/' , {
        method : 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrf,
        },

        body : JSON.stringify(data)
    }).then(result => result.json())
    .then(response => {
        if(response.status == 200){
            window.location.href = '/home'
        }
        else{
            alert(response.message)
        }

    })

}

function register(){
    var username = document.getElementById('regUsername').value
    var password = document.getElementById('regPassword').value
    var cfpassword = document.getElementById('regcfPassword').value
    var email = document.getElementById('regEmail').value
    var address = document.getElementById('Address').value
    var csrf = document.getElementById('csrf').value

    if(username == ''){
        alert('You must enter Username')
    }
    if(password == ''){
        alert('You must enter Password')
    }
    if(address == ''){
        alert('Please enter address')
    }
    if(cfpassword == ''){
        alert('confirm password not entered')
    }
    if(email == ''){
        alert('You must enter email')
    }
    if(password != cfpassword){
        alert('Password and Confirm password not matched')
    }


    var data = {
        'username' : username,
        'password' : password,
        'cfpassword' : cfpassword,
        'email' : email,
        'address' : address,
    }

    fetch('/api/register/' , {
        method : 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrf,
        },

        body : JSON.stringify(data)
    }).then(result => result.json())
    .then(response => {
    console.log(response)

        if(response.status == 200){
           window.location.href = '/'
        }
        else{
            alert(response.message)
        }

    })

}

