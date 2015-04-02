var tab = chrome.tabs;
console.log(tab);
var windows = chrome.windows;
console.log(windows);


chrome.runtime.onMessage.addListener(
    function(request){

        console.log(request.text);


		

//=============================================================================

		chrome.tabs.query({active: true, lastFocusedWindow:true}, function(tabs){  
		    if (tabs[0].incognito) {
		    	var xhr = new XMLHttpRequest();
				xhr.open("GET", "http://localhost:3000/", true);
				xhr.send();
				console.log("testing");
				console.log("in incognito");
			} else {
				console.log("not in incognito");
			}
		});

//=============================================================================

});


 // chrome.tabs.query({active: true, lastFocusedWindow:true}, function(tabs){  
	// 	    console.log(tabs[0].url);
	// 	    if (windows.incognito) {
	// 			console.log("in incognito");
	// 		} else {
	// 			console.log("not in incognito");
	// 		}
	// });













// incognitoTab(tab);

// function incognitoTab (tab) {
// 	if (tab.incognito) {
// 		console.log("in incognito");
// 	} else {
// 		console.log("not in incognito");
// 	}
// }
