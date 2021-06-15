


$(document).ready(function () {
    $('#add_purpose').click(function (e) {
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: "/AddExpenses",
            data: $('#add_expenses').serialize(),
            success: function (response) {
                 $('#add_expenses')[0].reset()
                  $('tbody').append(
                      `<tr>
                           <td class="text-start">`+response['purpose']+`</td>
                            <td class="text-end">`+response['category']+`</td>
                            <td class="text-end">`+response['total']+`</td>
                            <td class="text-end">`+response['date']+`</td>
                        </tr>
                      </tr>`
                  )
                  var cash = $('#money').text()
                  var total = cash - response['total']
                  $('#money').text(total)
            }
        });
    });
});