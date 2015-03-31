///////////////////////////////////////////////////
///---DOC READY---/////////////////////////////////
///////////////////////////////////////////////////
 	
console.log("page loaded");



// $(document).ready(function (){
	
// });


document.addEventListener("click", function(event){
		var xhr = new XMLHttpRequest();
		xhr.open("GET", "http://localhost:8080", true);
		xhr.onreadystatechange = function() {
		  if (xhr.readyState == 4) {
		  }
		}
		xhr.send();
		console.log("clicked");
});


function sendit() {
	chrome.runtime.sendMessage({text:"new page"});
}

window.onload = sendit();

