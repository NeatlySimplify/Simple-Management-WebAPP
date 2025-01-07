function validate(){
    const password = $('#password').val();
    const patterns = {
        lower: /[a-z]/,
        upper: /[A-Z]/,
        number: /\d/,
        lenght: /^.{6,20}$/
    }
    const check = [
        {id: "#atLeastALower-char", valid: patterns.lower.test(password)},
        {id: "#atLeastAUpper-char", valid: patterns.upper.test(password)},
        {id: "#atLeastANumber", valid: patterns.number.test(password)},
        {id: "#atLeastLenght", valid: patterns.lenght.test(password)}
    ]
    let isValid = true;
    check.forEach(({id, valid}) => {
        let $li = $(id);
        if (valid) {
            $li.removeClass("text-secondary").addClass("text-success");
        }
        else {
            $li.removeClass("text-success").addClass("text-secondary");
        }
    });
    return isValid
}

function checkpw() {
    const $confirm = $("#confirm-password");
    const password = $("#password").val();
    const confirmPassword = $confirm.val();
    
    if (password === confirmPassword) {
        $confirm.removeClass("is-invalid").addClass("is-valid");
        return true;
    } else {
        $confirm.removeClass("is-valid").addClass("is-invalid");
        return false;
    }
}

$(document).ready(function () {
    $("#password").on("input", function () {
        validate();
    });
        
    $("#confirm-password").on("input", function () {
        const confirm_password = $(this).val();
        const password = $('#password').val();
        checkpw();
    });
    
    $('#submitBtn').on('click', (event) => {
        event.preventDefault();
        const isValid = validate() && checkpw();
        if (!isValid) {
            alert("Há problemas com seu formulário, por favor preencha os campos corretamente.");
        }
        else {
            const data = {
                name: $('#nome').val(),
                email: $('#email').val(),
                password: $('#password').val()
            }
            const jsonData = JSON.stringify(data);
            $.ajax({    
                url: window.location.href,
                method: "POST",
                contentType: "application/json",
                data: jsonData,
                success: function(response, xhr) {
                    if (xhr.status === 201) {
                        alert(response.message);
                        window.location.href = "/login";
                    }
                },
                error: function(xhr) {
                    const errorData = xhr.responseJSON;
                    if (errorData.message) {
                        alert(`Error: ${errorData.message}`);
                    } else {
                        alert('An unexpected error occurred.');
                    }
                }
            });
        }
    });
});

