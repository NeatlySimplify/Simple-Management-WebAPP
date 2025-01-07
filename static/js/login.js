$(document).ready(function () {
    $('#submitBtn').on('click', (event) => {
        event.preventDefault();
        const data = {
            email: $('#email').val(),
            password: $('#password').val()
        }
        const jsonData = JSON.stringify(data);
        $.ajax({    
            url: window.location.href,
            method: "POST",
            contentType: "application/json",
            data: jsonData,
            xhrFields: {
                withCredentials: true
            },
            success: function(response, xhr) {
                    if (xhr.status === 200) {
                        const token = response.token;
                        document.cookie = `access_token=${token}; Path=/; SameSite=Lax;`
                        window.location.href = "/";
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
    });
});