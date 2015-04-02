/////  Message from Content Script,  /////
/////  Saying a new page was loaded /////
chrome.runtime.onMessage.addListener(
    
    function(request){
    	/////  When we get a message  /////
    	/////  Check if the last focused tab was in Incognito mode  /////
		chrome.tabs.query({active: true, lastFocusedWindow:true}, function(tabs){  
		    if (tabs[0].incognito) {
		    	/////  If it was Incognito  /////
		    	/////  Make HTTP Request to the server  /////
		    	var xhr = new XMLHttpRequest();
				xhr.open("GET", "http://localhost:3000/", true);
				xhr.send();
				console.log("in incognito");
			} else {
				console.log("not in incognito");
			}
		});
});