$(document).ready(function () {
    $('#submit').click(function (e) {
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: "/login",
            data: $('#form').serialize(),
            success: function (response) {
                if(response == 'error')
                {
                    
                    $('.fail').text('UserName or Password is Wrong')
                    $('.fail').removeAttr('style');
                }
                else if(response == 'Account does Not exist')
                {
                    $('.fail').text('Account does Not exist')
                    $('.fail').removeAttr('style')
                }
                else
                {
                    window.location.href='/dash'
                    console.log('success')
                }
            }
        });
    });
});