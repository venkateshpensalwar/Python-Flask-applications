$(document).ready(function () {
    $('#credit').click(function (e) {
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: "/Addcash",
            data: $('#add_cash').serialize(),
            success: function (response) {
                $('#add_cash')[0].reset()
                 $('tbody').append(
                      `<tr>
                           <td class="text-start">`+response['purpose']+`</td>
                            <td class="text-end">`+response['category']+`</td>
                            <td class="text-end">`+response['total']+`</td>
                            <td class="text-end">`+response['date']+`</td>
                        </tr>
                      </tr>`
                  )
                  var cash = parseInt($('#money').text());
                  $('#money').text(cash + response['total'])
            }
        });
    });
});