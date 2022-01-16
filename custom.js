$("#personal_information").click(function(e){
    e.preventDefault();
    formUrl = $('#personal_information_form').attr('action');
    t=$(this).closest("form")
    t.ajaxSubmit({url:formUrl,dataType:'JSON',success:function(e,r,n,l){
    if(e.status == 'success'){toastr.success(e.message);}else{toastr.error(e.message);}setTimeout(function(){
    if(typeof(e.print_error) != "undefined" && e.print_error !== null){
       var html = '<ul>';
       for(var key in e.print_error) {
           html +="<li><ul class='error'><li>"+key+" :</li>";
           html +="<li>"+e.print_error[key][0]+"</li></ul></li>";
        }
        html +='</ul>';
        $(".error-messages").html(html);
    }else{
        window.location.href = e.url;
    }},2e3)}})
})
function valid_ssn (elementValue){
		var  ssnPattern = /^[0-9]{3}\-?[0-9]{2}\-?[0-9]{4}$/;
		return ssnPattern.test(elementValue);
	}
$("#moov_information").click(function(e){
    var customerID = "b3d613316e210417547fcc22e59e71b23b9bfe6f";
    var accountID = "d2ae1c34-9af4-48a9-8c58-17282c4dd8a8";
    var formUrl = $('#admin_ach_form').attr('action');
    updateMoovResponseInUserProfile(customerID,accountID,formUrl);
    e.preventDefault();
//    var moovToken = $("#id_HiddenInput_token").val();
//    const moov = Moov(moovToken);
//    const customer = {
//				firstName: admin_ach_form.first_name.value,
//				lastName: admin_ach_form.last_name.value,
//				email: admin_ach_form.email.value,
//				ssn: admin_ach_form.Social_Security_Number.value,
//				type: 'individual'
//
//			};
//	const account = {
//				type: admin_ach_form.type.value, /* 'Checking' or 'Savings' */
//				holderName: `${admin_ach_form.first_name.value} ${admin_ach_form.last_name.value}`,
//				accountNumber: admin_ach_form.checking_account_number.value,
//				routingNumber: admin_ach_form.routing_number.value
//			};
//
//	moov.quickEnroll(customer, account)
//			.then((res) => {
//
//			    console.log(res)
//			});

})


function updateMoovResponseInUserProfile(customerID,accountID,formUrl){
     $.ajax({
            url: formUrl,
            type: 'POST',
            data: {'customerID':customerID,'accountID':accountID,'csrfmiddlewaretoken':window.CSRF_TOKEN},
            success:function(res){
                toastr.success(res.message);
            }
     })
}



$("#add_apikey_btn").click(function(e){
    e.preventDefault();
    formUrl = $('#add_apikey_form').attr('action');
    t=$(this).closest("form")
    t.ajaxSubmit({url:formUrl,dataType:'JSON',success:function(e,r,n,l){
    if(e.status == 'success'){toastr.success(e.message);}else{toastr.error(e.message);}setTimeout(function(){
    if(typeof(e.print_error) != "undefined" && e.print_error !== null){
       var html = '<ul>';
       for(var key in e.print_error) {
           html +="<li><ul class='error'><li>"+key+" :</li>";
           html +="<li>"+e.print_error[key][0]+"</li></ul></li>";
        }
        html +='</ul>';
        $(".error-messages").html(html);
    }else{
        window.location.href = e.url;
    }},2e3)}})
})

$("#update_apikey_btn").click(function(e){
    e.preventDefault();
    formUrl = $('#update_apikey_form').attr('action');
    t=$(this).closest("form")
    t.ajaxSubmit({url:formUrl,dataType:'JSON',success:function(e,r,n,l){
    if(e.status == 'success'){toastr.success(e.message);}else{toastr.error(e.message);}setTimeout(function(){
    if(typeof(e.print_error) != "undefined" && e.print_error !== null){
       var html = '<ul>';
       for(var key in e.print_error) {
           html +="<li><ul class='error'><li>"+key+" :</li>";
           html +="<li>"+e.print_error[key][0]+"</li></ul></li>";
        }
        html +='</ul>';
        $(".error-messages").html(html);
    }else{
        window.location.href = e.url;
    }},2e3)}})
})


