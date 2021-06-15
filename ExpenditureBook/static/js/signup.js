$(document).ready(function () {
 $('#submit').click(function (e) {
     e.preventDefault();
     $.ajax({
         type: "POST",
         url: "/register",
         data: $('#form').serialize(),
         success: function (response) {
             if (response == 'success')
             {
             $('.success').removeAttr('style');
             $('#form')[0].reset();
             $('.warning').attr('style', 'display:none');
             $('.fail').attr('style', 'display:none');
            }
            else if(response == 'Password should be same')
            {
                  $('.warning').removeAttr('style');
                  $('#form')[0].reset();
                  $('.success').attr('style', 'display:none');
                  $('.fail').attr('style', 'display:none');
            }
            else
            {
                $('.fail').removeAttr('style');
                $('#form')[0].reset();
                $('.success').attr('style', 'display:none');
                $('.warning').attr('style', 'display:none');
            }
         }
     });

 });

});