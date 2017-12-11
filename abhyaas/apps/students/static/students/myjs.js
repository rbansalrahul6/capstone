var main_page = ["Dashboard", "Settings", "Logout"];

var course_page = ["Course Notes", "Assignment", "Inbox", "Logout"];
var main_id=["dashboard","inbox","setting","logout"]

function bgcol(idobject) {
	var i,len;
    len=main_id.length;
    for(i=0;i<len;i++){
   		window.alert(main_id[i])
    	if(idobject==main_id[i]){  

    		document.getElementById(main_id).style.backgroundColor='#00BCD4';
    	}
    	else{
    		document.getElementById(main_id).style.backgroundColor='#37474F';
    	}
    }
}