$(document).on("click", "#delete_api_keybtn", function(e){
    e.preventDefault();
    var id = $(this).attr('apikeyId');
    swal({
          title: "Are you sure?",
          text: "Do you want delete this apikey ?",
          icon: "warning",
          buttons: true,
          dangerMode: true,
        }).then(function(res){
			if(res){
			    console.log('id');
			    window.location.href = "http://127.0.0.1:8000/admin-panel/organization_api/delete-api-key/"+id+"/";
			}
		})
});


$(document).on("click", "#delete_pool_btn", function(e){
    e.preventDefault();
    var id = $(this).attr('poolId');
    swal({
          title: "Are you sure?",
          text: "Do you want delete this pools ?",
          icon: "warning",
          buttons: true,
          dangerMode: true,
        }).then(function(res){
			if(res){
			    console.log('id');
			    window.location.href = "http://127.0.0.1:8000/admin-panel/pools/delete-pools/"+id+"/";
			}
		})
});


$("#btnsave").click(function(e){
    e.preventDefault();
    var nm = $("#nameid").val();
    var em = $("#emailid").val();
    var pass = $("#passwordid").val();
    //var act = $("#activeid").val();
    var act = $('#activeid').is(':checked') ? 'on' : '';


    var active = 'False';
    if(act=='on')
    {
       var active='True';
    }
    var crf = $("input[name=csrfmiddlewaretoken]").val();
    if(nm=='')
    {
       toastr.error('please enter name');
       return false;
    }/*else if(em!='')
    {
        const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        var valid_email= re.test(String(em).toLowerCase());
        if(valid_email=='False')
        {
           toastr.error('please enter valid email');
           alert('here');
        }
    }*/



    else
    {
      mydata={name:nm,email:em,password:pass,status:active,csrfmiddlewaretoken:crf};
      $.ajax({
				//url: 'http://127.0.0.1:8000/create-pauses/',
				url: "http://127.0.0.1:8000/admin-panel/pools/save/",
				type: 'POST',
				data: mydata,
				success: function(data) {
				console.log(data);
				if ($.trim(data.status) == 'success')
                {
                        toastr.success(data.message);
                 }
                 else
                  {
                        toastr.error(data.message);
                   }
				}
			})
    }
 });


 $(document).ready(function() {
   let todayDate = new Date().getDate();
   let endD = new Date(new Date().setDate(todayDate));
   $('#expires_api_check').datetimepicker({
      startDate : endD,
      weekStart: 7,
      todayBtn:  1,
      autoclose: 1,
      todayHighlight: 1,
   });

		//endDate(new Date());
	});
    $(document).ready(function() {
	$('#expires_api_check').keypress(function(e) {
			e.preventDefault();
		});
 $('#expires_api_check').bind('copy paste cut',function(e) {
 e.preventDefault();
 });
});


$("#infomation_input_btn").click(function(e){
    e.preventDefault();
    formUrl = $('#test_AddInformation').attr('action');
    t=$(this).closest("form")
    t.ajaxSubmit({url:formUrl,dataType:'JSON',success:function(e,r,n,l){
    if(e.status == 'success'){toastr.success(e.message);}else{toastr.error(e.message);}setTimeout(function(){
    if(typeof(e.print_error) != "undefined" && e.print_error !== null){
       var html = '<ul>';
       for(var key in e.print_error) {
           html +="<li><ul class='error'><li>"+key+" :</li>";
           html +="<li>"+e.print_error[key][0]+"</li></ul></li>";
        }
        html +='</ul>';
        $(".error-messages").html(html);
    }else{
        window.location.href = e.url;
    }},2e3)}})
})

