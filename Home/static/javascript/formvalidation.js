check = document.getElementById("id_required_access")

starttime = document.getElementById("id_start_time")
endtime = document.getElementById("id_end_time")

id_end_time
check.addEventListener('change', (event) => {
    if (event.target.value === "TEMPORARY"){
        starttime.required = true;
        endtime.required = true;
        console.log("temporary")
    }else if(event.target.value === "STANDARD"){
        starttime.required = false;
        endtime.required = false;
        console.log("standard")
    }
    console.log(check)
  });


  

