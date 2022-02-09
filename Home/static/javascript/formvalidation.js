let activeTab = 0

nextTab = document.getElementsByClassName('next-tab')
nextTab1 = document.getElementsByClassName('next-tab1')
nextTab[0].addEventListener("click", NextTab);
nextTab1[0].addEventListener("click", NextTab1);

previousTab = document.getElementsByClassName('previous-tab')
previousTab[0].addEventListener("click", PrevTab);
previousTab[1].addEventListener("click", PrevTab);


var tempOrNot = false
console.log(tempOrNot)
hide()

var tab1Tabs = document.querySelectorAll(".tab1 input,textarea")
function NextTab() {
    document.body.scrollTop = document.documentElement.scrollTop = 0;
   

    if(tab1Tabs[0].value !== "" && tab1Tabs[1].value !== "" && tab1Tabs[2].value !==""&& tab1Tabs[3].value !==""&& tab1Tabs[4].value !==""&& tab1Tabs[5].value !==""&& tab1Tabs[6].value !==""&& tab1Tabs[7].value !==""&& tab1Tabs[8].value !==""){
        activeTab = activeTab + 1
        hide()
    }else{
        for (let index = 0; index < tab1Tabs.length; index++) {
            if(tab1Tabs[index].value === ""){
                tab1Tabs[index].style.borderColor = "red";
            }
        }
    }
}

var tab2Tabs = document.querySelectorAll(".tab2 input,select")
function NextTab1() {
    document.body.scrollTop = document.documentElement.scrollTop = 0;

    console.log(tempOrNot)
    console.log(tab2Tabs)
    if(tab2Tabs[0].value !== "" && tab2Tabs[1].value !== "" && tempOrNot === true){
        console.log("hello")
        activeTab = activeTab + 1
        hide()
    }else{
        console.log("fill in date")
    }


}


check = document.getElementById("id_required_access")
starttime = document.getElementById("id_start_time")
endtime = document.getElementById("id_end_time")

// id_end_time
check.addEventListener('change', (event) => {
    if (event.target.value === "TEMPORARY"){
        tempOrNot = false
        starttime.required = true;
        endtime.required = true;
        
        starttime.addEventListener('change', (event) =>{
            console.log(tempOrNot)
                if(starttime.value !== "" && endtime.value !== ""){
                    console.log(event.target.value)
                    tempOrNot = true
                    console.log(tempOrNot)              
                }else{
                    tempOrNot = false
                }
        })
        endtime.addEventListener('change', (event) =>{
            console.log(tempOrNot)
                if(starttime.value !== "" && endtime.value !== ""){
                    console.log(event.target.value)
                    tempOrNot = true
                    console.log(tempOrNot)              
                }else{
                    tempOrNot = false
                }
        })


        // if(tab2Tabs[1].value !== "" && tab2Tabs[2].value !== ""){
        //     console.log("YOYOYOYOYOY")
        //     tempOrNot = true
            
        // }
    }else if(event.target.value === "PERMANENT"){
        starttime.required = false;
        endtime.required = false;
        tempOrNot = true
        console.log(tempOrNot)
    }
    
});




function PrevTab() {
    activeTab = activeTab - 1
    hide()
    // for (let index = 0; index < hello.length; index++) {
    //     hello[index].style.borderColor = "black";
    // } 

    document.body.scrollTop = document.documentElement.scrollTop = 0;
}


function hide(){
    console.log(activeTab)
    tab1 = document.getElementsByClassName("tab1")
    tab2 = document.getElementsByClassName("tab2")
    tab3 = document.getElementsByClassName("tab3")
    
    if(activeTab === 0){
        tab1[0].style.display = "block"
        tab2[0].style.display = "none"
        tab3[0].style.display = "none"
    }else if(activeTab === 1){
        tab1[0].style.display = "none"
        tab2[0].style.display = "block"
        tab3[0].style.display = "none"
    }else{
        tab1[0].style.display = "none"
        tab2[0].style.display = "none"
        tab3[0].style.display = "block"
    }
}












// hello = document.querySelectorAll(".tab1 input")

// console.log(hello)


// check = document.getElementById("id_required_access")

// starttime = document.getElementById("id_start_time")
// endtime = document.getElementById("id_end_time")

// id_end_time
// check.addEventListener('change', (event) => {
//     if (event.target.value === "TEMPORARY"){
//         starttime.required = true;
//         endtime.required = true;
//         console.log("temporary")
//     }else if(event.target.value === "STANDARD"){
//         starttime.required = false;
//         endtime.required = false;
//         console.log("standard")
//     }
//     console.log(check)
//   });


  

