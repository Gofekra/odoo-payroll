function attendance_data_loop(id) {
    openerp.jsonRpc('/longpolling/poll','call',
    {
        "channels":["attendance"],
        "last":id
    }).then(function(r){
        for(i=0; i<r.length; i++){
            console.log(r[i]);
            get_attendance(r[i].message);
        }
        if(r.length>0)
            attendance_data_loop(r[r.length-1].id);
        else
            attendance_data_loop(id);
        }, function(r) {
            attendance_data_loop(id);
        }
    )
};
attendance_data_loop(0);

function employee_state(){
    if ($("#hr_employee").val() != '') {
        openerp.jsonRpc("/hr/attendance/report", 'call', {
            'employee': $("#hr_employee").val(),
        }).done(function(data){
            if(data == "present") {
                $("#login").addClass("hidden");
                $("#logout").removeClass("hidden");
            }
            if(data == "absent") {
                $("#login").removeClass("hidden");
                $("#logout").addClass("hidden");
            }
        });
    }
    else {
        $("#login").addClass("hidden");
        $("#logout").addClass("hidden");
    }
}

/* Come and Go */
function come_and_go(){
openerp.jsonRpc("/hr/attendance/come_and_go", 'call', {
    'employee_id': $("#hr_employee").val(),
    }).done(function(data){
        console.log(data);
    });
}

function get_attendance(id){
openerp.jsonRpc("/hr/attendance/" + id, 'call', {
    }).done(function(data){
        console.log(data);
        $("#login").addClass("hidden");
        $("#logout").addClass("hidden");
        $("#attendance_div").load(document.URL +  " #attendance_div");
        $('#Log_div').fadeIn();
        if (data.employee.img !== null)
            $("#employee_image").html("<img src='data:image/png;base64," + data.employee.img + "''/>");
        if (data.employee.img === null)
            $("#employee_image").html("<img src='/hr_payroll_attendance/static/src/img/icon-user.png'/>");
        if (data.employee.state === 'present')
            $("#employee_message").html("<h2>Welcome!</h2><h2>" + data.employee.name +"</h2>");
        if (data.employee.state === 'absent'){
            $("#employee_message").html("<h2>Goodbye!</h2><h2>" + data.employee.name +"</h2>");
            $("#employee_worked_hour").html("<h4><strong>Du har idag jobbat: </strong>" + "xxx" +" minuter</h4>");
            $("#employee_time_bank").html("<h4><strong>Din tidbank är: </strong>" + "xxx" +" minuter</h4>");
        }
        $('#Log_div').delay(5000).fadeOut("slow");
    });
}

function clock() {
    var today = new Date();
    var year = today.getFullYear();
    var month = today.getMonth() + 1;
    var day = today.getDate();
    var hour = today.getHours();
    var minute = today.getMinutes();
    //var second = today.getSeconds();
    minute = checkTime(minute);
    //second = checkTime(second);
    $("#time").text(hour + ":" + minute);
    $("#date").text(year + "-" + month + "-" + day);
    var time = setTimeout(clock, 500);
}
function checkTime(i) {
    if (i < 10)
        i = "0" + i;
    return i;
}