$(".checkbox_key").click(function() {
    $(".checkbox_key").prev().prop('checked', false);
});


$(document).ready(function() {
   let todayDate = new Date().getDate();
   let endD = new Date(new Date().setDate(todayDate));
   $('#start_date').datetimepicker({
      startDate : endD,
      weekStart: 7,
      todayBtn:  1,
      autoclose: 1,
      todayHighlight: 1,
   });

		//endDate(new Date());
	});
    $(document).ready(function() {
	$('#start_date').keypress(function(e) {
			e.preventDefault();
		});
 $('#start_date').bind('copy paste cut',function(e) {
 e.preventDefault();
 });
});



$(document).ready(function() {
   let todayDate = new Date().getDate();
   let endD = new Date(new Date().setDate(todayDate));
   $('#end_date').datetimepicker({
      startDate : endD,
      weekStart: 7,
      todayBtn:  1,
      autoclose: 1,
      todayHighlight: 1,
   });

		//endDate(new Date());
	});
    $(document).ready(function() {
	$('#end_date').keypress(function(e) {
			e.preventDefault();
		});
 $('#end_date').bind('copy paste cut',function(e) {
 e.preventDefault();
 });
});


$(document).on('click', '#create_response_message_btn', function(e) {
e.preventDefault();
    var formErrors = 0;
    $('.validateInput').each(function(){
        if($.trim($(this).val()) == '') {
            $(this).removeClass('border border-dark');
            $(this).addClass('border border-danger');
            formErrors++;
        } else {
            $(this).removeClass('border border-danger');
            $(this).addClass('border border-dark');
        }
    });
    var fd = new FormData($('#add_response_messages_form')[0]);
    if(formErrors == 0 && formErrors == '0') {
        fd.append('title',$('#title').val())
        fd.append('description',$('#description').val())
        fd.append('message',$('#message').val())
        fd.append('image',$('#image')[0].files[0])
        fd.append('csrfmiddlewaretoken', $('input[name=csrfmiddlewaretoken]').val())
        console.log(fd)
        $.ajax({
            url: '/create-response-message/',
            type: 'POST',
            data: fd,
            cache: false,
            contentType: false,
            processData: false,
            success: function(data) {
                if ($.trim(data.status) == 'success')
                {
                    toastr.success(data.message);
                }
                else
                {
                    toastr.error(data.message);
                }
            }
        })
    }
	});






$(document).on("click", "#delete_response_message", function(e){
    e.preventDefault();
    var id = $(this).attr('responseId');
    swal({
          title: "Are you sure?",
          text: "Do you want delete this response message ?",
          icon: "warning",
          buttons: true,
          dangerMode: true,
        }).then(function(res){
			if(res){
			    console.log('id');
			    window.location.href = "/delete-response-message/"+id+"/";
			}
		})
});




$(document).on('click', '#update_response_message_btn', function(e) {
e.preventDefault();
    var formErrors = 0;
    $('.validateInput').each(function(){
        if($.trim($(this).val()) == '') {
            $(this).removeClass('border border-dark');
            $(this).addClass('border border-danger');
            formErrors++;
        } else {
            $(this).removeClass('border border-danger');
            $(this).addClass('border border-dark');
        }
    });
    var fd = new FormData($('#update_response_messages_form')[0]);
    if(formErrors == 0 && formErrors == '0') {
        fd.append('title',$('#title').val())
        fd.append('description',$('#description').val())
        fd.append('message',$('#message').val())
        fd.append('image',$('#image')[0].files[0])
        fd.append('csrfmiddlewaretoken', $('input[name=csrfmiddlewaretoken]').val())
        console.log(fd)
        $.ajax({
            url: $(this).attr('action'),
            type: 'POST',
            data: fd,
            cache: false,
            contentType: false,
            processData: false,
            success: function(data) {
                if ($.trim(data.status) == 'success')
                {
                    toastr.success(data.message);
                }
                else
                {
                    toastr.error(data.message);
                }
            }
        })
    }
	});








