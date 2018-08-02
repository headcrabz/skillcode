window.jQuery = window.$ = jQuery;

 $(window).load(function(){

  $("#collectinfo_teacher").click(function(e){
			e.preventDefault()
			var mForm = $("#info_teacher").serialize()
			$.ajax({
				type: "POST",
				url: "{% url 'ajax_teacher' %}",
				data: mForm,
				success: function(data){
					console.log("success")
            // console.log(data)
            console.log(data)
            $('#exampleModal2').modal('toggle');
            console.log("successteacher")
            $('.modal').on('hidden.bs.modal', function(){
            	$(this).find('form')[0].reset();
            });
            showFlashMessage("Information Sent, you will hear back soon!")
            // $("#modalMessage").html("<p>" + data + "</p>")
            //  $("#marketingModal").modal("hide");
        },
        error: function(data){
          	alert('please fill out the required fields')
            var obj = data.responseJSON
        },
    });
		});


  	$("#collectinfo").click(function(e){
  		e.preventDefault()
  		var mForm = $("#info").serialize()
  		$.ajax({
  			type: "POST",
  			url: "{% url 'ajax_report' %}",
  			data: mForm,
  			success: function(data){
            // console.log(data)
            console.log(data)
            $('#exampleModal').modal('toggle');
            $('.modal').on('hidden.bs.modal', function(){
            	$(this).find('form')[0].reset();
            });
            showFlashMessage("Information Sent, you will hear back soon!")
            // $("#modalMessage").html("<p>" + data + "</p>")
            //  $("#marketingModal").modal("hide");
        },
        error: function(data){

            alert('please fill out the required fields')
            var obj = data.responseJSON
            // console.log(obj)
            // console.log(obj.email)
            // $("#modalMessage").html("<p style='color:red;'>" + obj.email + "</p>")
        },
    });
  	});
  });

