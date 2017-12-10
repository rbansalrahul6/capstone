var main_page = ["Dashboard", "Settings", "Logout"];

var course_page = ["Course Notes", "Assignment", "Inbox", "Logout"];
var main_id=["dashboard","inbox","setting","logout"]

function bgcol(idobject) {
    for(var item in main_id){
    	if(idobject==item){
    		document.getElementById(item).style.backgroundColor='#00BCD4';
    	}
    	else{
    		document.getElementById(item).style.backgroundColor='#37474F';
    	}
    }
}

$("a").click(function()
{
	alert(this.id);
});