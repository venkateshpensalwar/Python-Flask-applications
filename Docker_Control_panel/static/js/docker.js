
        $(document).ready(function () {
            $('#submit').click(function (e) {
                e.preventDefault();
               $.ajax({
                   type:"POST",
                   url: "http://192.168.0.110/cgi-bin/docker.py",
                   data: $('#form').serialize(),
                   success: function (response) {
                       $('.res').text(response)
                      $('#form')[0].reset()
                   },
               });
            });
        });